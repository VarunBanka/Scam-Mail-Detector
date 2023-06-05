import requests

# URL of the Flask application
url = 'http://localhost:5000/main'

# Email to classify
email = 'get-free-$100-bitcoin-by-clicking-here'

# Send POST request
response = requests.post(url, data={'email': email})

# Get the response content
result = response.text

# Print the result
print(result)
