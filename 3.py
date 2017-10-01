data = {'Ivanov':{'paper':10}}
f = open('input','r')
inputData = f.readlines()

for line in inputData:
    owner = line.split(' ', 1)[0]
    productName = line.split(' ', 2)[1]
    count = int(line.split(' ', 2)[2])
    if owner in data:
        try:
            data[owner][productName] += count
        except KeyError:
            data[owner][productName] = count
    else:
        data[owner] = {productName:count}


data['Aloha'] = {'book':22}
sorted_data = sorted(data.keys())
result = {}

for key in sorted_data:
    print(key + ':')
    values = sorted(data[key].keys())
    rezVal = {}
    for value in values:
        rezVal[value] = data[key][value]
        print(value + ' '+ str(data[key][value]))
    result[key] = rezVal