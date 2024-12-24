from flask import Flask, request, jsonify, render_template
import sqlite3
from passlib.hash import bcrypt

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect("phishing_simulation.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def login_page():
    return render_template("login.html")  # Make sure login.html exists in the templates/ folder

@app.route("/capture", methods=["POST"])
def capture_credentials():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Save to database with hashed password
    hashed_password = bcrypt.hash(password)
    conn = sqlite3.connect("phishing_simulation.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO responses (email, password) VALUES (?, ?)", (email, hashed_password))
    conn.commit()
    conn.close()

    return jsonify({"message": "Captured successfully"}), 200

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
