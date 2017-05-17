import requests

url = 'http://www.autotrader.ca/cars/honda/accord/on/ottawa/?prx=100&prv=Ontario&loc=Ottawa%2c+ON&sts=New-Used&hprc=True&wcp=True&inMarket=basicSearch'
req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
response = req.text
with open('listing.html', 'w') as file:
    file.write(response)


