import geocoder

try:
    coordinates = geocoder.ip('me').latlng
except:
    coordinates = []