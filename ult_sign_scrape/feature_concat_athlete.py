import sys
import pandas as pd
import os
reload(sys)
sys.setdefaultencoding('utf-8')

def feature_dataframe(directory):

    data = pd.DataFrame()
    athlete_list = []
    for p, dirs, files in os.walk(directory):
        for ff in files:
            print ff
            data = pd.read_csv(directory + '/' + ff, index_col=None, header=0)
            athlete_list.append(data)

    frame = pd.concat(athlete_list)
    frame.to_csv('athlete_dataframe/athletes_features')

if __name__ == '__main__':
    feature_dataframe('athlete_features')
