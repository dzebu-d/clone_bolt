import uuid
class Driver:
    def __init__(self,name,location,card,vehicle_reg,vehicle_class):
        self.name = name
        self.location = location
        self.card = card
        self.vehicle_reg = vehicle_reg
        self.vehicle_class = vehicle_class
        self.id = uuid.uuid4()
        self.category = "driver"
        
    