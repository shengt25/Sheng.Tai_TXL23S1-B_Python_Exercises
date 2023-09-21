from geopy.distance import geodesic
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metro',
    autocommit=True)

ident1 = input("Enter the ICAO codes of first airport: ")
ident2 = input("Enter the ICAO codes of second airport: ")
sql_cmd1 = f"select name, latitude_deg, longitude_deg from airport where ident = '{ident1}'"
sql_cmd2 = f"select name, latitude_deg, longitude_deg from airport where ident = '{ident2}'"

cursor = connection.cursor()
cursor.execute(sql_cmd1)
result = cursor.fetchall()[0]
airport_name1, *coord1 = result

cursor.execute(sql_cmd2)
result = cursor.fetchall()[0]
airport_name2, *coord2 = result

dist = geodesic(coord1, coord2).km
print(f"The distance between {airport_name1} and {airport_name2} is: {dist} km")
