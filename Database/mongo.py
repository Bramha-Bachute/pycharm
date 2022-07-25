import pymongo

client = pymongo.MongoClient("mongodb+srv://maharaj:maharaj@cluster0.6kcud2v.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"Bramha",
    "email":"brambachute@gmail.com",
    "surname":"Bachute"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)