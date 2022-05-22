from flask import Flask
from flask import jsonify
from flask import request
import requests
from concurrent.futures import ThreadPoolExecutor
import base64
from deepface import DeepFace

executor = ThreadPoolExecutor(2)
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
	pic = request.values['picture']
	with open('pic.jpg', 'wb') as file:
		jiema = base64.b64decode(pic)
		file.write(jiema)
	obj = DeepFace.analyze(img_path = "pic.jpg", actions = ['age', 'gender'])
	print(obj)
	return obj


if __name__ == "__main__":
	server.run(host='0.0.0.0')

