import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metro',
    autocommit=True)

icao = input("Enter the ICAO: ")
sql_cmd = f"select name, municipality from airport where ident = '{icao}'"

cursor = connection.cursor()
cursor.execute(sql_cmd)
name, location = cursor.fetchall()[0]

print(f"Name: {name}\nLocation: {location}")
