import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('http://127.0.0.1:8000/promo/vk/')
 
# check status code for response received
# success code - 200
print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
