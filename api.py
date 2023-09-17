from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify
from models import *
from utils.database_utils import *


app = Flask(__name__)

app.config['SECRET_KEY'] = 'generated-secrete-key'
app.config["SQLALCHEMY_DATABASE_URI"] = instance

db.init_app(app)

create_db()
create_tables(app=app)
seeds(app=app)

@app.route('/')
def hello_geek():
    return '<h2>Hello from Flask & Docker</h2>'

@app.route('/test')
def testing_jenkins():
    return '<h2>Testing Jenkins!!</h2>'

@app.route('/jenkinstest')
def testing_api():
    return '<h2>Jenkins API!!</h2>'

@app.route("/time")
def get_current_time():
    data:list[User] = db.session.query(User).all()
    users = [row.as_dict() for row in data]
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0")