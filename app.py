from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Function to create a MySQL connection
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='jophin@69',
        database='car_rental_system'
    )

# Route to fetch customers from the database
@app.route('/fetch_customers')
def fetch_customers():
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM Customers')
        customers = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('fetchcustomers.html', customers=customers)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to fetch cars from the database
@app.route('/fetch_cars')
def fetch_cars():
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM Cars')
        cars = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('fetchcars.html', cars=cars)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
 

# Add more routes for fetching Owners, Locations, Reservations, etc.

if __name__ == '__main__':
    app.run(debug=True)
