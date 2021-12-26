import phonenumbers
from phonenumbers import geocoder
import folium
number=phonenumbers.parse("+919496994276")
location=geocoder.description_for_number(number,"en")
print(location)

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode('49b4d5dbf3ea4d788ac65bf1e0b081c7')
query=str(location)
Result=geocoder.geocode(query)
print(Result)
lat=Result[0]['geometry']['lat']
lng=Result[0]['geometry']['lng']
print(lat,lng)

map=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to((map))
map.save("location.html")