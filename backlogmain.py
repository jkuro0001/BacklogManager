from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import hashlib
#pip install flask flask_sqlalchemy psycopg2 flask_cors

app = Flask(__name__)
CORS(app)

#Connection: MAKE SURE TO REPLACE USERNAME:PASSWORD WITH THE ONE SET UP ON YOUR OWN DEVICE
#SSH Tunnel Forward to Local Port: ssh -L 5433:127.0.0.1:5432 USERNAME@128.113.126.87
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://knighk4:1234@localhost/backlog_manager'

db = SQLAlchemy(app)

#Define basic users table
class Users(db.Model):
    email = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'


#Temporary table
class Preferences(db.Model):
    email = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    prefer = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

#Create tables in the database (one-time setup for now)
with app.app_context():
    db.create_all()

#Allow requests from frontend
CORS(app, resources={r"/*": {"origins": "http://128.113.126.87:3000"}})

#API route to register a new user: http://127.0.0.1:5000/register

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    print(data)
    existing_user = Users.query.filter((Users.email == data['email'])).first()
    if existing_user:
        return jsonify({"error": "User already exists!"}), 400

    new_user = Users(email=data['email'], name=data['name'], password_hash=hash_password(data['password']))
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully!"}), 201


def hash_password(password: str) -> str:
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password: str, stored_hash: str) -> bool:
    """Verifies if the input password matches the stored hash."""
    return hash_password(input_password) == stored_hash


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
