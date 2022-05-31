from flask import Flask
from flask import jsonify
from flask import request
import requests
from concurrent.futures import ThreadPoolExecutor
import threading
import base64
from deepface import DeepFace

number = 1
executor = ThreadPoolExecutor(2)
mutex = threading.Lock()
def runAI(fileName):
	try:
		obj = DeepFace.analyze(img_path = fileName, actions = ['age', 'gender'])
		print('predict successfully')
		print(obj)
	except:
		print('Error while detecting face')
	return 'cannot detect face'
# executor.submit(long_task, 'hello', 123)

server = Flask(__name__)
prefix = '/ai'

@server.route("/")
def hello():
	return "Hello World from flask!"

@server.route("/ai")
def test():
	res = requests.get('http://backend:3000/api')
	print(res.text)
	return "Hello World from flask AI route!"

@server.route(prefix + '/version')
def ver():
	return jsonify({'ver': '0.1.0'})

@server.route(prefix + '/predict', methods=['POST'])
def predict():
	global mutex, number
	pic = request.values['picture']
	mutex.acquire()
	filename = 'pic' + str(number) + '.jpg'
	with open(filename, 'wb') as file:
		jiema = base64.b64decode(pic)
		file.write(jiema)
	executor.submit(runAI, filename)
	number += 1
	mutex.release()
	return 'submit successfully'


if __name__ == "__main__":
	server.run(host='0.0.0.0')