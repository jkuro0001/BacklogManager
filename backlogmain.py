from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import hashlib
#pip install flask flask_sqlalchemy psycopg2

app = Flask(__name__)

#Connection: MAKE SURE TO REPLACE USERNAME:PASSWORD WITH THE ONE SET UP ON YOUR OWN DEVICE
#SSH Tunnel Forward to Local Port: ssh -L 5433:127.0.0.1:5432 USERNAME@128.113.126.87
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USERNAME:1234@127.0.0.1:5433/backlog_manager'

db = SQLAlchemy(app)

#Define basic users table
class Users(db.Model):
    email = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'


#Temporary table
class Preferences(db.model):
    email = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    prefer = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

#Create tables in the database (one-time setup for now)
with app.app_context():
    db.create_all()

#Testing insert to table
#Go to http://127.0.0.1:5000/insert_test_user on browser to activate
@app.route('/insert_test_user', methods=['GET'])
def insert_test_user():
    test_user = Users(email="test@example.com", password_hash="hashedpassword123")
    db.session.add(test_user)
    db.session.commit()
    return "Test user inserted successfully!"


def hash_password(password: str) -> str:
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password: str, stored_hash: str) -> bool:
    """Verifies if the input password matches the stored hash."""
    return hash_password(input_password) == stored_hash


if __name__ == '__main__':
    app.run(debug=False)