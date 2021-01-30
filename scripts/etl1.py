# name, gender, age, profession, country, username?, password?

# Load Data into MySQL

import pymysql
from sqlalchemy import create_engine
import pandas as pd
from pymongo import MongoClient

username = 'root'
password = 'root'
end_point = '127.0.0.1'
port = '3306'

connection = pymysql.connect(user=username, passwd=password, host=end_point)
cursor = connection.cursor()
query = ("SHOW FULL PROCESSLIST")
cursor.execute(query)
for item in cursor:
  print(item)

client = MongoClient()
client.db
# engine = create_engine(
#   'mysql+pymysql://{}:{}@{}:{}'.format(
#     username,password,end_point,port)
#   )
# sql = 'SHOW FULL PROCESSLIST;'
# df = pd.read_sql(sql, engine)

# engine.execute("SHOW DATABASES;")

# mycursor.execute("CREATE TABLE users (id INT, name VARCHAR(255), gender VARCHAR(255), age INT, profession VARCHAR(255), country VARCHAR(255))")

# sql = "INSERT INTO users (name, gender, age, profession, country) VALUES (%s, %s, %d, %s, %s)"
# val = [
#   (1, 'Peter', 'Male', 24, 'Actor', 'UK'),
#   (2, 'Amy', 'Female', 19, 'Singer', 'USA'),
#   (3, 'Hannah', 'Female', 30, 'Jornalist', 'USA'),
#   (4, 'Michael', 'Male', 32, 'Jornalist', 'UK'),
#   (5, 'Sunny', 'Male', 22, 'Actor', 'USA'),
#   (6, 'Betty', 'Female', 28, 'Singer', 'UK'),
#   (7, 'Richard', 'Male', 38, 'Actor', 'USA'),
#   (8, 'Susan', 'Female', 33, 'Jornalist', 'UK'),
#   (9, 'Vicky', 'Male', 26, 'Singer', 'USA'),
#   (10, 'Ben', 'Male', 18, 'Singer', 'USA'),
#   (11, 'William', 'Male', 30, 'Jornalist', 'UK'),
#   (12, 'Chuck', 'Male', 21, 'Actor', 'USA'),
#   (13, 'Viola', 'Female', 29, 'Journalist', 'UK')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")



# # Load data into MongoDB
# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["mydatabase"]

# mycol = mydb["users"]

# mylist = [
#   { "id": , "name": "Peter", "gender": "Male", "age":24, "profession": "Actor", "country": "UK"}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
#   { "id": , "name": "", "gender": "", "age": , "profession": "", "country": ""}
# ]

# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)


# #Load data into Neo4j

# # Youtube important playlist


# #------------------------------------------------------------------------------------------------------------------------

# #ETL MySQL ---> MongoDB

# import mysql.connector
# import pymongo
# import datetime

# mgoclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mgodb = mgoclient["projectA"]

# db = mysql.connector.connect(
# 	host="127.0.0.1",
# 	user="root",
# 	passwd="",
# 	database=""
# )


# def migrate(db, mgodb, table, page):
# 	cursor = db.cursor(dictionary=True)
# 	limit = 100
# 	mgocol = mgodb[table]
# 	mgocol.create_index("ID", unique=True)

# 	while True:
# 		offset = (page-1)*limit
# 		page = page + 1

# 		sql = "select * from " +table+ " LIMIT " + str(offset) + "," + str(limit)
# 		cursor.execute(sql)
# 		result = cursor.fetchall()
# 		if (len(result) <= 0):
# 			break

# 		for row in result:
# 			for key in row:
# 				if (isinstance(row[key], datetime.datetime) or isinstance(row[key], datetime.date)):
# 					row[key] = row[key].strftime('%Y-%m-%d %H:%M:%S')

# 			try:
# 				mgocol.insert_one(row)
# 			except:
# 				print("error insert")

# mycursor = db.cursor()
# mycursor.execute("show tables")
# tables = mycursor.fetchall()

# for table in tables:
#   print(table)
#   migrate(db, mgodb, table[0], 1)

# print("Done") 