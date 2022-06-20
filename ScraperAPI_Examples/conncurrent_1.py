''' YouTube Demo '''
import os 
import concurrent.futures
import urllib.request

from urllib.error import HTTPError

from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method


api_key= os.environ.get('apikey')
# print(api_key)

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(_url, timeout):
    ''' https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor-example '''
    with urllib.request.urlopen(_url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except HTTPError as e:
            print(f"\n{url} generated an exception - Forbidden! : {e}")
        else:
            print(f"page {url} is {len(data)} bytes")
