from Tourist import Tourist

allTourists = []

for i in range(3):
    allTourists.append(Tourist("Ukraine", i + 10))

allTourists.append(Tourist("USA", 12))

print('To {} travelling {} peoples avg weight of luggage = {} kg' .format("Ukraine", Tourist.touristToUkraine,
                                                                          Tourist.allSumOfLuggageToUkraine/Tourist.touristToUkraine))




