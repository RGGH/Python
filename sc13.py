# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

''' API example using JsonRequest '''

import scrapy
from scrapy.crawler import CrawlerProcess
import copy
import json
import warnings
from scrapy.http.request.json_request import JsonRequest
from pprint import pprint

class sc13(scrapy.Spider):
    name = 'sc13'
    custom_settings = {'FEEDS':{'results1.csv':{'format':'csv'}}}
    start_urls = ['https://fakerapi.it/api/v1/']

    def parse(self, response):
        
        payload = {'_quantity': "2"}
        
        yield JsonRequest(url='https://fakerapi.it/api/v1/persons', 
            data=payload, method='GET')
            
        pprint(response.text)          

# main driver
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(sc13)
    process.start()
