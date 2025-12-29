# assignment 1
from flask import Flask


app = Flask(__name__)
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number)):
        if number % i == 0:
            return False
    return True
@app.route('/prime_number/<int:number>')
def prime_number(number):
    response = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return response
app.run(host='127.0.0.1', port=5000, debug=True)

# assignment 2
from flask import Flask
import mysql.connector

connection = mysql.connector.connect(
        host="localhost",
        user="soder1",
        password="soderfests1234",
        database="flight_game",
        autocommit=True
)
def airport1(icao):
    sql = "SELECT ident, name, municipality FROM airport where ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result

app = Flask(__name__)
@app.route('/airport/<string:icao>')
def airport(icao):
    airport_data = airport1(icao)
    response = {
        "ICAO": airport_data[0],
        "Name": airport_data[1],
        "Location": airport_data[2]
    }
    return response
app.run(host='127.0.0.1', port=5000, debug=True)