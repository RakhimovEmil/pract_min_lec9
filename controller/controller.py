from flask import Flask, request, make_response
import requests
import json

app = Flask(__name__)

@app.route("/storage/<filename>", methods=['GET', 'PUT', 'DELETE'])
def controller(filename):
  url = 'http://service:8081/storage/' + filename
  
  if request.method == 'GET':
    res = requests.get(url)
    return make_response(res.text, res.status_code)
    
  if request.method == 'PUT':
    if request.is_json:
      req = request.get_json()
      res = requests.put(url, json=req)
      return make_response("", 201)
    else:
      return make_response("", 400);
  
  if request.method == 'DELETE':
    res = requests.delete(url, data=filename)
    return make_response("", 204)

if __name__ = "__main__":
  app.run(host='0.0.0.0', port=8080)