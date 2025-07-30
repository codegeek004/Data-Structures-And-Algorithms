dict1 = {
        "brand":"honda",
        "model":"city",
        "Price":900,
        "toBuy":True,
        "Mileage":12.42
        }
#prints dictionary
print(dict1)

#prints a value of dict
print(dict1["brand"])
print(dict1.get("model"))

#access all the keys
print(dict1.keys())

#access all the values
print(dict1.values())

#access all the instances of the dictionary
print(dict1.items())

for i, j in dict1.items():
    print('{key: ',i, 'value: ', j, '}')

#change value of a key
dict1['Mileage'] = 45
print(dict1.items())

#update method to change value
dict1.update({"year":300})
print(dict1['year'])
print()

#add key value pairs
dict1['color'] = 'red'
dict1['origin'] = 'india'
print(dict1.items())
print()

#this will also add items
dict1.update({"wheels":"alloy_wheels"})
print(dict1.items())
print()

#delete items
dict1.pop('origin')
print(dict1.items())
print()

del dict1['toBuy']
print(dict1.items())
print()

#deletes last item
dict1.popitem()
print(dict1.items())
print()

#empties the dictionary
dict1.clear()
print(dict1)
