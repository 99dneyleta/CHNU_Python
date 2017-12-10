import sqlite

tableName = 'Entrant'
faculty = 'Math'
allEntrantFromFacultyQuery = 'SELECT * FROM ' + tableName + ' WHERE faculty=(?)'
studentWithTheLowestMark = 'SELECT * FROM ' + tableName + ' WHERE avg_mark = (SELECT min(avg_mark) FROM ' + tableName + ')'

entrantTable = {'name': 'str', 'birthday': 'str', 'school': 'str', 'faculty': 'str', 'specialty': 'str', 'avg_mark': 'float'}
data = [('Petro', '12-2-1996', '121', 'Math', 'Programmer', 5),
        ('Petro', '12-12-1996', '13', 'Applied Math', 'Programmer', 3),
        ('Petro', '12-7-1996', '45', 'Applied Math', 'testing', 2),
       ]

DB = sqlite.Sqlite('DB.sqlite3')
#DB.createTable(tableName, entrantTable)
#DB.insertIntoTable('Entrant', data)

DB.select(allEntrantFromFacultyQuery,faculty)
print(DB.Cursor.fetchall().__len__())

DB.Cursor.execute(studentWithTheLowestMark)
print(DB.Cursor.fetchone())

DB.close()
