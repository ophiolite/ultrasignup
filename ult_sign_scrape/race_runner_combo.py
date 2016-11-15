import pandas as pd
import json

def race_runner_features(directory1, directory2):
    '''INPUT: Two .csv files, one with racer features the other with race
    specific features
    OUTPUT: One .csv file with the combined data, joined on participant ID
    Note: duplicate participant IDs are desired in this case, as they the model
    is for individual races, not racers'''

    race_db = pd.read_csv(directory1)
    athletes = pd.read_csv(directory2)

    for race in race_db.participant_id:
        for athlete in athletes.Id:
            if race == athlete:
                race_db['Age_Rank'] = athletes['AgeRank']
                race_db['Gender_Rank'] = athletes['Rank']
                race_db['Total_races'] = athletes['race_total']
            else:
                continue

    race_db.to_csv('race_master/master_database_fe4.csv')

if __name__ == '__main__':
    race_runner_features('race_master/master_list.csv', 'athlete_dataframe/concat')
