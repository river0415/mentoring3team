import csv
import sqlite3
r=open('동물병원_utf8.csv', encoding='utf-8')
data=csv.reader(r)
header=next(data)
address=[]
num=[]
for rr in data :
    address.append(rr[2])
    num.append(int(rr[0]))
for i in range(len(address)):
    a = address[i].split(' ')
    address[i] = " ".join(a[0:4])

####### 도로명주소 위도 경도 값으로 바꿔주기 ########
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')
# 위도, 경도 반환하는 함수
def geocoding(address):
    geo = geo_local.geocode(address)
    x_y = [geo.latitude, geo.longitude]
    return x_y

#####주소를 위,경도 값으로 변환하기 #####
latitude = []
longitude =[]

for i in address:
    latitude.append(geocoding(i)[0])
    longitude.append(geocoding(i)[1])

conn = sqlite3.connect('C:/Users/river/PycharmProjects/mentoring3team/mentoring3team.db', isolation_level=None)

c = conn.cursor()

sqlite_update_query = """Update hospital set latitude = ?, longitude = ? where num = ?"""
for i in range(len(address)):
    columnValue = (latitude[i], longitude[i], num[i])
    c.execute(sqlite_update_query, columnValue)

conn.close()
r.close()