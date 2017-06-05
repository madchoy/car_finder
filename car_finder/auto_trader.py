import re
from enum import Enum

import requests
from bs4 import BeautifulSoup
import json

from decimal import Decimal
from requests.models import Request

# list = ''
# read = False
#
# json = json.loads(list.replace("'",'"'))
#
# urls = []
# url_template = 'http://wwwb.autotrader.ca/a/Honda/Accord/Ottawa/Ontario/5_{0}_{1}'
# for vehicle in json['lists'][0]['vehicles']:
#     add_id = vehicle[u'adID'].replace('5-','')
#     dealer_id = vehicle[u'dealerID'].replace('5-','')
#     url = str.format(url_template, add_id, dealer_id)
#     urls.append(url)
#
# print (urls[0])
#
# # req = requests.get(urls[0], headers={'User-Agent': 'Mozilla/5.0'})
# # soup = BeautifulSoup(req.text)
#
# with open('sample_accord.html','r') as f:
#     content = f.read()
#
# soup = BeautifulSoup(content)
# # for value in soup.findall('div',{'class':'at_value at_col'}):
# #     print (value)
#
# interesting_fields = ['Kilometres', 'Style/Trim','Body Type','Engine','Transmission','Exterior Colour']
#
# spec_list_div = soup.findAll('div',{'class':'specList'})[0]
# for div in spec_list_div.findAll('div',{'class':'at_row'}):
#     # print (div)
#     with open('listing.html') as file:
#         for line in file.readlines():
#             # print line
#             if 'var dataLayer = [' in line:
#                 read = True
#                 continue
#             if '];' in line:
#                 break
#             if read == True:
#                 list += line
#     title_div  = div.findAll('div',{'class':'at_title at_col '})[0]
#     title = (title_div.findAll('span')[0].string)
#     if title in interesting_fields:
#         value_div = div.findAll('div', {'class':'at_value at_col'})[0]
#         print (value_div.string)
#
# from bs4 import BeautifulSoup
# import json
#
# list = ''
# read = False
# with open('listing.html') as file:
#     for line in file.readlines():
#         # print line
#         if 'var dataLayer = [' in line:
#             read = True
#             continue
#         if '];' in line:
#             break
#         if read == True:
#             list += line
from car_finder.car import Car

def scrape_decimal_from_string(value):
    string_number = re.sub("[^0-9]", "", value)
    return Decimal(string_number)
class CarFields(object):
    class CarField(object):
        _fields = {}
        def __init__(self, attribute_name, field_name, convert = None):
            self.__attribute_name = attribute_name
            self.__field_name = field_name
            self.__convert = convert
            self._fields[self.__attribute_name]=self

        @property
        def field_name(self):
            return self.__field_name

        def convert(self, value):
            if self.__convert:
                return self.__convert(value)
            else:
                return value

    KILOMETRES = CarField('Kilometres', 'kilometers', convert = scrape_decimal_from_string)
    STYLE_TRIM = CarField('Style/Trim', 'trim')
    BODY_TYPE = CarField('Body Type', 'type')
    ENGINE = CarField('Engine', 'engine')
    TRANSMISSION = CarField('Transmission', 'transmission')
    EXTERIOR_COLOUR = CarField('Exterior Colour', 'colour')

    __car_fields = CarField._fields
    del CarField._fields

    @classmethod
    def get_car_field(cls, attribute_name):
        try:
            return cls.__car_fields[attribute_name]
        except KeyError:
            pass
        return None

class AutoTrader(object):
    def parse_car(self, car_file):
        car = Car()
        soup = BeautifulSoup(car_file)
        current_price_string = (soup.findAll('div',{'class':'currentPrice'})[0].text)
        price = Decimal((current_price_string.replace('Current Price','').replace(',','').replace('$','').strip()))
        print (price)
        car.selling_price = price
        spec_list_div = soup.findAll('div', {'class': 'specList'})[0]
        for div in spec_list_div.findAll('div', {'class': 'at_row'}):
            title_div = div.findAll('div', {'class': 'at_title at_col '})[0]
            title = (title_div.findAll('span')[0].string)
            car_field = CarFields.get_car_field(title)
            if car_field:
                value_div = div.findAll('div', {'class': 'at_value at_col'})[0]
                setattr(car, car_field.field_name, car_field.convert(value_div.string))

        return car
