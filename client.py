import uuid
class Client:
    def __init__(self,name,location,card,preference):
        self.name = name
        self.location = location
        self.card = card
        self.preference = preference
        self.id = uuid.uuid4()
        self.category = "client"