import requests

# Replace example.com with the URL of the webpage you want to retrieve the contents of
url = "https://www.youtube.com/"

response = requests.get(url)

# Retrieve the contents of the webpage
webpage_contents = response.text

print(webpage_contents)
