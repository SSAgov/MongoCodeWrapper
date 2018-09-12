
"""
   Demo for MongoUtils
"""
import sys
import ast
import mongoUtils

def mainMenu():
	MyObj=mongoUtils.mutils()
	print("Enter Connection String [user_name:user_pwrd@uri:port/defaultDB] ")
	constr=sys.stdin.readline()
	ldb=MyObj.mConnect(constr.strip())
	col_name=""
	print(MyObj.getErrMsg())
	print("Database(s) ",ldb)
	# if ldb > 1, then you need to select a database to work with
	# ex MyObj.setDB("Mydb")
	while(True):
		# select an option to do CRUD operations
		print("\n\nSelected database ", MyObj.getDB())
		print("Selected collection ", col_name)
		sys.stdout.write('\nSelect Option \n C to Create Doc\n R to Read Doc(s)\n U to Update Doc\n D to Delete Doc\n F to Find Doc\n\n L to List Collections\n S to Select a Collection\n Q to Quit\n => ')
		selection=sys.stdin.readline().strip()
		if   'Cc'.find(selection) !=-1:
			"(C)reate Doc"
			# Sample docs
			#{'id':'test', 'item': "canvas", 'qty': 100}
			#{'id':'003', 'fname': "Al", 'lname': 'Bundy'}
			#{'id':'test', 'item': "canvas", 'qty': 100, 'tags': ["cotton"], 'size': { 'h': 28, 'w': 35.5, 'uom': "cm" }}

			print("Enter doc in this format {'id':'003', 'fname': 'Al', 'lname': 'Bundy'}  ")
			doc=sys.stdin.readline().strip()
			print(MyObj.createDoc(col_name, ast.literal_eval(doc)))

		elif 'Rr'.find(selection) !=-1:
			"(R)ead Doc(s)"

			docs=MyObj.getColDocs(col_name)
			for d in docs:
				print(d,"\n")

		elif 'Uu'.find(selection) !=-1:
			"UI and testing   (U)pdate doc"
			#{"id":"MZZZZ"},{"$set": {"name":"qZZZZ"}}
			print("Enter filter in this format {'id':''}  ")
			filter = sys.stdin.readline().strip()
			print("Enter set criteria in this format {'$set': {'name':'qZZZZ'}}  ")
			criteria = sys.stdin.readline().strip()
			print("Upsert, True / False ")
			upsertResponse = sys.stdin.readline().strip()
			if len(upsertResponse) < 1:
				upsertParm = True
			else:
				upsertParm = "Tt".find(upsertResponse[0]) !=-1
			filterParm = ast.literal_eval(filter)
			criteriaParm = ast.literal_eval(criteria)
			print(MyObj.updateDoc(col_name, filterParm, criteriaParm, upsertParm))

		elif 'Dd'.find(selection) !=-1:
			"(D)elete Docs"
			print("Enter criteria in this format {'id':''}  ")
			criteria = sys.stdin.readline().strip()
			print(MyObj.delCollDocs(col_name, ast.literal_eval(criteria)))

		elif 'Ff'.find(selection) !=-1:
			"find a doc"
			print ("Enter criteria in this format {'id':''}  ")
			criteria = sys.stdin.readline().strip()
			docs=MyObj.findDoc(col_name, ast.literal_eval(criteria))
			for d in docs:
				print(d,"\n")


		elif 'Ll'.find(selection) !=-1:
			"List Collections"
			l=MyObj.getDBColl()
			for i in range(len(l)):
				print(l[i])

		elif 'Ss'.find(selection) !=-1:
			"Select a collection"
			print("Select a collection name  " )
			col_name = sys.stdin.readline().strip()



		elif 'QqXx'.find(selection) !=-1:
			print ('\n Quiting...... Bye \n')
			break

		else:
			print ('\n INVALID SELECTION \n')



def main():
	#Main menu
	try:
		mainMenu()
	except:
		print(MyObj.getErrMsg())
		print("Oops!",sys.exc_info()[0],"occurred.")




if __name__ == '__main__':
    main()
