import json
import sys
import pandas as pd
import os
reload(sys)
sys.setdefaultencoding('utf-8')

root_url = 'http://ultrasignup.com'
directory = 'race_results'

def read_races(directory):
    '''Loop through race files and format into dataframe
    INPUT: csv file of json
    OUTPUT: dataframe of race'''
    for p, dirs, files in os.walk(directory):
        for f in files:
            racedf = pd.read_json(f)
            name_dict = athlete_dataframe(racedf)
            races = racers_race(name_dict)

def athlete_dataframe(df):
    athlete = racedf[['firstname','lastname']]
    name_dict = athlete.to_dict('records')
    return name_dict

def racers_race(name_dict):
    '''Loop through years and url ID for each race in dictionary and feed into
    results function'''
    racers = [(r['firstname'], r['lastname']) for r in name_dict]
    for racer in racers:
         get_racer_results(root_url, racer[0], racer[1])

def get_racer_results(root_url, fname, lname):
    '''Retrieve results data for a given racer'''
    res_url = root_url + \
    "/service/events.svc/history/%s/%s/" % (fname, lname)
    race_lst = requests.get(res_url).text
    filename = fname + '_' + lname + '.csv'
    f = open(filename, 'w')
    f.write(race_lst)
    f.close()

if __name__ == '__main__':
    read_races('race_results')
