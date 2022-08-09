import pymongo
client = pymongo.MongoClient("mongodb+srv://akhilm4907:pandarun@cluster0.onqehwd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "akhil" ,
    "email": "akhil4907@gmail.com",
    "surname" : "mohan"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)