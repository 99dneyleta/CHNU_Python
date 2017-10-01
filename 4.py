from datetime import date
class Person:
    def __init__(self):
        self.name = "default_name"
        self.surname = "default_surname"
        self.middleName = "default_middleName"
        self.birthday = date.min

    def printFullAges(self):
        print(date.today().year - self.birthday.year)

class Tourist(Person):
    def __init__(self):
        self.countryWhereGoing = "default_country"
        self.daysOfTravel = 14
        self.price = 700
        self.countOfThings = 0
        self.weightOfLuggage = 21

countryWhereGoing = "Ukraine"
sumOfLuggageWeight = 0
count = 0
allTourists = []

for i in range(5):
    allTourists.append(Tourist())
    allTourists[i].weightOfLuggage += i

allTourists[0].countryWhereGoing = "USA"
allTourists[1].countryWhereGoing = "Ukraine"
allTourists[2].countryWhereGoing = "Thailand"
allTourists[3].countryWhereGoing = "Canada"
allTourists[4].countryWhereGoing = "Ukraine"



for tourist in allTourists:
    if tourist.countryWhereGoing == countryWhereGoing:
        count += 1;
        sumOfLuggageWeight += tourist.weightOfLuggage

print('To {} travelling {} peoples avg weight of luggage = {} kg' .format(countryWhereGoing, count, sumOfLuggageWeight/count))





