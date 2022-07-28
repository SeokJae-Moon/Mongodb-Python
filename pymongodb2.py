import os
import sys
from pymongo import MongoClient

def mydbConn():
    client = MongoClient("mongodb://localhost:27017/")
    return client['test-db']

def screen():
    print("\n### 간단한 회원 관리 프로그램 ###")
    print("0.초기생성 1.멤버추가 2.멤버리스트 3.멤버찾기 4. 정보수정 5. 화면지우기 6.종료")


def memberAdd() :
    name = input("->NAME: ")
    email = input("->EMAIL: ")
    age = input("->AGE: ")

    data = {
        'name' : name,
        'email' : email,
        'age' : age
    }
    db = mydbConn()
    db.member.insert_one(data)
    print('{0},{1},{2} insert! '.format(name, email, age))

def memberAllList():
    db = mydbConn()
    print('NAME\tEMAIL\tAGE')
    for member in db['member'].find():
        print('{0}\t{1}\t{2}'.format(member['name'], member['email'], member['age']))
   

def memberSearch():
    name = input("Name you want to find: ")
    db = mydbConn()
    
    print(db.member.find_one({'name':name}))

def memberModify():
    name = input("Name you want to find: ")
    db = mydbConn()

    if db.member.find_one({'name':name}):
        email = input("Email To Edit:  ")
        age = input("Age To Edit:  ")

        db.member.update_one(
            {'name':name },
            {'$set':{'email':email, 'age':age}}
        )
    else:
        print('Member Empty!')

# def memberModify():
#     search_name = input("Name you want to find: ")
#     count = 0

#     db = mydbConn()
#     result = db.member.find({"name" : search_name})
#     for mem in result:
#         print(mem)
#         count += 1
        
#     if (count > 0):
#         new_email = input("Email To Edit:  ")
#         new_age = input("Age To Edit:  ")
        
#         db['member'].update(
#         { 'name':search_name},
#         { "$set":{'email': new_email, 'age' : new_age }} )  
#     else:
#         print('Member Empty')

def createNodeInit():
    data1 = {
        'name' : 'GuSeoYeun', 'email' : 'gu@gmail.com', 'age' : '24'
    }
    data2 = {
        'name' : 'Jang', 'email' : 'jang@kw.ac.kr', 'age' : '21'
    }    
    db = mydbConn()
    db.member.insert_many( [data1, data2] )
    print("초기 데이터 추가되었음.")
    
if __name__ == '__main__' :
    while True:
        screen()
        choice = input("-> ")

        if choice == '0':
           createNodeInit()
        elif choice == '1':
            memberAdd()
        elif choice == '2':
            memberAllList()
        elif choice == '3':
            memberSearch()
        elif choice == '4':
            memberModify()
        elif choice == "5" :
            os.system("cls")
        elif choice == '6':
            sys.exit(1)

# db.collection.findAndModify({
#         query:<document>,
#         sort:<document>,
#         remove:<boolean>,
#         update:<document>,
#         new:<boolean>,
#         fields:<document>,
#         upsert:<boolean>,
#         bypassDocumentValidation:<boolean>,
#         writeConcern:<document>,
#         collation:<document>
# });
