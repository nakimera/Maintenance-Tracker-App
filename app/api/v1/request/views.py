import random
from flask import (Blueprint, jsonify, request)
from app.api.v1.request.requests import Request

mod =  Blueprint('request', __name__) 

requestIds = []
user_requests = []

@mod.route('/', methods=['POST', 'GET'])
def requests():
    if request.method == 'POST':
        data = request.get_json(force = True)
        requestId = generate_requestId()
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
            user_request = Request(requestId, category, item_name, quantity, description)
            user_requests.append(user_request)
            return jsonify({
                    "message": "Request successfully created",
                    "status": True,
                    "data": {
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

#generate requestId function
def generate_requestId():
    requestId = random.randint(1,1000)
    if requestId in requestIds:
        requestId = random.randint(1,1000)
        requestIds.append(requestId)
    return requestId

# convert request to dictionary function
def convert_req_to_dict(user_request):
    if not user_request:
        return {}
    
    return dict([
            ('requestId', user_request.requestId),
            ('category', user_request.category),
            ('item_name', user_request.item_name),
            ('quantity', user_request.quantity),
            ('description', user_request.description)])


# get request by requestId func
def get_request_by_requestId(requestId):
    for user_request in user_requests:

        if user_request.requestId == int(requestId):
            return user_request
    return None

# get request by requestId func
def get_request_by_requestId(requestId):
    for user_request in user_requests:

        if user_request.requestId == int(requestId):
            return user_request
    return None
            

#individual request
@mod.route('/<requestId>', methods=['PUT', 'GET'])       
def indiv_request(requestId): 
    one_request = get_request_by_requestId(requestId) 

    if not one_request:
        return jsonify({
            "message" : "Request not found",
            "status": False}), 203

    if request.method == 'GET':  
        return jsonify({
            "message": "Request successfully retrieved",
            "status": True,
            "data": convert_req_to_dict(one_request)
            }), 200

    if request.method == 'PUT':
        data = request.get_json(force = True)

    for key, value in data.items():
        if key == "item_name":
            one_request.name = value
        elif key  == "category":
            one_request.category = value
        elif key  == "quantity":
            one_request.quantity = value
        elif key  == "description":
            one_request.description = value
        
    return jsonify({
            "message": "Request successfully updated",
            "status": True,
            "data": convert_req_to_dict(one_request)
            }), 200
            