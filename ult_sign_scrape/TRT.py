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
years_dict = {2016:35090, 2015:30643, 2014:24111, 2013:18412}
file_lst = []

def get_result_pages(root_url, year):
    '''Retrieve results data for a given race url'''
    res_url = root_url + \
    "/service/events.svc/results/%s/json?_search=false" % year
    json_lst = requests.get(res_url).text
    return json_lst

def result_years(years):
    '''Loop through years and url ID for each race in dictionary and feed into
    results function'''
    for year, value in years.iteritems():
        json_lst = get_result_pages(root_url, value)
        year = str(year)
        filename = 'TRT' + year + '.csv'
        file_lst.append(filename)
        f = open(filename, 'w')
        f.write(json_lst)
        f.close()

def parse_lst(filename):
    '''Go through list of json objects for each file and extract to csv format'''
    df_raw = pd.read_csv(filename)
    with open(filename) as f:
        for line in f:
            df = pd.read_json(line)
            df = df.join(pd.read_json(line))
    df.to_csv(test_2013)



print result_years(years_dict)
