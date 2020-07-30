"""
Use a webproxy to access web data behind a firewall
if the following code doesn't work:

    import pandas as pd
    df = pd.read_csv(url)

WARNING: Never put your credentials into code files!
Instead use a .proxies-file in USERPROFILE
with the following contents:

{'http': 'http://user:pass@webproxy.com',
 'https': 'https://user:pass@webproxy.com'}

Your credentials will then be used to provide access to the csv.
"""

import io
import json
import os
import requests


def proxify(url: str):
    """
    usage: df = pd.read_csv(proxify(url))
    """
    
    try:
        # read the proxy settings
        with open(os.environ['USERPROFILE'] + '\\.proxies') as f:
            proxies = json.load(f)

    except FileNotFoundError:
        # probably we don't need a proxy?
        return url
        
        
    # get data using the proxy
    r = requests.get(url, proxies=proxies, verify=False)
    
    # make text string behave like a file
    return io.StringIO(r.text)
