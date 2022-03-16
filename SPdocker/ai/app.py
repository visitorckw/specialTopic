from flask import Flask
from flask import jsonify
import requests

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
@server.route(prefix+'/version')
def ver():
  return jsonify({'ver': '0.1.0'})

if __name__ == "__main__":
  server.run(host='0.0.0.0')

