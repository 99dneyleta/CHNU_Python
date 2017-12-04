# База даних містить інформацію про абітурієнтів у вигляді:
# прізвище, ім’я абітурієнта, дата народження, навчальний заклад (закінчив), факультет (поступає), спеціальність, середній бал атестату.
# Для заданого факультету обчисліть кількість абітурієнтів, що поступають, а також знайдіть абітурієнта із найнижчим балом.
# В завданні 1 використайте “Об'єктно-орієнтовані бази даних (ZODB)”.

from ZODB import FileStorage, DB
from Entrant import Entrant
from datetime import datetime
import transaction

storage = FileStorage.FileStorage('mydata.fs')
db = DB(storage)
connection = db.open()
root = connection.root
facultyNameFilter = "Applied Math"

if not root.entrants:
    root.entrants = {}

    size = int(input('Set count of entrants...'))
    for i in range(size):
        entrant = Entrant(
            input("Type entrant name"),
            datetime(int(input("Set Year")),int(input("Set Month")), int(input("Set Day"))),
            input("Type ended school"),
            input("Type chosen faculty"),
            input("Type specialty"),
            input("Type avgMark")
        )

transaction.commit()
print(root.entrants.keys())
print("On faculty Applied Math want to learn" + Entrant.getCountOfEntrant(facultyNameFilter, list(root.entrants.values())))
connection.close()