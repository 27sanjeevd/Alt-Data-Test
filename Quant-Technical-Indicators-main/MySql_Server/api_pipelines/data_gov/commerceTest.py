import requests

api_key = "api-key"

base_url = "https://api.commerce.gov/api/news?api_key="

# Set any additional query parameters you want to include in the request
params = {
    "page": 1,
    "per_page": 1
}

# Make the request to the API
response = requests.get(base_url, params=params, headers={"x-api-key": api_key})

# Print the response status code to check if the request was successful
print(response.status_code)

# If the request was successful, print the data returned by the API
if response.status_code == 200:
    data = response.json()
    data = data.get("data")

    for x in range(10):
        if x < len(data):
            print(str(data[x].get("self")) + " " + str(data[x].get("tags")) + " " + str(data[x].get("news_type")))




