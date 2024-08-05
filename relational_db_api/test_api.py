import requests

# curl -X POST -H "Content-Type: application/json" -d """{ "playlist": [{"id": "d6416719-d5ad-44f9-ba72-7a922865bc3b"}, {"id": "5f3c97c1-cc14-4429-8e62-c586106ea7d3"}]}""" http://127.0.0.1:5000/search/playlist

# Replace this with your actual API URL
api_url = "http://127.0.0.1:5001/get/songs"

# Replace this with the data you want to send
data = { "song_ids": 
            [
                {"id": "d6416719-d5ad-44f9-ba72-7a922865bc3b"}, 
                {"id": "5f3c97c1-cc14-4429-8e62-c586106ea7d3"}
            ]
        }

# Make the POST request
response = requests.post(api_url, json=data)

# Print the status code and response content
print("Status Code:", response.status_code)
print("Response Content:", response.json())
