from bson.objectid import ObjectId
from pymongo import MongoClient
import datetime

cluster = "mongodb+srv://benjamin:1234@cluster0.ymasxal.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(cluster)

print(client.list_database_names())

db = client.test
print(db.list_collection_names())

todo1 = {"name": "Ben", "text": "My first todo!", "status": "open",
         "tags": ["python", "coding"], "date": datetime.datetime.utcnow()}

todos = db.todos

# insert one item
# result = todos.insert_one(todo1)

todo2 = [{"name": "Chris", "text": "My second todo!", "status": "open",
          "tags": ["python", "coding"], "date": datetime.datetime.utcnow()}, {"name": "Charles", "text": "My second todo!", "status": "open",
                                                                              "tags": ["c++", "coding"], "date": datetime.datetime.utcnow()}]

# insert many item
# result = todos.insert_many(todo2)

# query
result1 = todos.find_one({"name": "Ben"})

# query
result2 = todos.find_one({"_id": ObjectId("63c77ce5d3003b4208bc7e6f")})

# query
result3 = todos.find({"tags": "python"})

# more than one item in the result
# for result in result3:
#     print(result)

# another alternative in list
# print(list(result3))

# for deleting one item
# result = todos.delete_one({"_id": ObjectId("63c77ce5d3003b4208bc7e6f")})

# for deleting many item
# result = todos.delete_one({"name": "Chris"})

# for updating
# result = todos.update_one({"tags": "c++"}, {"$set": {"status": "done"}})
