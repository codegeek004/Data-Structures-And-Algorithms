dict1 = {
        "brand":"honda",
        "model":"city",
        "Price":900,
        "toBuy":True,
        "Mileage":12.42
        }
#prints all the keys
for i in dict1:
    print(i)

print()

#prints all the values
for i in dict1:
    print(dict1[i])

print()

for i,j in dict1.items():
    print(i, ':', j)


#copy dictionary
dict2 = dict1.copy()
print(dict2)



