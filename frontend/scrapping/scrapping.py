import json
import random
import urllib.parse
import urllib.request
from thefuzz import fuzz

def write_output(output):
    with open('output.json', 'w') as output_file:
        output_file.write(json.dumps(output))


def process_company(company):
    result = send_api_request(company['name'])
    with open('data.json', 'a+') as f:
        f.write('{"name": "' + company['name'] + '", "result": ')
        f.write(json.dumps(result)) 
        f.write('},')
    google_score = get_google_score(company['name'], result) if result else 0
    print(google_score)
    return {'name': company['name'], 'rating': google_score }


def process(filename):
    with open(filename) as input_file:
        data = json.load(input_file)
    output = list(map(process_company, data[:]))
    write_output(output)

def get_google_score(name, response):
    name_similarity = fuzz.token_sort_ratio(name, response['result']['name'])
    return 1 if name_similarity > 90 else 0

def send_api_request(name):
    api_key = open('.api_key').read()
    query = name
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        #'types': 'LocalBusiness',
        'limit': 1,
        'indent': True,
        'key': api_key,
    }
    url = service_url + '?' + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read())

    return response['itemListElement'][0] if response['itemListElement'] else {}


if __name__ == '__main__':
    process('input.json')