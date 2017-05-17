import requests
from bs4 import BeautifulSoup
import json

from requests.models import Request

list = ''
read = False
with open('listing.html') as file:
    for line in file.readlines():
        # print line
        if 'var dataLayer = [' in line:
            read = True
            continue
        if '];' in line:
            break
        if read == True:
            list += line


json = json.loads(list.replace("'",'"'))

urls = []
url_template = 'http://wwwb.autotrader.ca/a/Honda/Accord/Ottawa/Ontario/5_{0}_{1}'
for vehicle in json['lists'][0]['vehicles']:
    add_id = vehicle[u'adID'].replace('5-','')
    dealer_id = vehicle[u'dealerID'].replace('5-','')
    url = str.format(url_template, add_id, dealer_id)
    urls.append(url)

print (urls[0])

# req = requests.get(urls[0], headers={'User-Agent': 'Mozilla/5.0'})
# soup = BeautifulSoup(req.text)

with open('sample_accord.html','r') as f:
    content = f.read()

soup = BeautifulSoup(content)
# for value in soup.findall('div',{'class':'at_value at_col'}):
#     print (value)

spec_list_div = soup.findAll('div',{'class':'specList'})[0]
for div in spec_list_div.findAll('div',{'class':'at_row'}):
    # print (div)
    title_div  = div.find('div',{'class':'at_title at_col '})[0]
    print (title_div.find('span')[0].string)