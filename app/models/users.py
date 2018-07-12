import uuid
import jwt

from .requests import Request

my_requests = []

class User(object):
    def __init__(self, username, password):
        self.id = int(uuid.uuid1())
        self.username = username
        self.password = password



    def add_request(self, user_request):  
        self.user_request = user_request      
        my_requests.append(user_request)




        