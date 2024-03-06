from flask import Flask, jsonify, redirect, render_template, request
import mysql.connector

app = Flask(__name__)


# Connect to your MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jophin@69",
    database="car_rental_system"

)

# Create a cursor object
cursor = conn.cursor()

# Create cars table
create_cars_table = """
CREATE TABLE IF NOT EXISTS cars (
    VIN varchar(20) PRIMARY KEY,
    Model varchar(50),
    Car_type varchar(50),
    Colour varchar(20),
    OwnerName varchar(50)
)
"""
cursor.execute(create_cars_table)

# Create customers table
create_customers_table = """
CREATE TABLE IF NOT EXISTS customers (
    Cid int AUTO_INCREMENT PRIMARY KEY,
    Cname varchar(50),
    Phone varchar(20),
    Mobile varchar(20),
    Address varchar(100)
)
"""
cursor.execute(create_customers_table)

# Create locations table
create_locations_table = """
CREATE TABLE IF NOT EXISTS locations (
    Loc_id int AUTO_INCREMENT PRIMARY KEY,
    Address varchar(100)
)
"""
cursor.execute(create_locations_table)

# Create owners table
create_owners_table = """
CREATE TABLE IF NOT EXISTS owners (
    Oname varchar(50) PRIMARY KEY,
    Address varchar(100)
)
"""
cursor.execute(create_owners_table)

# Create picks_from table
create_picks_from_table = """
CREATE TABLE IF NOT EXISTS picks_from (
    Pickup_id int AUTO_INCREMENT PRIMARY KEY,
    Res_num int,
    Loc_id int
)
"""
cursor.execute(create_picks_from_table)

create_reservation_table="""
CREATE TABLE IF NOT EXISTS reservations (
    Res_num INT AUTO_INCREMENT PRIMARY KEY,
    Res_date DATE,
    Cid INT,
    VIN VARCHAR(20),
    Loc_id INT
)
"""
cursor.execute(create_reservation_table)

# Commit changes and close connection
conn.commit()
conn.close()

 
@app.route('/')
def home():
   return render_template('index.html')
def fetch_cars():
    try:
        conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jophin@69",
    database="car_rental_system"
)
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM cars')
        cars = cursor.fetchall()
        cursor.close()
        conn.close()
        return cars
    except Exception as e:
        print(f"An error occurred while fetching cars: {str(e)}")
        return []

# Route to view cars table
@app.route('/view_cars')
def view_cars():
    cars = fetch_cars()
    return render_template('viewcars.html', cars=cars) 

def fetch_customers():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jophin@69",
            database="car_rental_system"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM customers')
        customers = cursor.fetchall()
        cursor.close()
        conn.close()
        return customers
    except Exception as e:
        print(f"An error occurred while fetching customers: {str(e)}")
        return []

# Route to view customers table
@app.route('/view_customers')
def view_customers():
    customers = fetch_customers()
    return render_template('view_customers.html', customers=customers)

# Function to fetch locations
def fetch_locations():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jophin@69",
            database="car_rental_system"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM locations')
        locations = cursor.fetchall()
        cursor.close()
        conn.close()
        return locations
    except Exception as e:
        print(f"An error occurred while fetching locations: {str(e)}")
        return []

# Function to fetch owners
def fetch_owners():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jophin@69",
            database="car_rental_system"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM owners')
        owners = cursor.fetchall()
        cursor.close()
        conn.close()
        return owners
    except Exception as e:
        print(f"An error occurred while fetching owners: {str(e)}")
        return []
# Function to fetch pickups
def fetch_pickups():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jophin@69",
            database="car_rental_system"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM picks_from')
        pickups = cursor.fetchall()
        cursor.close()
        conn.close()
        return pickups
    except Exception as e:
        print(f"An error occurred while fetching pickups: {str(e)}")
        return []

def fetch_reservations():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jophin@69",
            database="car_rental_system"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM reservations')
        reservations = cursor.fetchall()
        cursor.close()
        conn.close()
        return reservations
    except Exception as e:
        print(f"An error occurred while fetching reservations: {str(e)}")
        return []

# Route to view reservations
@app.route('/view_reservations')
def view_reservations():
    reservations = fetch_reservations()
    return render_template('view_reservations.html', reservations=reservations)


# Route to view pickups
@app.route('/view_pickups')
def view_pickups():
    pickups = fetch_pickups()
    return render_template('view_pickups.html', pickups=pickups)


# Route to view locations
@app.route('/view_locations')
def view_locations():
    locations = fetch_locations()
    return render_template('view_locations.html', locations=locations)

# Route to view owners
@app.route('/view_owners')
def view_owners():
    owners = fetch_owners()
    return render_template('view_owners.html', owners=owners)




@app.route('/insert_cars', methods=['GET', 'POST'])
def insert_cars():
    if request.method == 'POST':
        vin = request.form.get('vin')
        model = request.form.get('model')
        car_type = request.form.get('car_type')
        colour = request.form.get('colour')
        owner_name = request.form.get('owner_name')
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="jophin@69",
                database="car_rental_system"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cars (VIN, Model, Car_type, Colour, OwnerName) VALUES (%s, %s, %s, %s, %s)", (vin, model, car_type, colour, owner_name))
            conn.commit()
            conn.close()
            return redirect('/view_cars')
        except Exception as e:
            print(f"An error occurred while inserting car: {str(e)}")
    
    return render_template('insert_cars.html')


@app.route('/insert_customers', methods=['GET', 'POST'])
def insert_customers():
    if request.method == 'POST':
        cname = request.form.get('cname')
        phone = request.form.get('phone')
        mobile = request.form.get('mobile')
        address = request.form.get('address')
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="jophin@69",
                database="car_rental_system"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO customers (Cname, Phone, Mobile, Address) VALUES (%s, %s, %s, %s)", (cname, phone, mobile, address))
            conn.commit()
            conn.close()
            return redirect('/view_customers')
        except Exception as e:
            print(f"An error occurred while inserting customer: {str(e)}")
    
    return render_template('insert_customers.html')


# Route for inserting locations
@app.route('/insert_locations', methods=['GET', 'POST'])
def insert_locations():
    if request.method == 'POST':
        address = request.form.get('address')
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="jophin@69",
                database="car_rental_system"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO locations (Address) VALUES (%s)", (address,))
            conn.commit()
            conn.close()
            return redirect('/view_locations')
        except Exception as e:
            print(f"An error occurred while inserting location: {str(e)}")
    
    return render_template('insert_locations.html')

# Route for inserting owners
@app.route('/insert_owners', methods=['GET', 'POST'])
def insert_owners():
    if request.method == 'POST':
        oname = request.form.get('oname')
        address = request.form.get('address')
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="jophin@69",
                database="car_rental_system"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO owners (Oname, Address) VALUES (%s, %s)", (oname, address))
            conn.commit()
            conn.close()
            return redirect('/view_owners')
        except Exception as e:
            print(f"An error occurred while inserting owner: {str(e)}")
    
    return render_template('insert_owners.html')

# Route for inserting reservations
@app.route('/insert_reservations', methods=['GET', 'POST'])
def insert_reservations():
    if request.method == 'POST':
        res_date = request.form.get('res_date')
        cid = request.form.get('cid')
        vin = request.form.get('vin')
        loc_id = request.form.get('loc_id')
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="jophin@69",
                database="car_rental_system"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO reservations (Res_date, Cid, VIN, Loc_id) VALUES (%s, %s, %s, %s)", (res_date, cid, vin, loc_id))
            conn.commit()
            conn.close()
            return redirect('/view_reservations')
        except Exception as e:
            print(f"An error occurred while inserting reservation: {str(e)}")
    
    return render_template('insert_reservations.html')
@app.route('/book_cars', methods=['GET', 'POST'])
def book_cars():
    if request.method == 'POST':
        res_date = request.form.get('res_date')
        cid = request.form.get('cid')
        vin = request.form.get('vin')
        loc_id = request.form.get('loc_id')
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="jophin@69",
                database="car_rental_system"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO reservations (Res_date, Cid, VIN, Loc_id) VALUES (%s, %s, %s, %s)", (res_date, cid, vin, loc_id))
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"An error occurred while booking car: {str(e)}")
    
    # Fetch available cars and locations to display in the form
    cars = fetch_cars()
    locations = fetch_locations()
    
    return render_template('book_cars.html', cars=cars, locations=locations)



if __name__ == '__main__':
    app.run(debug=True)
    
