import json
import sys
import pandas as pd
import os
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

def athlete_features(directory1, directory2):

    for p, dirs, files in os.walk(directory1):
        for ff in files:
            print ff
            athlete = pd.read_json(directory1 + '/' + ff)
            first = str(athlete['FirstName'])
            last = str(athlete['LastName'])
            clean = athlete.drop(['ImageId', 'Status', 'FirstName', 'LastName', 'Results'], axis=1)

            for p, dirs, files in os.walk(directory2):
                for f in files:
                    if f == ff + '_clean.csv':
                        print f
                        results = pd.read_json(directory2 + '/' + f)
                        clean['race_total'] = results['status'].count()
                        clean.to_csv('athlete_features/%s.csv' % ff)
                    else:
                        continue



if __name__ == '__main__':
    athlete_features('racers', 'clean_athlete')
