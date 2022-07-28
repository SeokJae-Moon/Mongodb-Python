from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['test-db']

#print(client.list_database_names())

# data = {
#     'author' : 'moon',
#     'text' : 'mongoDB is first',
#     'tags' : ['kwangwoon', 'python', 'pymongo']
# }

# dbInsert = db.posts.insert_one(data)
# print('몽고디비입력완료')

# for d in db['posts'].find():
#     print(d['author'], d['text'], d['tags'])

# print()
# print(db.posts.find_one({'author':'moon'})['text'])

# print()
for d in db['posts'].find({}, {'test':0}):
    print(d)
