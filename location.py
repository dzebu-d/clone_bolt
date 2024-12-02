
import requests



def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io/?token=0d9efacd76837f')
        
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
        #return lat, long
    except:
        #Displaying ther error message
        
        #closing the program 
        exit()
        return "Could not fetch location"
