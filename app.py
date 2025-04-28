from flask import Flask, request, jsonify

import psycopg2

import os


app = Flask(__name__)


# Database connection function

def get_db_connection():

    conn = psycopg2.connect(

        host="localhost",  # Change this if your database is hosted elsewhere

        database="your_database_name",  # Replace with your database name

        user="your_username",  # Replace with your database username

        password="your_password"  # Replace with your database password

    )

    return conn


# Ensure the uploads directory exists

if not os.path.exists('uploads'):

    os.makedirs('uploads')


@app.route('/save_biodata', methods=['POST'])

def save_biodata():

    # Get form data

    first_name = request.form['firstName']

    last_name = request.form['lastName']

    address = request.form['address']

    dob = request.form['dob']

    gender = request.form['gender']

    hobbies = request.form.getlist('hobbies')  # Get multiple hobbies


    # Handle file upload

    photo = request.files['photo']

    photo_path = os.path.join('uploads', photo.filename)  # Save in uploads directory

    photo.save(photo_path)  # Save the photo


    # Save to database

    conn = get_db_connection()

    cur = conn.cursor()

    cur.execute('INSERT INTO biodata (first_name, last_name, address, dob, gender, hobbies, photo) VALUES (%s, %s, %s, %s, %s, %s, %s)',

                (first_name, last_name, address, dob, gender, ','.join(hobbies), photo_path))

    conn.commit()

    cur.close()

    conn.close()


    return jsonify({'status': 'success'})


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)  # Run the server on all interfaces
