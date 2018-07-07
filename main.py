from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

requests = [
    {'id': 0,
    'category': 'Repair',
    'item_name': 'Laptop',
    'quantity': 2,
    'description': 'All 2 computers cannot power on'},
    {'id': 1,
    'category': 'Maintenance',
    'item_name': 'Iphone',
    'quantity': 1,
    'description': 'Update operating system'},
    {'id': 3,
    'category': 'Maintenance',
    'item_name': 'Macbook',
    'quantity': 1,
    'description': 'Update operating system'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Maintenance Tracker</h1><p>Hello, World</p>"


@app.route('/api/v1/resources/users/requests', methods=['GET'])
def api_all():
    return jsonify(requests)

@app.route('/api/v1/resources/users/requests/<requestId>', methods=['GET'])
def api_id():
    if 'id' in request.args:                                           
        id = int(request.args['id'])                                   
    else:                                                              
        return "Error: No id provided. Please specify an ID"

    results = []

    for request in requests:
        if request['id'] == id:
            results.append(request)

    return jsonify(results)

"""@app.route('/api/v1/resources/users/requests', methods=['POST'])

@app.route('/api/v1/resources/users/requests/<requestId>', methods=['PUT'])"""

app.run()