import urllib2
from BeautifulSoup import BeautifulStoneSoup
with open('test_ottawa_honda.html') as file:
    html = file.read()
# used_accords = urllib2.urlopen("https://www.ottawahonda.com/used/Honda-Accord.html").read()
soup = BeautifulStoneSoup(html)

accord_pages = soup.findAll(lambda tag:tag.name =='a' and len(tag.attrs)>1 and 'used' in tag.attrs[0][1])