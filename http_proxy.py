import requests
class HTTPRequest(object):
    def save_page(self, url, filename):
        req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = req.text
        with open(filename, 'w') as file:
            file.write(response)