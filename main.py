import os 

from flask import Flask, request, jsonify, session

from app.models.users import User
from app.models.requests import Request

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config["DEBUG"] = True

users = []
user_requests = []
logged_in_user = None

@app.route('/', methods=['GET'])
def home():
    return "<h1>Maintenance Tracker</h1><p>Hello, World</p>"

@app.route('/signup', methods=['POST'])
def signup_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 
        user = User(username,password)
        users.append(user)
        return "User successfully added"

@app.route('/users', methods=['GET'])
def get_users():
    usernames = []
    for user in users:
        usernames.append(user.username)
    return jsonify(usernames)

def get_loggedin_user():
        for user in users:
            if user.username == session['username']:
                return user

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
def requests():
    if request.method == 'POST':
        category = request.form['category']
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        description = request.form['description']
        user_request = Request(category, item_name, quantity, description)
        user_requests.append(user_request)
        return "Request successfully created"

    if request.method == 'GET':
        requests_list = [] 
        for user_request in user_requests:
            user_request = dict([('category', user_request.category),
            ('item_name', user_request.item_name),
            ('quantity', user_request.quantity),
            ('description', user_request.description)])
            requests_list.append(user_request)

        return jsonify(requests_list)

app.run()
 
    



