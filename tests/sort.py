array = ["Snehashish", "Aauguest", "August", "trevor", "ishan"]
array.sort()
print(array)

data = {
    "students": {
        "attributes": [
            "name",
            "age",
            "email",
            "grades"
        ],
        "2022-10-09 11:28:21.875568": {
            "name": "Snehashish Laskar",
            "age": 15,
            "email": "snehashish.laskar@gmail.com",
            "grades": []
        },
        "2022-10-09 11:28:30.020252": {
            "name": "Snehashish Laskar",
            "age": 15,
            "email": "snehashish.laskar@gmail.com",
            "grades": []
        }
    }
}

by = 'name'
list = []
for i in data['students']:
    if i != "attributes":
        list.append(data['students'][i][by])

list.sort()
data2 = {
    'students':{
        "attributes": [
            "name",
            "age",
            "email",
            "grades"
        ],
    }
}

for i in list:
    for j in data2['students']:
        if j != "attributes":
            print(j)