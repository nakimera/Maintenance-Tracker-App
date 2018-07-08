from .requests import Request

class User(object):

    requests = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_request(Request):          
        requests.append(Request)
        return "Request successfully created"