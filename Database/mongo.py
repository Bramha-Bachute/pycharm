import pymongo

client = pymongo.MongoClient("mongodb+srv://maharaj:maharaj@cluster0.6kcud2v.mongodb.net/?retryWrites=true&w=majority")
db = client.test

"""d = [{
    "name":"Bramha",
    "email":"brambachute@gmail.com",
    "surname":"Bachute",
    "Subject" : ['Python', 'Pandas', 'SQL']
},{
    "name":"Pulse",
    "email":"pulsebachute@gmail.com",
    "surname":"Bachute",
    "Subject" : ['Python', 'Pandas', 'SQL']
},{
    "name":"Yog",
    "email":"yogbachute@gmail.com",
    "surname":"Bachute",
    "Subject" : ['Python', 'Pandas', 'SQL']
}]"""

data = {
  "users": [
    {
      "userId": 1,
      "firstName": "Krish",
      "lastName": "Lee",
      "phoneNumber": "123456",
      "emailAddress": "krish.lee@learningcontainer.com"
    },
    {
      "userId": 2,
      "firstName": "racks",
      "lastName": "jacson",
      "phoneNumber": "123456",
      "emailAddress": "racks.jacson@learningcontainer.com"
    },
    {
      "userId": 3,
      "firstName": "denial",
      "lastName": "roast",
      "phoneNumber": "33333333",
      "emailAddress": "denial.roast@learningcontainer.com"
    },
    {
      "userId": 4,
      "firstName": "devid",
      "lastName": "neo",
      "phoneNumber": "222222222",
      "emailAddress": "devid.neo@learningcontainer.com"
    },
    {
      "userId": 5,
      "firstName": "jone",
      "lastName": "mac",
      "phoneNumber": "111111111",
      "emailAddress": "jone.mac@learningcontainer.com"
    }
  ]
}

db1 = client['mongotest']
coll = db1['Emp']
#coll.insert_one(data)

r = coll.find({"firstName":"devid"}) #Tp find specific record

#To find the record where name start with letter E or Higher

for i in r:
    print(i)