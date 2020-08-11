import requests
import mypgeocode

api_key="a7d0ed68a5f3f24591d5f7754d6c8734"
#lat=32.7157
#lon=117.1611

def detect_zip(zip):

    nomi = mypgeocode.Nominatim('us')
    latlon = nomi.query_postal_code(zip)
    print ("latlon: ", latlon)

    lat = latlon.latitude
    lon = latlon.longitude
    city = latlon.place_name

    print ("latitude: ", lat)
    print ("longitude: ", lon)


    url="http://api.openweathermap.org/data/2.5/uvi?appid={}&lat={}&lon={}".format(api_key,lat,lon)

    result = requests.get(url)

    #value of uv index for today at noon
    print(result)
    print(result.json()['value'])
    uv = result.json()['value']
    date = result.json()['date_iso']

    return (str(uv), city)
