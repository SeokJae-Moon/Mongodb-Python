from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['test-db']

# data = {
#      'author' : 'lee',
#      'text' : 'Who are you?',
#  }
# dpInsert = db.posts.insert_one(data)

db['posts'].update_one(
     {'author':'lee', 'text':'Who are you?' },
     {'$set':{'author':'Lee', 'address':'Busan' }}
)
