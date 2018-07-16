import os
from app import create_app

app = create_app(os.environ.get('APP_ENV') or 'development')

if __name__ == "__main__":
    app.run()

#individual request
@app.route('/api/v1/users/requests/<requestId>', methods=['PUT', 'GET'])       
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
            