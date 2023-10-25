from flask import Flask
import json
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metro',
    autocommit=True)

cursor = connection.cursor()
app = Flask(__name__)


# Route for get_info_by_icao
@app.route("/<icao>")
def route_get_info_by_icao(icao):
    sql_cmd = f"select name, municipality from airport where ident = '{icao}'"
    cursor.execute(sql_cmd)
    try:
        name, location = cursor.fetchall()[0]
    except:
        result = {"ICAO": icao, "message": "Invalid ICAO code."}
        return json.dumps(result), 400
    else:
        result = {"ICAO": icao, "Name": name, "Location": location}
        return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=False)
