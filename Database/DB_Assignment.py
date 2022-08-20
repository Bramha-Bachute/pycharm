import datetime
import pandas as pd
import mysql.connector as connection
from openpyxl import load_workbook

conn = connection.connect(host='localhost', user='root', password='Deva@321#', database='Assignment')

cursor = conn.cursor()

# Q1. Create database for table attribute dataset and dress dataset

#cursor.execute('create database Assignment')   """Data Base created"""

#Create table

'''
#cursor.execute("Create table Attributes (Dress_ID int,	Style varchar(100),	Price varchar(100),	Rating int,	Size char(10), Season varchar(100),	NeckLine varchar(100), SleeveLength varchar(100), waiseline varchar(100), Material varchar(100), FabricType varchar(100), Decoration varchar(100), Pattern_Type varchar(100), Recommendation int)")

'''

#Q2. DO bulk upload for these two tables
'''Insert Data Query for bulk data upload

insert into Attributes values(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13])

wb = load_workbook("D:\IT Study\Bramha\Data Science\Pandas\drive-download-20220729T133108Z-001\Attribute DataSet.xlsx")

ws = wb['Sheet1']

"""Insert Bulk data"""
for i in ws.values:
    cursor.execute(f"""insert into Attributes values({i[0]},"{i[1]}","{i[2]}",{i[3]},"{i[4]}","{i[5]}","{i[6]}","{i[7]}","{i[8]}","{i[9]}","{i[10]}","{i[11]}","{i[12]}",{i[13]})""")
    conn.commit()

"""Create table dress with date as column name"""
Directly cannot create table with date so using underscore created columns
create table dress (Dress_ID int, _29082013 int, _31082013 int, _02092013 int, _04092013 int, _06092013 int, _08092013 int, _10092013 int, _12092013 int, _14092013 int, _16092013 int, _18092013 int, _20092013 int, _22092013 int, _24092013 int, _26092013 int, _28092013 int, _30092013 int, _10022013 int, _10042013 int, _10062013 int, _10082010 int, _10102013 int, _10122013 int)

for i in ws.values:
   cursor.execute(f"""Insert into dress values({int(i[0])},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]},{i[10]},{i[11]},{i[12]},{i[13]}),{i[14]},{i[15]},{i[16]},{i[17]},{i[18]},{i[19]},{i[20]},{i[21]},{i[22]},{i[23]}""")
   conn.commit()------Not worked
'''
#Q3. read datasets as dataframe
'''
cursor.execute("Select * from Attributes")
df1 = pd.DataFrame(cursor)
'''
#print(df1)

cursor.execute("Select * from dress")

df2 = pd.DataFrame(cursor)

#print(df2)

#Q4. Convert Attribute dataset in json format

#df = pd.read_excel("D:\IT Study\Bramha\Data Science\Pandas\drive-download-20220729T133108Z-001\Attribute DataSet.xlsx")

#df.fillna(value="Blank")

df2.fillna(value="Blank")

json_data = df2.to_json()

import json

#Convert json data to dict
mydict = json.loads(json_data)

print(type(mydict))

#Q5. store this data set in the mango db

import pymongo

client = pymongo.MongoClient("mongodb+srv://maharaj:maharaj@cluster0.6kcud2v.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db = client['Assignment']
coll = db['dress']

#coll.insert_one(mydict)

#Q6. In SQL Try to perform left join operation with attibutes and dress datasets on dress_id

#Left Join QUery

#select * from attributes a left join dress d on a.Dress_id = d.Dress_id

#cursor.execute("""select * from attributes a left join dress d on a.Dress_id = d.Dress_id""")

#for i in cursor:
    #print(i)

#Q7. Write a SQL query to find out how many unique dress that we have based on dress id

# cursor.execute("""select count(distinct dress_id) from attributes""")
#
# for i in cursor:
#     print(i)


#Q8 try to find out how many dress is having recommendation 0

#cursor.execute("""select count(distinct dress_id) from attributes where Recommendation=0""")

#Q9. Try to find out total dress sell for individual id

#cursor.execute("""select dress_id, sum(_29082013 + _31082013 + _02092013 + _04092013 + _06092013 + _08092013 + _10092013 + _12092013 + _14092013 + _16092013 + _18092013 + _20092013 + _22092013 + _24092013 + _26092013 + _28092013 + _30092013 + _10022013 + _10042013 + _10062013 + _10082010 + _10102013 + _10122013) Total_Sell from dress group by dress_id""")

#Q.10 Try to find Third highest most selling dress id
'''
cursor.execute("""select max(Total_sell) from (select dress_id, sum(_29082013 + _31082013 + _02092013 + _04092013 + _06092013 + _08092013 + _10092013 + _12092013 + _14092013 + _16092013 + _18092013 + _20092013 + _22092013 + _24092013 + _26092013 + _28092013 + _30092013 + _10022013 + _10042013 + _10062013 + _10082010 + _10102013 + _10122013) Total_Sell from dress group by dress_id) Total_dress_Sell where Total_sell<(select max(Total_sell) from (select dress_id, sum(_29082013 + _31082013 + _02092013 + _04092013 + _06092013 + _08092013 + _10092013 + _12092013 + _14092013 + _16092013 + _18092013 + _20092013 + _22092013 + _24092013 + _26092013 + _28092013 + _30092013 + _10022013 + _10042013 + _10062013 + _10082010 + _10102013 + _10122013) Total_Sell from dress group by dress_id) Total_dress_Sell where Total_sell<(select max(Total_sell) from (select dress_id, sum(_29082013 + _31082013 + _02092013 + _04092013 + _06092013 + _08092013 + _10092013 + _12092013 + _14092013 + _16092013 + _18092013 + _20092013 + _22092013 + _24092013 + _26092013 + _28092013 + _30092013 + _10022013 + _10042013 + _10062013 + _10082010 + _10102013 + _10122013) Total_Sell from dress group by dress_id) Total_dress_Sell))""")

for i in cursor:
    print(i)

'''

#same result can be produced by using below query also

cursor.execute("""select * from (select dress_id, sum(_29082013 + _31082013 + _02092013 + _04092013 + _06092013 + _08092013 + _10092013 + _12092013 + _14092013 + _16092013 + _18092013 + _20092013 + _22092013 + _24092013 + _26092013 + _28092013 + _30092013 + _10022013 + _10042013 + _10062013 + _10082010 + _10102013 + _10122013) Total_Sell from dress group by dress_id) Total_dress_Sell order by Total_sell desc limit 1 offset 2""")