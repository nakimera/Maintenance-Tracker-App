from flask import (Blueprint, jsonify, request)
from app.models.users import User

mod =  Blueprint('auth', __name__) 

users_list = []

@mod.route('/login', methods=['POST'])
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

@mod.route('/', methods=['POST', 'GET'])
def users():
    if request.method == 'POST':
        data = request.get_json(force=True)
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
            "data": usernames
            })