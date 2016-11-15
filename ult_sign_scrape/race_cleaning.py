import json
import sys
import pandas as pd
import os
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

Bear = {2016:34749, 2013:18622, 2012:15242, 2011:11470}
Black_Canyon = {2016:34087, 2014:24355}
Canyons = {2015:30603}
ES100 = {2016:34680, 2014:22675}
FatDog = {2016:35969, 2015:30194, 2014:24501, 2013:18075, 2012:14868}
GDR = {2016:34211, 2014:27071}
JJ = {2016:35377, 2015:31274, 2014:27560, 2013:19185, 2012:15839, 2011:12159}
SD = {2016:33977, 2015:30643, 2014:22699, 2012:13858, 2011:11813}
SOB = {2016:33769}
TRT = {2016:35090, 2015:30643, 2014:24111, 2013:18412}
WSER = {2016:34733, 2015:30033, 2014:24962, 2013:17746}
Zion = {2015:29195, 2014:22673, 2013:17113, 2012:13855}

Season = {'Bear': 'Fall', 'Black_Canyon': 'Winter', 'Canyons': 'Spring', \
            'ES100': 'Summer', 'Fatdog': 'Summer', 'GDR': 'Spring', 'JJ': 'Fall', \
            'SD': 'Summer', 'SOB': 'Winter', 'TRT': 'Summer', 'WSER': 'Summer', \
            'Zion': 'Spring'}

def clean_races(directory):
    '''INPUT: directory of json objects
    OUTPUT: cleaned files in csv format for further feature engineering'''

    for p, dirs, files in os.walk(directory):
        for ff in files:
            print ff
            race = pd.read_json(directory + '/' + ff)
            df = race.drop(['photo_count', 'firstname', 'lastname', \
                            'drilldown', 'time', 'formattime', \
                        'race_count', 'bib', 'age_rank', 'prior_count', \
                        'city', 'state', 'agegroup', 'place', 'gender_place'], \
                         axis=1)

            year = int(ff[-8:-4])

            df['race_id'] = globals()[ff[:-8]][year]
            df['race_name'] = ff[:-8]

            if ff[:-8] == 'Bear':
                df['Season'] = 3
                df['Metro_area'] = 0
                df['WL_SO'] = 1
            elif ff[:-8] == 'Black_Canyon':
                df['Season'] = 4
                df['Metro_area'] = 1
                df['WL_SO'] = 0
            elif ff[:-8] == 'Canyons':
                df['Season'] = 1
                df['Metro_area'] = 1
                df['WL_SO'] = 0
            elif ff[:-8] == 'ES100':
                df['Season'] = 2
                df['Metro_area'] = 0
                df['WL_SO'] = 0
            elif ff[:-8] == 'FatDog':
                df['Season'] = 2
                df['Metro_area'] = 0
                df['WL_SO'] = 1
            elif ff[:-8] == 'JJ':
                df['Season'] = 3
                df['Metro_area'] = 1
                df['WL_SO'] = 0
            elif ff[:-8] == 'SD':
                df['Season'] = 2
                df['Metro_area'] = 1
                df['WL_SO'] = 1
            elif ff[:-8] == 'SOB':
                df['Season'] = 4
                df['Metro_area'] = 1
                df['WL_SO'] = 0
            elif ff[:-8] == 'TRT':
                df['Season'] = 2
                df['Metro_area'] = 1
                df['WL_SO'] = 1
            elif ff[:-8] == 'WSER':
                df['Season'] = 2
                df['Metro_area'] = 1
                df['WL_SO'] = 1
            elif ff[:-8] == 'Zion':
                df['Season'] = 1
                df['Metro_area'] = 1
                df['WL_SO'] = 1
            elif ff[:-8] == 'GDR':
                df['Season'] = 1
                df['Metro_area'] = 1
                df['WL_SO'] = 1

            df.to_csv('cleaned_races/%s' % ff)

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
    frame.to_csv('race_master/master_list.csv')

if __name__ == '__main__':
    clean_races('scraped_races')
    race_master('cleaned_races')
