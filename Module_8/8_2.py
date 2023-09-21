import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metro',
    autocommit=True)

area_code = input("Enter the area code: ")
sql_cmd = f"select type, name from airport where iso_country = '{area_code}' order by type"

cursor = connection.cursor()
cursor.execute(sql_cmd)
name_type = cursor.fetchall()

if len(name_type) == 0:
    print("No result, please check area code.")
else:
    print("Type:\tName:")
    for item in name_type:
        ap_type, ap_name = item
        print(f"{ap_type}\t{ap_name}")  # item[0]: type, item[1]: name
