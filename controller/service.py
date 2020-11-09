from bson import json_util
from flask import jsonify, json
from repository import redis_repository, mongo_repository

class service:
	def __init__(self):
		self.mongo=mongo_repository()
		self.redis=redis_repository()
    
	def get(self,filename):
		if self.redis.exists(filename):
			return self.redis.get(filename)
		if self.mongo.exists(filename):
			cur = json.loads(json_util.dumps(self.mongo.get(filename)))
			self.redis.put(filename, cur)
			return cur
		return 
    
	def put(self, filename, value):
		self.mongo.put(filename, value)
	
  def delete(self, filename):
		if self.redis.exists(filename):                                                   
			self.redis.delete(filename)       
		if self.mongo.exists(filename):
			self.mongo.delete(filename)  
