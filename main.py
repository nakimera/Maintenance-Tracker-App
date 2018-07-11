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

@app.route('/signup', methods=['POST'])
def signup_user():
    if request.method == 'POST':
        data = request.get_json(force = True)
        username = data.get("username", None)
        password = data.get("password", None)
        user = User(username, password)
        users.append(user)
        return jsonify({
            "message": "User sucessfully created",
            "status": True,
            "data": {
                "id": user.id,
                "username": "{}".format(username)
                }
            }), 201

        # else:
        #     return {"message": "User account already exists",
        #     "status": False,
        #     "data": {"id": user.id,
        #     "username": user.username,
        #     "password": user.password}
        #     }, 200

@app.route('/users', methods=['GET'])
def get_users():
    usernames = []
    for user in users:
        usernames.append(user.username)
    return jsonify({
        "message": "Users successfully retrieved",
        "status": True, 
        "data": "{}".format(usernames)}), 200

@app.route('/login', methods=['POST'])
def login_user(): 
    if request.method == 'POST':
        data = request.get_json(force = True)
        username = data.get("username", None)
        password = data.get("password", None)
        for user in users:
            if user.username == username and user.password == password:
                session['username'] = user.username
                return jsonify({
                    "message": "{} logged in".format(username),
                    "status": True
                }), 200
            
        return jsonify({
                    "message": "Either username or password is incorrect",
                    "status": False
                }), 404

def get_loggedin_user():
        for user in users:
            if user.username == session['username']:
                return user

@app.route('/users/requests', methods=['POST', 'GET'])
def requests():
    if request.method == 'POST':
        data = request.get_json(force = True)
        user = logged_in_user
        category = data.get("category", None)
        item_name = data.get("item_name", None)
        quantity = data.get("quantity", None)
        description = data.get("description", None)
        user_request = Request(category, item_name, quantity, description)
        user.add_request(user_request)
        return jsonify({
                "message": "Request successfully created",
                "status": True
                })    

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
 
    



