from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        host="db", 
        database="contacts_db", 
        user="postgres", 
        password="password"
    )
    return conn

# Route for form submission
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']

    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('INSERT INTO contacts (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"message": "Contact submitted!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')

