from datetime import date, timedelta
class Person:
    def __init__(self):
        self.name = "default_name"
        self.surname = "default_surname"
        self.middleName = "default_middleName"
        self.birthday = date.min

    def printFullAge(self):
        print(date.min - (date.today() - self.birthday - timedelta(366))).year