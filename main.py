from flask import Flask, request, jsonify

from app.models.users import User

app = Flask(__name__)
app.config["DEBUG"] = True

users = []

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
    print(request.get_json(force=True))
   
    return "User successfully added"


app.run()
 
    



