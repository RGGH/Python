import json
from ebaysdk.finding import Connection as finding # install with pip
from bs4 import BeautifulSoup # install with pip
from ebayapi import ebayapi # My API key - register for your own
import time

# read search keywords, line by line, from a text file "ebay_search.txt"
def get_kw():
	f = open ("ebay_search.txt", "r")
	lines = f.readlines()
	keywords = lines
	return keywords

def get_items(keywords):
    api = finding(appid = ebayapi, siteid="EBAY-GB", config_file=None) # change country with "siteid="
    api_request = { "keywords": keywords, "outputSelector" : "SellerInfo"}
    response = api.execute("findItemsByKeywords", api_request)
    time.sleep(3)
    soup = BeautifulSoup(response.content, "lxml")
    items = soup.find_all("item")
    for item in items:
         title = item.title.string.lower().strip()
         price = item.currentprice.string
         url = item.viewitemurl.string.lower()
         if item.conditiondisplayname:
            condition = item.conditiondisplayname.string.lower()
         else:
            condition = "n/a"    
         print(title,"\t",condition,"\t",price)

# main driver
if __name__== "__main__":
    get_items(get_kw())
