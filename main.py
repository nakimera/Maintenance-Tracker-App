import os 

from flask import Flask, request, jsonify, session

from app.models.users import User
from app.models.requests import Request

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config["DEBUG"] = True

users = []
logged_in_user = None

def get_loggedin_user():
    for user in users:
        if user.username == session['username']:
            return user

@app.route('/', methods=['GET'])
def home():
    return "<h1>Maintenance Tracker</h1><p>Hello, World</p>"

@app.route('/users', methods=['GET'])
def get_users():
    usernames = []
    for user in users:
        usernames.append(user.username)

    return jsonify(usernames)

@app.route('/signup', methods=['POST'])
def signup_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 
        user = User(username,password)
        users.append(user)
        return "User successfully added"

@app.route('/login', methods=['POST'])
def login_user(): 
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 
        for user in users:
            if user.username == username and user.password == password:
                session['username'] = user.username
                return user.username + " logged in" 
            else:
                return 'Either username or password is incorrect'
            
@app.route('/users/requests', methods=['POST', 'GET'])
def create_request():
    if request.method == 'POST':
        category = request.form['category']
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        description = request.form['description']
        user_request = Request(category, item_name, quantity, description)
        user = get_loggedin_user() 
        return "Request successfully created"



app.run()
 
    



