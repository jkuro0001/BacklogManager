from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#pip install flask flask_sqlalchemy psycopg2

app = Flask(__name__)

#Connection: MAKE SURE TO REPLACE USERNAME:PASSWORD WITH THE ONE SET UP ON YOUR OWN DEVICE
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USERNAME:PASSWORD@localhost:5432/backlogdatabase'

db = SQLAlchemy(app)

#Define basic users table
class Users(db.Model):
    email = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
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

if __name__ == '__main__':
    app.run(debug=False)