
class Request(object):
    def __init__(self, requestId, category, item_name, quantity, description):
        self.requestId = int(requestId)
        self.category = category
        self.item_name = item_name
        self.quantity = int(quantity)
        self.description = description
        