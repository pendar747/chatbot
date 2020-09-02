import mysql.connector as mysql

class Database(object):

    db = None
    dbName = 'chatbot'

    def connect(self):
        self.db = mysql.connect(
            user="root",
            passwd="chatbot",
            host="127.0.0.1",
            database="chatbot",
            auth_plugin='mysql_native_password'
        )

    def databaseExists(self, dbName):
        cursor = self.db.cursor()

        cursor.execute("SHOW DATABASES")

        databases = cursor.fetchall()

        for db in databases:
            if db[0] == dbName:
                return True
        return False
    
    def tableExists(self, tableName):
        cursor = self.db.cursor()
        cursor.execute('SHOW TABLES')
        tables = cursor.fetchall()

        for table in tables:
            if table[0] == tableName:
                return True
        return False
        
        
    def createDB(self):
        cursor = self.db.cursor()
        cursor.execute(f"CREATE DATABASE {self.dbName}")
    
    def createActivitiesTable(self):
        cursor = self.db.cursor()
        cursor.execute('CREATE TABLE chatbot.activity ( name VARCHAR(500) NOT NULL , duration INT NOT NULL , id INT NOT NULL AUTO_INCREMENT , PRIMARY KEY (id)) ENGINE = InnoDB;')
        
    def setupDB(self):
        if not self.databaseExists(self.dbName):
            self.createDB()

        if not self.tableExists('activity'):
            self.createActivitiesTable()

    def insertActivity(self, activityName, duration):
        cursor = self.db.cursor()
        query = 'INSERT INTO activity (name, duration) VALUES (%s, %s)'
        values = (activityName, duration)
        cursor.execute(query, values)
        self.db.commit()
            
