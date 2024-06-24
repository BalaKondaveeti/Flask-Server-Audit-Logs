import requests

# URL for the API endpoint
url = "http://ec2-34-228-167-143.compute-1.amazonaws.com:5000/events"

# Example data to send in a POST request
data_to_send = {
    "data":{"name": "Sample Event",
    "location": "Virtual",
    "date": "2024-04-16"}
}

# Making a POST request
response_post = requests.post(url, json=data_to_send)
print("Response from POST request:")
print(response_post.status_code)
print(response_post.json())

# Making a GET request
response_get = requests.get(url)
print("\nResponse from GET request:")
print(response_get.status_code)
print(response_get.json())
