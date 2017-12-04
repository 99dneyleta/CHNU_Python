import persistent
# База даних містить інформацію про абітурієнтів у вигляді:
# прізвище, ім’я абітурієнта, дата народження, навчальний заклад (закінчив), факультет (поступає), спеціальність, середній бал атестату.
# Для заданого факультету обчисліть кількість абітурієнтів, що поступають, а також знайдіть абітурієнта із найнижчим балом.
# В завданні 1 використайте “Об'єктно-орієнтовані бази даних (ZODB)”.
from datetime import date


class Entrant(persistent.Persistent):

    def __init__(self, name, birtday, school, faculty, specialty, avgMark):
        self.name = str(name)
        self.birthday = birtday
        self.school = str(school)
        self.faculty = str(faculty)
        self.specialty = str(specialty)
        self.avgMark = float(avgMark)

        @staticmethod
        def getCountOfEntrant(facultyName, entrants):
            count = 0
            for i in entrants:
                if i.faculty == facultyName:
                    count += 1
            return count

        @staticmethod
        def get_Entrant_With_Lowest_Mark(entrants):
            studentWithLowestMark = entrants[0]
            for i in entrants:
                if i.avgMark < studentWithLowestMark.avgMark:
                    studentWithLowestMark = i
            return studentWithLowestMark
