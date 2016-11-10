import requests
from string import lowercase
from pymongo import MongoClient
from bs4 import BeautifulSoup
import json
import sys
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf-8')

root_url = 'http://ultrasignup.com'
#index_url = root_url + '/results_event.aspx?did=34773'
years_dict = {2016:34211, 2014:24071}
file_lst = []

#2017 entrants url: http://ultrasignup.com/service/events.svc/entrants/38292/json?_search=false

def get_result_pages(root_url, year):
    '''Retrieve results data for a given race url'''
    res_url = root_url + \
    "/service/events.svc/results/%s/json?_search=false" % year
    json_lst = requests.get(res_url).text
    print json_lst

def result_years(years):
    for year, value in years_dict.iteritems():
        json_lst = get_result_pages(root_url, value)
        year = str(year)
        filename = 'GDR' + year + '.csv'
        file_lst.append(filename)
        f = open(filename, 'w')
        f.write(json_lst)
    return file_lst


def parse_lst():
    pass

print(result_years(years_dict))
