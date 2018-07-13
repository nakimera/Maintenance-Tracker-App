import os 
from flask import Flask, request, jsonify, make_response
import jwt
import datetime

from app.models.users import User
from app.models.requests import Request

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config["DEBUG"] = True

users_list = []
user_requests = []

@app.route('/unprotected')
def unprotected():
    return ""

@app.route('/protected')
def protected():
    return ""

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    data = request.get_json(force = True)
    username = data.get("username", None)
    password = data.get("password", None)

    for user in users_list:
        if auth and auth.username == "username":
            token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow + datetime.timedelta(minutes=5)}, app.secret_key[os.urandom(12)])
            print(token)
            return jsonify({'token': token})

    return make_response('could not verify', 401, {'www-Authenticate': 'Basic realm="Login Required'})

#users
@app.route('/api/v1/users', methods=['POST', 'GET'])
def users():
    if request.method == 'POST':
        data = request.get_json(force = True)
        username = data.get("username", None)
        password = data.get("password", None)

        if not username:
            return jsonify({'message': 'Please provide a username'}), 400  

        elif not password:
            return jsonify({'message': 'Please provide a password'}), 400    

        else:
            user = User(username, password)
            users_list.append(user)
            return jsonify({
                "message": "User sucessfully created",
                "status": True,
                "data": {
                    "id": user.id,
                    "username": "{}".format(username)
                    }
                }), 201

    if request.method == 'GET':
        usernames = []
        for user in users_list:
            usernames.append(user.username)
        return jsonify({
            "message": "Users successfully retrieved",
            "status": True, 
            "data": "{}".format(usernames)}), 200

@app.route('/api/v1/users/login', methods=['POST'])
def login_user(): 
    if request.method == 'POST':
        data = request.get_json(force = True)
        username = data.get("username", None)
        password = data.get("password", None)
        for user in users_list:
            if user.username == username and user.password == password: 
                
                return jsonify({
                    "message": "{} logged in".format(username),
                    "status": True
                }), 200
            
        return jsonify({
                    "message": "Either username or password is incorrect",
                    "status": False
                }), 404


#user requests
@app.route('/api/v1/users/requests', methods=['POST', 'GET'])
def requests():

    if request.method == 'POST':
        data = request.get_json(force = True)
        requestId = data.get("requestId", None)
        category = data.get("category", None)
        item_name = data.get("item_name", None)
        quantity = data.get("quantity", None)
        description = data.get("description", None)
        
        if not category:
            return jsonify({'message': 'Please fill the category field'}), 400

        elif not item_name:
            return jsonify({'message': 'Please fill the item_name field'}), 400

        elif not quantity:
            return jsonify({'message': 'Please fill the quantity field'}), 400

        elif not description:
            return jsonify({'message': 'Please fill the description field'}), 400

        else:
            prossie = User("naki", "kk")
            user_request = Request(requestId, category, item_name, quantity, description)
            user_requests.append(user_request)
            return jsonify({
                    "message": "Request successfully created",
                    "status": True,
                    "{}".format(prossie.username): {
                        "requestId": "{}".format(requestId),
                        "category": "{}".format(category),
                        "item_name": "{}".format(item_name),
                        "quantity": "{}".format(quantity),
                        "description": "{}".format(description)
                    }
                    }) , 201   

    if request.method == 'GET':

        all_requests = []

        for user_request in user_requests:
            user_request = dict([
                ('requestId', user_request.requestId),
                ('category', user_request.category),
                ('item_name', user_request.item_name),
                ('quantity', user_request.quantity),
                ('description', user_request.description)])
            all_requests.append(user_request)
        
        return jsonify({
            "message": "All requests retrieved",
            "status": True,
            "data": all_requests
        }), 200

#individual request
@app.route('/api/v1/users/requests/<requestId>', methods=['PUT', 'GET'])       
def indiv_request(requestId):
    for user_request in user_requests:
        if user_request.requestId == int(requestId):
            indiv_request = dict([
                    ('requestId', user_request.requestId),
                    ('category', user_request.category),
                    ('item_name', user_request.item_name),
                    ('quantity', user_request.quantity),
                    ('description', user_request.description)])
    
            if request.method == 'GET':    
                return jsonify({
                    "message": "Request successfully retrieved",
                    "status": True,
                    "data": indiv_request
                }), 200
            

            if request.method == 'PUT':
                return "something"

app.run()
 
    



