import pymongo

client = pymongo.MongoClient("mongodb+srv://Suraj:Suraj143@cluster0.8qp0yum.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"suraj",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "shetage"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )