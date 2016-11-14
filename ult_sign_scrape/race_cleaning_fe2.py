import json
import sys
import pandas as pd
import os
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

def clean_races(directory):
    '''INPUT: directory of json objects
    OUTPUT: cleaned files in csv format for further feature engineering'''

    for p, dirs, files in os.walk(directory):
        for ff in files:
            print ff
            race = pd.read_json(directory + '/' + ff)
            df = race.drop(['photo_count', 'firstname', 'lastname', \
                            'drilldown', 'formattime', \
                        'race_count', 'bib', 'prior_count', \
                        'agegroup', 'age_rank', 'time', 'place', 'gender_place'], \
                         axis=1)
            df.to_csv('cleaned_races/fe2/%s' % ff)

def race_master(directory2):
    '''INPUT: directory of cleaned race csv files
    OUTPUT: master csv file containing all racers for each race'''

    data = pd.DataFrame()
    race_list = []
    for p, dirs, files in os.walk(directory2):
        for ff in files:
            print ff
            data = pd.read_csv(directory2 + '/' + ff, index_col=None, header=0)
            race_list.append(data)

    frame = pd.concat(race_list)
    frame.to_csv('race_master/master_list_fe2.csv')

if __name__ == '__main__':
    clean_races('scraped_races')
    race_master('cleaned_races/fe2')
