import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split

class Model_setup(object):
    def __init__(self):
        pass

    def clean_dataframe(filename):
        '''INPUT: .csv file with feature data
        OUTPUT: dataframe for model analysis'''
        ##Clean data by dropping extraneous columns
        data = pd.read_csv(filename)
        cleaned_data = data.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1)
        ##Second stage of cleaning by removing na values from dataframe
        cleaned_data = cleaned_data.dropna()
        cleaned_data['success_metric'] = cleaned_data['Total_races'] * cleaned_data['Success_rate']
        ##Create gender dummy variables for model
        gender_dummies = pd.get_dummies(cleaned_data.gender, prefix='gender')
        cleaned_data = cleaned_data.join(gender_dummies)
        cleaned_data["status_coded"] = coding(cleaned_data["status"], {'1':0,'2':0, '3':1})
        cleaned_data['DNF_DNS_coded'] = coding(cleaned_data["status"], {'1':1,'2':0, '3':0})


    def coding(col, codeDict):
        '''Consolidate all starts (code DNF with finishers) for modeling'''
        colCoded = pd.Series(col, copy=True)
        for key, value in codeDict.items():
            colCoded.replace(key, value, inplace=True)
        return colCoded
