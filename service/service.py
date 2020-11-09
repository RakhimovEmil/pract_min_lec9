from flask import Flask, request,make_response, jsonify, json
import redis
import pymongo
from bson import json_util
from pprint import pformat

mongoClient = pymongo.MongoClient(host='0.0.0.0', port=27017)
mongo_table = mongoClient['hw9']['cache']

cache = redis.Redis(host='0.0.0.0', port=6379, decode_responses=True)
cache.ping()

app = Flask(__name__)

@app.route("/storage/<filename>", methods=['GET'])
def get_service(filename):
	if cache.exists(filename):
		url = 'http://repository_:8082/storage/'
		return make_response(cache.get(filename), 200)
  
	if mongo_table.find_one({'key':filename}) != None:
		mongo_cach = mongo_table.find_one({'key':filename})["value"]
		cache.set(filename, json.loads(json_util.dumps(mongo_cach)))
		return make_response(json.loads(json_util.dumps(mongo_cach)), 200)
  
	res = make_response({}, 404)
	return res

@app.route("/storage/<filename>", methods=["PUT"])
def put_collection(filename):
    req = request.get_json()
    mongo_table.insert_one({'key':filename, 'value':json.dumps(req)})

@app.route("/storage/<filename>",methods=["DELETE"])                         
def delete_collection(filename):
    if cache.exists(filename):                                                   
        cache.delete(filename)  
        
    if mongo_table.find_one({'key':filename}) != None:
        mongo_table.delete_one({'key':filename}) 
  
if __name__ == '__main__':                                                      
    app.run(host= '0.0.0.0', port = 8081, debug=True)                                                                                   
