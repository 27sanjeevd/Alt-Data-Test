import requests

# Replace 'latitude' and 'longitude' with the latitude and longitude of the location you want to get light data for
latitude = '38.989697'
longitude = '-76.937759'

# Construct the API endpoint URL
url = 'https://api.sunrise-sunset.org/json?lat=' + latitude + '&lng=' + longitude

# Make the API request and get the response
response = requests.get(url)
response_json = response.json()

# Print the light data for the specified location
print('Sunrise: {}'.format(response_json['results']['sunrise']))
print('Sunset: {}'.format(response_json['results']['sunset']))