#GENERATING A URL FOR WHAT WE WANT

import requests
d={'q':'Mohun Bagan','tbm':'isch'}    #'tbm':'isch'--- for tabs with images.
results=requests.get('https://www.google.com/search',params=d)
print(results.url)
print(results.text)



# 'isch' IS FOR IMAGE SEARCH.
# 'params' IS PASSING THE PARAMETER DICTIONARY.

dict1={'q':'Cristiano Ronaldo','tbm':'isch'}
results=requests.get('https://www.google.com/search',params=dict1)
print(results.url)
print(results.text)


dict2={'q':'Leonel Messi','tbm':'isch'}
results=requests.get('https://www.google.com/search',params=dict2)
print(results.url)
print(results.text)


