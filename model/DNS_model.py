from Model_setup import Model_setup as data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier as GBC
import pickle
import pandas as pd
import numpy as np

class DNS_model(object):

    def __init__(self, filename):
        self.df = data.clean_dataframe(filename)
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def model_setup(self):
        '''INPUT: .csv of final dataframe
        cleans up and sets up model for training
        OUTPUT: None'''
        y = self.df.pop('status_coded')
        X = self.df.drop(['gender', 'participant_id', 'race_name', 'race_id'\
                 , 'gender_M', 'DNF_DNS_coded', 'status'], axis=1)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3)
        print self.X_train.info()

    def final_model(self):
            '''INPUT: GBC model
            Fits and predicts GBC model for module.
            OUTPUT: fitted model as json object'''
            model = GBC(loss='deviance', learning_rate=0.005, \
            n_estimators=4700, subsample=0.75, criterion='friedman_mse', \
            min_samples_split=1000, min_samples_leaf=30, min_weight_fraction_leaf=0.0, \
            max_depth=9, min_impurity_split=1e-07, init=None, random_state=None, \
            max_features=11, verbose=0, max_leaf_nodes=None, warm_start=False, \
            presort='auto')
            model.fit(self.X_train, self.y_train)
            filename = 'DNS_model.pkl'
            X_test = 'X_test.pkl'
            y_test = 'y_test.pkl'
            pickle.dump(model, open(filename, 'wb'))
            pickle.dump(self.X_test, open(X_test, 'wb'))
            pickle.dump(self.y_test, open(y_test, 'wb'))

if __name__ == '__main__':
    filename = '../ult_sign_scrape/race_master/master_database_fe4.csv'
    dnsmodelinstance = DNS_model(filename)
    dnsmodelinstance.model_setup()
    dnsmodelinstance.final_model()
