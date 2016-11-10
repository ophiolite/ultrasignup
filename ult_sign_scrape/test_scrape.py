import requests
from string import lowercase
from pymongo import MongoClient
from bs4 import BeautifulSoup
import json

root_url = 'http://ultrasignup.com'
#index_url = root_url + '/results_event.aspx?did=34773'
years = [34733, 30033, 24962, 17746]

def get_result_pages(root_url, year):
    '''Retrieve results data for a given race url'''
    res_url = root_url + \
    "/service/events.svc/results/%s/json?_search=false" % year
    json_lst = requests.get(res_url).text
    return json_lst

def result_years(years):
    for year in years:
        get_result_pages(root_url, year)


def parse_lst():
    pass

print(result_years(years))
