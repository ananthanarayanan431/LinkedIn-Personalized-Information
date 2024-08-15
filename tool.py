

import requests
import openai
import http.client
import json, re 
import os

from constant import SERPER_API_KEY

os.environ['SERPER_API_KEY']=SERPER_API_KEY

NUM_TOP_URLS_SCRAPED=10

def get_social_profile_url(name,company,platform, platform_url_pattern):
    top_results = []
    query = f"{name} {company} {platform}"
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
            "q": query
    })
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = data.decode("utf-8")
    response_dict = json.loads(response)
    top_results.append(response_dict["organic"][:NUM_TOP_URLS_SCRAPED])
    top_urls = [result['link'] for result in top_results[0]]
    regex = re.compile(fr'{platform_url_pattern}')
    for url in top_urls:
        if regex.match(url):
            return url
    return None