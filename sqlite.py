import sqlite3

class Sqlite:
    def __init__(self, dbName):
        self.dbName = dbName
        self.tablesNameList = []
        self.Connection = sqlite3.connect(dbName)
        self.Cursor = self.Connection.cursor()

    def closeDB(self):
        self.Connection.close()
    # rows must be dictionary with type and value
    def createTable(self, tableName, rows):
        values = ''
        for row in rows:
            values += row.type + ' ' + row.value + ', '
        self.Cursor.execute('''CREATE TABLE''' + str(tableName) + values)
        self.tablesNameList.append(tableName)

    def insertIntoTable(self, tableName, values, lineParametrsCount):
         # if this table Name was created
         parametrs = '?,'*lineParametrsCount
         if(self.tablesNameList.Consist(tableName, values)):
             self.Cursor.executemany('INSERT INTO' + tableName + 'VALUES ()' + parametrs, values)

    def commit(self):
        self.Connection.commit()

#     add select with parametrs


