import sys
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)


from Database import Database

db = Database()
db.connect()
db.setupDB()