from flask import Flask, render_template, send_from_directory, request, jsonify
import numpy as np
import json
import sys
import cPickle as pickle
import pandas as pd
import requests

app = Flask(__name__)

@app.endpoint('model.endpoint')

def load_model(filename):
    with open(filename) as f:
        model = pickle.load(f)
    return model

def race_dir_button(filename):
    '''When clicked, allows for model stats to pop up for the DNS model'''
    ##May just bypass the pickled model for this one and just pop up the model
    ##statistics calculated by the holdout data and just return the numeric values

    ##If time allows, have a dropdown to show the results of the BB100 hold out test
    #DNS_model.predict_proba()
    AUC_score = 0.681
    accuracy_score = 0.956
    acurrate_show = 'Successfully predicted 3015 out of 3016 runners who showed'
    return jsonify(AUC_score, accuracy_score, accurate_show) ##return when button clicked


def parse_athlete_json(answer_list):
    '''Takes answers from form on app and makes list for entry into DNF modeling'''
##button entries include age, gender, and race
##extrapolate from race: Season, Metro_area, WL_SO, Entry_fee, PPM
##gender/age group averages for: runner_rank, Age_Rank, Gender_Rank, Success_rate, Total_races
    '''Need to change reader from list to numpy array'''
    pass

def Gender_F():
    gender = pd.read_json(gender)
    if ans == 'M':
        Gender_F = 0.
    else:
        Gender_F = 1
    return Gender_F

def race_factors():
    race_factors = pd.read_json(race_factors)
    race_fields = ['Season', 'Metro_area', 'WL_SO', 'Entry_fee', 'PPM']
    pd.concat([race_features,pd.DataFrame(columns=race_fields)])
    # if ans == 'BB':
    #     Season = 4
    #     Metro_area = 1
    #     WL_SO = 0
    #     Entry_fee = 0
    #     PPM = 1.9
    if ans == 'Bear 100':
        race_factors = {Season: 3, Metro_area: 0, WL_SO: 1, Entry_fee: 1, PPM: 2.5}
    elif ans == 'Black Canyon 100k':
        race = {Season: 4, Metro_area: 1, WL_SO: 0, Entry_fee: 0, PPM: 2.5}
    elif ans == 'Canyons 100k':
        race_factors = Season = 1
        Metro_area = 1
        WL_SO = 1
        Entry_fee = 1
        PPM = 3.2
    elif ans == 'Eastern States 100':
        Season = 2
        Metro_area = 0
        WL_SO = 0
        Entry_fee = 0
        PPM = 1.85
    elif ans == 'FatDog 120':
        Season = 2
        Metro_area = 0
        WL_SO = 1
        Entry_fee = 1
        PPM = 2.7
    elif ans == 'Javelina Jundred':
        Season = 3
        Metro_area = 1
        WL_SO = 0
        Entry_fee = 1
        PPM = 2.65
    elif ans == 'San Diego 100':
        Season = 2
        Metro_area = 1
        WL_SO = 1
        Entry_fee = 1
        PPM = 2.65
    elif ans == "Sean O'Brien 100k":
        Season = 4
        Metro_area = 1
        WL_SO = 0
        Entry_fee = 0
        PPM = 2.5
    elif ans == 'Tahoe Rim Trail 100':
        Season = 2
        Metro_area = 1
        WL_SO = 1
        Entry_fee = 1
        PPM = 2.75
    elif ans == 'Western States 100':
        Season = 2
        Metro_area = 1
        WL_SO = 1
        Entry_fee = 1
        PPM = 4.1
    elif ans == 'Zion 100':
        Season = 1
        Metro_area = 1
        WL_SO = 1
        Entry_fee = 1
        PPM = 2.5
    elif ans == 'Georgia Death Race':
        Season = 1
        Metro_area = 1
        WL_SO = 1
        Entry_fee = 1
        PPM = 3.16
##need something in here to catch numeric from string input
def age_factors(age):

        try:
            age = pd.read_json(int(age))
        except ValueError:
            print("Age is but a number, dude!")

        if age < 20:
            age_dict = {Age: age, runner_rank: 70.3851, Age_Rank: 0.7538, \
            Gender_Rank: 0.6842, Success_rate, 0.900, Total_races: 11.515}
        elif age >= 20 and age < 30:
            age_dict = {Age: age, runner_rank: 74.5336, Age_Rank, 0.7254, \
            Gender_Rank: 0.6560, Success_rate: 0.8798, Total_races, 10.286}
        elif age >= 30 and age < 40:
            age_dict = {Age:age, runner_rank: 72.3374, Age_Rank: 0.7319, \
            Gender_Rank: 0.6689, Success_rate: 0.8867, Total_races: 11.352}
        elif age >= 40 and age < 50:
            age_dict = {Age: age, runner_rank: 69.9372, Age_Rank: 0.7308, \
            Gender_Rank: 0.6668, Success_rate, 0.8753, Total_races: 11.191}
        elif age >= 50 and age < 60:
            age_dict = {Age: age, runner_rank: 66.6021, Age_Rank: 0.7339, \
            Gender_Rank: 0.6733, Success_rate: 0.8837, Total_races: 11.092}
        elif age >= 60 and age < 70:
            age_dict = {Age: age, runner_rank: 61.5856, Age_Rank: 0.7213, \
            Gender_Rank: 0.6683, Success_rate: 0.8721, Total_races: 10.311}
        elif age > 70:
            age_dict = {Age: age, runner_rank: 58.3583, Age_Rank: 0.7308, \
            Gender_Rank: 0.6395, Success_rate: 0.8579, Total_races = 10.080}

    return age_dict

@app.route('/', methods=['GET'])
def index():
    return render_template('bootstrap2.html')

@app.route('/images/<path:path>', methods=['GET'])
def send_image(path):
    return send_from_directory('images', path)

@app.route('/athlete_proba', methods=['POST'])
def Finish_proba():
    athlete_answers = request.json
    age, gender, race = (athlete_answers[0],
                                      athlete_answers[1],
                                      athlete_answers[2])
    age_factors = age_factors(age)
    gender_factors = gender_factors(gender)
    race_factors = race_factors(race)
    #profile = parse_athlete_json(athlete_answers)
    answer_list = [Age, runner_rank, Season, Metro_area, \
    WL_SO, Entry_fee, PPM, Age_Rank, Gender_Rank, \
    Total_races, Success_rate, Gender_F]
    probas = Finish_model.predict_proba(answer_list)
    return jsonify(probas[0][1]) ##returns the numeric probability of success for selected race

@app.route('/blog', methods=['GET'])
def index():
    return render_template('blog.html')



if __name__ == '__main__':
    filename = '../model/DNS_model.pkl'
    filename2 = '../model/Finish_model.pkl'
    DNS_model = load_model(filename)
    Finish_model = load_model(filename2)
    app.run()
