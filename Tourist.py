from Person import Person
class Tourist(Person):
    allTouristsCounter = 0
    allSumOfLuggageToUkraine = 0
    touristToUkraine = 0


    def __init__(self):
        Person.__init__(self)
        self.countryWhereGoing = "default_country"
        self.daysOfTravel = 14
        self.price = 700
        self.countOfThings = 0
        self.weightOfLuggage = 21
        Tourist.allTouristsCounter += 1;


    def __init__(self, country = "Ukraine", weight = 0):
        self.countryWhereGoing = country
        self.daysOfTravel = 14
        self.price = 700
        self.countOfThings = 0
        self.weightOfLuggage = weight
        Tourist.allTouristsCounter += 1
        if country == "Ukraine":
            Tourist.touristToUkraine += 1
            Tourist.allSumOfLuggageToUkraine += weight
