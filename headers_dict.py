def get_headers(s):
    d = dict()
    sep=":"
    for kv in s.split('\n'):
        kv = kv.strip()

        if sep in kv:
            k = kv.split(sep)[0].strip()
            if k == 'user-agent':
                v = kv.split(sep)[1]
            else:
                v = ":".join(kv.split(sep)[:]).split()[1] # so 'referer' works

            # exclude cookie from headers if using for Scrapy
            if k.lower() == 'cookie':
                continue 
            d[k] = v
    return d

s = '''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cookie: wp-settings-time-1=1605181340; wp-settings-1=libraryContent%3Dbrowse%26mfold%3Do%26editor%3Dtinymce
referer: https://redandgreen.co.uk/webscraping-archive/
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'''

headers = (get_headers(s))
print(headers)

import requests
res = requests.get("https://redandgreen.co.uk/webscraping-archive/")
print(res)
