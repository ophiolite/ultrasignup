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
                    if f == ff:
                        print f
                        results = pd.read_csv(directory2 + '/' + f)
                        # if results.status.value_counts()
                        for entry in results.status:
                            # if results.status.values()[-1]:
                            #     results['status'] = results['status']
                            # if len(results.status.value_counts()) > 0:
                            #     clean['Finished'] = results.status.value_counts()[1]
                            # elif:
                            #     clean['Finished'] = 0
                            # else:
                            #     continue
                            # if len(results.status.value_counts()) > 2:
                            #     clean['DNF'] = results.status.value_counts()[2]
                            # elif:
                            #     clean['DNF'] = 0.
                            # else:
                            #     continue
                            # if len(results.status.value_counts()) == 3:
                            #     clean['DNS'] = results.status.value_counts()[3]
                            # elif:
                            #     clean['DNS'] = 0
                            # else:
                            #     continue
                            for each in results:
                                clean['race_total'] = results['status'].count()
                        for each in clean.Id:
                            if 1 in results.status.value_counts():
                                if 3 not in results.status.value_counts() and 2 in results.status.value_counts():
                                    clean['success_rate'] = (results.status.value_counts()[1]) / clean.race_total
                                elif 3 in results.status.value_counts():
                                    DNS = results.status.value_counts()[3]
                                    clean['success_rate'] = (results.status.value_counts()[1]) / (clean.race_total - DNS)
                                else:
                                    clean['success_rate'] = 1.
                            else:
                                clean['success_rate'] = 0.
                        clean.to_csv('athlete_features2/%s' % ff)
                    else:
                        continue




if __name__ == '__main__':
    athlete_features('racers', 'clean_athlete')
