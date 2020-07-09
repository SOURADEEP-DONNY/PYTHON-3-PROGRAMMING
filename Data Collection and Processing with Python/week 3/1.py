import requests
import json
page=requests.get("https://www.google.com")
print(type(page))
print(page.text[:15000])
print(page.url)

print('\n\n')
print('--------------------------------------------------------------------')
