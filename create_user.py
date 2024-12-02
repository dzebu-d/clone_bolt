from client import Client
from database_worker import *
from location import locationCoordinates
def create_client():
    name = input("enter name: ")
    location = str(locationCoordinates())
    card = input("enter card number: ")
    preference = input("select ur preferred level (1-4)")
    user = Client(name,location,card,preference)
    return user

