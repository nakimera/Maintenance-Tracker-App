import uuid

class User(object):
    def __init__(self, username, password):
        self.id = int(uuid.uuid1())
        self.username = username
        self.password = password





        