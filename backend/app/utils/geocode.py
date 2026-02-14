from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="hunger_pins")

def get_lat_lng(address: str):
    location = geolocator.geocode(address)

    if not location:
        return None, None

    return location.latitude, location.longitude
