import json
import sys
import pandas as pd
import os
import requests
reload(sys)
sys.setdefaultencoding('utf-8')


def clean_racers(directory):
    for p, dirs, files in os.walk(directory):
        for ff in files:
            print ff
            racer = pd.read_json(directory + '/' + ff)
            
            try:
                results = racer['Results'].values
                json1_data = json.dumps(results[0][1:])
                results = json.loads(json1_data)
                results_df = pd.DataFrame(results)
                filename =  ff + '_clean.csv'
                f = open(filename, 'w')
                f.write(json1_data)
                f.close()
            except KeyError:
                continue
            except ValueError:
                continue


if __name__ == '__main__':
    clean_racers('racers')
