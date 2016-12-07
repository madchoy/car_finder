import urllib2
import requests
from BeautifulSoup import BeautifulStoneSoup
with open('test_ottawa_honda.html') as file:
    html = file.read()
# used_accords = urllib2.urlopen("https://www.ottawahonda.com/used/Honda-Accord.html").read()
soup = BeautifulStoneSoup(html)

accord_hrefs = soup.findAll(lambda tag:tag.name =='a' and len(tag.attrs)>1 and 'used' in tag.attrs[0][1])
print accord_hrefs
bleh = [href.attrs[0][1] for href in accord_hrefs]
print len(bleh)
unique_hrefs = set(bleh)
print len(unique_hrefs)
# accord_href = accord_hrefs[0]
# href = accord_href.attrs[0][1]
# page_html = requests.get(href).text
# inner_page = BeautifulStoneSoup(page_html)

def span_id_text(page, id):
    return page.findAll('span',{'id':id})[0].text


for accord_href in list(unique_hrefs)[0:2]:
    page_html = requests.get(accord_href).text
    inner_page = BeautifulStoneSoup(page_html)
    print span_id_text(inner_page, 'specsPrice')
    print span_id_text(inner_page, 'specsStock')
    print span_id_text(inner_page, 'specsStock')
    print span_id_text(inner_page, 'specsExtColor')
    print span_id_text(inner_page, 'specsIntColor')
    print span_id_text(inner_page, 'specsModel')
    print span_id_text(inner_page, 'specsCylinders')
    print span_id_text(inner_page, 'specsTransmission')