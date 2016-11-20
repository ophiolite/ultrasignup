import model.Model_setup as data
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import GradientBoostingClassifier as GBC

class Finisher_model(object):
    def __init__(self):
        self.df = data.clean_dataframe('../ult_sign_scrape/race_master/master_database_fe4.csv')
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def model_setup(self):
        '''INPUT: .csv of final dataframe
        cleans up and sets up model for training
        OUTPUT: None'''
        y = df.pop('status_coded')
        X = df.drop(['gender', 'participant_id', 'race_name', 'race_id'\
                 , 'gender_M', 'DNF_DNS_coded'], axis=1)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3)

    def final_model(self):
            '''INPUT: GBC model
            Fits and predicts GBC model for module.
            OUTPUT: fitted model as json object'''
            model = GradientBoostingClassifier(loss='deviance', learning_rate=0.005, \
            n_estimators=4700, subsample=0.75, criterion='friedman_mse', \
            min_samples_split=1000, min_samples_leaf=30, min_weight_fraction_leaf=0.0, \
            max_depth=9, min_impurity_split=1e-07, init=None, random_state=None, \
            max_features=11, verbose=0, max_leaf_nodes=None, warm_start=False, \
            presort='auto')
            model.fit(self.X_train, self.y_train)
            filename = 'DNS_model.pkl'
            pickle.dump(model, open(filename, 'wb'))
