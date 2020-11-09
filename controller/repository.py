import redis
import pymongo

class redis_repository:
	def __init__(self):
		self.cache = redis.StrictRedis(host ='0.0.0.0', port =6379, decode_responses=True)
  
  def get(self,key):
		return self.cache.get(key)
	
  def put(self,key,value):
		self.cache.set(key,value)
  
  def delete(self,key):
		self.cache.delete(key)       
	
	def exists(self,key):
		return self.cache.exists(key)
    
class mongo_repository:
	def __init__(self):
		self.client = pymongo.MongoClient(host='0.0.0.0', port=27017)
		self.mongo_table = self.client['hw9']['cache']
  
  def get(self,key):
		return self.mongo_table.find_one({'key':key})["value"]
    
  def put(self,key,value):
		self.mongo_table.insert_one({'key':key, 'value':value})
  
	def delete(self, key):
		self.mongo_table.delete_one({'key':key})                                          
	
	def exists(self,key):
		return self.mongo_table.find_one({'key':key})
