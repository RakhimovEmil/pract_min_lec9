from flask import Flask, request, make_response
import requests
import json
from service import service

app = Flask(__name__)
my_service = service()

@app.route("/storage/<filename>", methods=['GET', 'PUT', 'DELETE'])
def controller(filename):
  if request.method == 'GET':
    if my_service.get(filename):
		  return make_response(my_service.get(filename), 200)
	  return make_response("", 404)
    
  if request.method == 'PUT':
    if request.is_json:
      my_service.put(filename, json.dumps(request.get_json()))
      return make_response("", 201)
    else:
      return make_response("", 400);
  
  if request.method == 'DELETE':
    my_service.delete(filename)  
    return make_response("", 204)

if __name__ = "__main__":
  app.run(host='0.0.0.0', port=8080)
