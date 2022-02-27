import subprocess
from urllib import response


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
    gscore = google_scrapper(company)
    yscore = yelp_scrapper(company)
    return {"name": company["name"], "rating": gscore + yscore}

def google_scrapper(company):
    result = send_google_api_request(company["name"])
    google_score = get_google_score(company["name"], result) if result else 0
    return google_score

def process(filename):
    pre_data = urllib.request.urlopen("https://raw.githubusercontent.com/saltpay/oxfordhack-minichallenge/master/input-alt.json").read()
    data = json.loads(pre_data)
    output = list(map(process_company, data[:]))
    write_output(output)


def get_google_score(name, response):
    name_similarity = fuzz.token_sort_ratio(name, response["result"]["name"])
    return 2 if name_similarity > 90 else 0


def send_google_api_request(name):
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


def yelp_scrapper(company):
    response = send_yelp_api_request(company)
    yelp_score = get_yelp_score(company['name'], response) if response else 0
    return yelp_score


def get_yelp_score(name, response):
    name_similarity = fuzz.token_sort_ratio(name, response["name"])
    if name_similarity < 65:
        return 0
    return 2 + get_review_score(response['review_count'])
    

def get_review_score(review_count):
    return min(100, review_count) / 100 * 6

def send_yelp_api_request(company):
    MY_API_KEY = "xgtN0hq4WTZcd_42NJXze7vNbVsHOVxyf38ibF-RWHj9Y6zOwWbNMagWyfyXmJeCGupWtE1XWG6zTz-NLRvQ6qGveO3GSYW4DAMk31XkXmP4reMYU757Z9tj4vUaYnYx "

    headers = {"Authorization": "Bearer %s" % MY_API_KEY}
    url = "https://api.yelp.com/v3/businesses/search"
    params = {"term": company['name'], 'location': company['address']}

    response = requests.get(url, params=params, headers=headers)
    response = json.loads(response.text)
    return response['businesses'][0] if response['businesses'] else {}


if __name__ == "__main__":
    process("input.json")
