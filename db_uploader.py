import csv
import sqlite3
r=open('동물병원_utf8.csv', encoding='utf-8')
data=csv.reader(r)
header=next(data)
list=[]
for rr in data :
    num = rr[0]
    name = rr[1]
    address = rr[2]
    tel = rr[3]
    list.append(rr[:4])
r.close()

conn = sqlite3.connect('C:/Users/river/PycharmProjects/mentoring3team/mentoring3team.db', isolation_level=None)

c = conn.cursor()

c.executemany("INSERT INTO hospital(num, name, address, tel) VALUES (?,?,?,?)", list)

conn.close()