import subprocess


def install():
    print("Installing the fuzz")
    subprocess.call(["pip", "install", "thefuzz", "yelp", "requests"])


install()

import json
import urllib.parse
import urllib.request
from thefuzz import fuzz
import requests


import sys


def write_output(output):
    with open("output.json", "w") as output_file:
        output_file.write(json.dumps(output))


def process_company(company):
    result = send_api_request(company["name"])
    with open("data.json", "a+") as f:
        f.write('{"name": "' + company["name"] + '", "result": ')
        f.write(json.dumps(result))
        f.write("},")
    google_score = get_google_score(company["name"], result) if result else 0
    print(google_score)
    return {"name": company["name"], "rating": google_score}


def process(filename):
    pre_data = urllib.request.urlopen("https://raw.githubusercontent.com/saltpay/oxfordhack-minichallenge/master/input-alt.json").read()
    data = json.loads(pre_data)
    output = list(map(process_company, data[:]))
    write_output(output)


def get_google_score(name, response):
    name_similarity = fuzz.token_sort_ratio(name, response["result"]["name"])
    return 1 if name_similarity > 90 else 0


def send_api_request(name):
    api_key = "AIzaSyBTYI_bAtT6TP__w7OLFqxnydfFBBF9un8"
    query = name
    service_url = "https://kgsearch.googleapis.com/v1/entities:search"
    params = {
        "query": query,
        "limit": 1,
        "indent": True,
        "key": api_key,
    }
    url = service_url + "?" + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read())

    return response["itemListElement"][0] if response["itemListElement"] else {}


def yelp_scrapper():
    MY_API_KEY = "xgtN0hq4WTZcd_42NJXze7vNbVsHOVxyf38ibF-RWHj9Y6zOwWbNMagWyfyXmJeCGupWtE1XWG6zTz-NLRvQ6qGveO3GSYW4DAMk31XkXmP4reMYU757Z9tj4vUaYnYx "

    headers = {"Authorization": "Bearer %s" % MY_API_KEY}
    url = "https://api.yelp.com/v3/businesses/search"

    # In the dictionary, term can take values like food, cafes or businesses like McDonalds
    params = {"term": "seafood", "location": "New York City"}

    req = requests.get(url, params=params, headers=headers)

    # proceed only if the status code is 200
    print("The status code is {}".format(req.status_code))
    print( json.loads(req.text) )

    # business_response = client.business.search('Starbucks')


if __name__ == "__main__":
    process("input.json")
    yelp_scrapper()
