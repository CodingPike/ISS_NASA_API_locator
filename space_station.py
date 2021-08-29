#!/usr/bin/env python
# coding: utf-8

import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from translate import Translator

def ISSLocator():
    url = 'http://api.open-notify.org/iss-now'
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
    else:
        return f'Something went wrong! Response status code = {response.status_code}.'
    longitude = response['iss_position']['longitude']
    longitude = float(longitude)
    latitude = response['iss_position']['latitude']
    latitude = float(latitude)
    coordinates = latitude, longitude
    coordinates_str = f'{latitude}, {longitude}'
    my_latitude= input('\nType in ur latitude\n')
    my_longitude = input('\nType in ur longitude\n')
    my_latitude = float(my_latitude)
    my_longitude = float(my_longitude)
    my_location = my_latitude, my_longitude
    my_location_str = f'{my_latitude}, {my_longitude}'
    geolocator = Nominatim(user_agent="my_application")
    location = geolocator.reverse(my_location_str)
    distance = int(geodesic(my_location, coordinates).kilometers)
    try:
        geolocator = Nominatim(user_agent="my_application_1")
        location_iss = geolocator.reverse(coordinates_str)
        translator= Translator(to_lang="pl")
        translation = translator.translate(location_iss.address)
        return f'Ur estimated address : {location.address}. ISS estimated location: {translation}. ISS is around {distance} km away from ur current location!'
    except:
        return f"Ur estimated address : {location.address}. ISS is currently above an ocean or a sea so we can't provide an actual address. ISS is around {distance} km away from ur current location!"


ISSLocator()
