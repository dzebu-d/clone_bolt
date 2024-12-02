from driver import Driver
from location import locationCoordinates
def create_driver():
    name = input("enter name: ")
    location = str(locationCoordinates())
    card = input("enter card number: ")
    vehicle_reg= input("enter vehicle reg nr")
    vehicle_class = 2 #place holder 
    user = Driver(name,location,card,vehicle_reg,vehicle_class)
    return user
