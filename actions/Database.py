import mysql.connector as mysql


class Database(object):

    def connect(self):
        db = mysql.connect(
            user="root",
            passwd="chatbot",
            host="127.0.0.1",
            database="chatbot",
            auth_plugin='mysql_native_password'
        )
        print(db)
