"""
   Simple self contained class CRUD library for Pymongo
   (client should not use import pymongo)
   version 1.00

   see MongoLibDemo for usage
   You can copy this library in  \python\mongolib


"""
import pymongo
import sys

class mutils:

	def __init__(self):
		#constructor
		#private class variables
		self.__errorMsg="No Error"
		self.__client=""
		self.__dbname=""

	def setDB(self, db_name):
		# Setting the current database
		# Use this method when the login user has access to more than one database
		self.__dbname=db_name

	def getDB(self):
		# get the currect database
		return self.__dbname

	def mConnect(self, connectionString):
		# mConnent get a  connection string in this format "user_name:user_pwrd@uri:port/defaultDB"
		# return a list of available databases for this URL
		# return False for any issues
		# if you are going to work with multiple databases, you should set a database or create mConnect object for each database
		# if you have access to multiple database, .

		try:
			self.__client = pymongo.MongoClient('mongodb://'+connectionString)
			l=list()
			try:
				self.__dbname = self.__client.get_default_database().name
				l.append(self.__client.get_default_database().name)
				return l
			except:
				self.__errorMsg="Single Database"


			try:
				l = self.__client.database_names()
				return l
			except:
				self.__errorMsg="Multiple Databases"

		except:
			self.__errorMsg=sys.exc_info()[0]
			return [False]

	def getDBColl(self):
		# return list of collections per database
		# error if the database does not exist
		try:
			dbo=self.__client[self.__dbname]
			return list(dbo.collection_names())
		except:
			self.__errorMsg=sys.exc_info()[0]
			return [False]

	def getColDocs(self, co_name):
		# parameter; collection name
		# return list of documents per collection
		try:
			return list(self.__client[self.__dbname][co_name].find({}))
		except:
			self.__errorMsg=sys.exc_info()[0]
			return [False]

	def getErrMsg(self):
		# get last error message
		return self.__errorMsg

	def delCollDocs(self, co_name, criteria ):
		# parameters; collection name, criteria
		# criteria is dictionary should be in this format {"id":""}
		try:
			db=self.__client[self.__dbname]
			db[co_name].delete_many(criteria)
			return [True]
		except:
			self.__errorMsg=sys.exc_info()[0]
			return [False]


	def findDoc(self, co_name, criteria):
		# parameters; collection name, criteria
		# criteria is a dictionary like {"id":""}
		try:
			print(criteria)
			db=self.__client[self.__dbname]
			return list(db[co_name].find(criteria))
		except:
			self.__errorMsg=sys.exc_info()[0]
			return [False]

	def updateDoc(self, co_name, filter, set_criteria, upsert_flag=False):
		# parameters; collection name, filter, criteria, upsert flag (insert /update)
		# filter, criteria is a dictionary like {"id":""}
		# {"id":"MZZZZ"},{"$set": {"name":"qZZZZ"}}
		# upsert default value is False
		try:
			db=self.__client[self.__dbname]
			db[co_name].update_one(filter, set_criteria, upsert=upsert_flag)
			return [True]
		except:
			self.__errorMsg=sys.exc_info()[0]
			return [False]

	def createDoc(self, co_name, doc):
		# parameters; collection name, document
		# document is a dictionary like {"id":""}
		try:
			db=self.__client[self.__dbname]
			db[co_name].insert_one(doc)
			return [True]
		except:
			self.__errorMsg=sys.exc_info()[0]
			return [False]
