# База даних містить інформацію про абітурієнтів у вигляді:
# прізвище, ім’я абітурієнта, дата народження, навчальний заклад (закінчив), факультет (поступає), спеціальність, середній бал атестату.
# Для заданого факультету обчисліть кількість абітурієнтів, що поступають, а також знайдіть абітурієнта із найнижчим балом.
# В завданні 1 використайте “Об'єктно-орієнтовані бази даних (ZODB)”.

import persistent
from datetime import date

class Entrant(persistent.Persistent):
    def __init__(self):
        self.secondName = "default_name"
        self.firstName = "default_first_name"
        self.birthday = date.min
        self.school = "default_school"
        self.faculty = "default_faculty"
        self.specialty = "default_specialty"
        self.avgPointOfCertificate = "default_mark"




