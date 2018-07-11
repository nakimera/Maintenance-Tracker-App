import uuid
from .requests import Request

my_requests = []

class User(object):
    def __init__(self, username, password):
        self.id = str(uuid.uuid1())
        self.username = username
        self.password = password

    def add_request(self, user_request):  
        self.user_request = user_request      
        my_requests.append(user_request)




    def get_requests(self):
        for user_request in my_requests:
            all_requests = []
            user_request = dict([
                ('category', user_request.category),
                ('item_name', user_request.item_name),
                ('quantity', user_request.quantity),
                ('description', user_request.description)])
            all_requests.append(user_request)
        return my_requests
        