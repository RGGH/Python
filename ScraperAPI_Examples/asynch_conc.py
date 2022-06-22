''' YouTube Demo - uses a pool of threads to execute calls asynchronously '''

import concurrent.futures
import urllib.request
import socket
from urllib.error import HTTPError

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
            if e.code == 403:
                print(f"generated an exception: {url, e}")
        except socket.error as e:
            print (f"Error creating socket: {e}")
        else:
            print(f"{url} page is  {len(data)} bytes")
