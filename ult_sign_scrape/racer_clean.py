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
                for result in results:
                    json1_data = json.dumps(result[1:])
                    results = json.loads(json1_data)
                    results_df = pd.DataFrame(result)
                    results_df.to_csv('clean_check1/%s' % ff)
            except KeyError:
                continue
            except ValueError:
                continue
                results = racer['Results'].values
                json1_data = json.dumps(results[1])
                results = json.loads(json1_data)
                results_df = pd.DataFrame(results)
                results_df.to_csv('clean_check1/%s' % ff)


if __name__ == '__main__':
    clean_racers('racers')
