November 9, 2016:

* Finished creating python scripts to scrape race results from ultrasignup.com
* Explored workflow for getting athlete data from each race

November 10, 2016:

* Finished creating python scripts to pull all racers out of the race result files stored
* Fixed bug in GDR scraper
* Scraped athlete data and stored
* Added python script to clean up results json object in athlete files
* Added jupyter notebook working towards feature engineering of racer-related characteristics for modeling

November 11, 2016:

* Created python script to create files of only desired athlete features for modeling
* Fixed bug in python script to clean up the results in athlete files to deal with multiple ids per athlete

November 12, 2016:

* Optimizing clean athlete code and athlete features code
* Added python script to concatenate all athlete features into a single .csv for EDA
* Added python script to clean up race results and concatenate into single .csv for EDA
* Added python script to combine races and add on runner features by their identifying participant id number
* Started initial EDA with some scatter plotting and getting handle of the dataset

November 13, 2016:

* EDA work on cleaned dataframe
* Updating jupyter notebook and exploring generalized relationships in dataset to the status (Finish/DNF/DNS) column
* Started playing around with some simple models "off the shelf", Logistic Regression, Random Forest Classifier and Gradient Boosted Classifier, nothing too complex yet, simply for better understanding of data behavior

November 14, 2016:

* Crowd-sourcing more feature engineering. Beginning to add in more race-related details and scoping distance to listed hometown.
* Continued EDA on model choice and metric evaluation parameters.
* Trouble-shooting MVP model for multi-class predictions. DNF classifications appeared to be skewing results, merged DNF and Finished classes and improved prediction of DNS to a log loss of 0.008-0.003 (from 0.8). Confirmed suspicion it is very difficult to predict who will finish long distance ultras.
* Identified data leakage! Fixed data leakage to get more "reasonable" log loss of 0.19-0.2 for Logistic Regression, Random Forest and Gradient Boosted Classifier models. ROC scores of 0.503-0.553. Work to be done for parameter optimization to improve model predictions.
* Modifying code to include other race-related qualifiers including seasons and race id numbers. Hard coded and not optimized, will optimize for v2
* Due to initial results, started v2 feature engineering: added seasons, race id number to the dataframe. Brainstorming and using crowd-sourced ideas to include other metrics easily engineered.

November 15, 2016:

* Trouble-shooting and rebuilding features for input into MVP model
* Initial look at model with new feature engineering yields 0.17-0.19 log loss and auc scores of ~0.73-0.74 0.68
* New features = race season, race metro area (binary classification), race "prestige" (identified by waitlist/lottery/sell out or not)
* Reduced feature dimensionality by removing rankings and total # races
* Improved auc score for RFC to 0.73 (kept runner rank, removed gender and age rank)
* Added features for price per mile and binary classification for $200 entry fee threshold.
* Began grid search optimization on Logistic Regression, Random Forest and Gradient Boosted Classification.
* AUC scores hover in the upper 0.64-0.69 range for optimization runs (including 10-fold cross-validation)
* Best max AUC scores coming from Random Forest

November 16, 2016:

* Cleaning up model workflow for final selection (alpha model)
* Working on cost/benefit matrix to quantify value for final model selection
* Scoping early phase web app for deployment to friends (will contact RDs directly for feedback for beta model deployment)
* First pass profit curves and collated ROC curve plot for final model selection
* Used following values for determinations (open to suggestions and discussion)
* TP (predicted DNS) = $250/racer (average 100 mile race entry that can be resold)
* TN (predicted show) = $100/racer (may return if DNF or suggest race to others if they enjoyed course)
* FP (predicted DNS, but showed) = -$100 (ended up needing more supplies, doesn't include potential reputation risk)
* FN (predicted show, but didn't) = $0 (already bought supplies)

November 17, 2016:

* Doing one more round of feature engineering to pull predictive power behind the DNF rates of individual athletes and for the races in general.
* Feature engineering column for Finish/DNF rate for each athlete (ignoring DNS due to potential data leakage)
  * Random Forest auc = 0.69, Logistic Regression auc = 0.62, Gradient Boosted Classifier auc = 0.698
      * Updated - Random Forect auc = 0.690 (unchanged), Logistic Regression auc = 0.62 (unchanged), Gradient Boosted Classifier auc = 0.701
* First pass model to predict finishers vs. DNF/DNS based on athlete features. Random Forest auc = 0.67, Logistic Regression auc = 0.64, Gradient Boosted Classifier auc = 0.66. All using same parameters as the DNS prediction model.
* Second pass with some parameter tuning yields LR auc = 0.663, RFC auc = 0.67, GBC auc = 0.68
* Added back in total races for athlete into prediction dataframe
   * LR auc = 0.663, RF auc = 0.688, GBC auc = 0.707
* Identified some potential data leakage in features and fixed appropriately. Decreased log loss values considerably.

* Summary of features as of November 17th

DNS Prediction Model:

y(DNS) = 0 / 1 (0 = started, 1 = DNS)
X = age, runner rank (overall), season of race (spring, summer, fall, winter), metro area (w/in 2 hour drive of metro area), waitlist/sell out (1 = sells out/waitlist/lottery, 0 = doesn't fill), entry fee ($200 threshold), price per mile, athlete success metric ((total races finished / total DNF) * total races), gender

Finishing Prediction Model:

y(finished) = 0 / 1 (0 = DNF but started, 1 = Finished)
X = age, runner rank (overall), season of race, total races, success rate, metro area, waitlist/sell out, price per mile, athlete success metric ((total races finished / total DNF) * total races), gender

November 18, 2016:

* Working script to pull current data from 2017 Western States 100 lottery to use for future updating work (using lottery registration date as a predictor of eventual race status)
* Test model on unseen race data from an unrelated race on ultrasignup to assess model performance
* Scraped 2016 Brazos Bend 100 data for unrelated race cross-validation
* Model performed moderately well with a Gradient Boosted Classifier, not very well using Logitic Regression or Random Forest models
GBC predicted 53/61 DNF's for 2016 BB100 accurately. Less accurate in predicting finishers currently.
* Continue scoping webapp deployment options
* Identified template for webapp and working on getting it functional
* Will host in conjunction with my personal blog

November 19, 2016:

* Working on getting webapp designed with Flask using a bootstrap template.
* Simple template updated with a general skeleton of the design
* Identifying ways to plug in blog to webapp
* Decided to give a quick try to fit data to Gaussian Naive Bayes for fun.
* Out of box performance = 0.63 auc score for DNS prediction
* Performs poorly on newly added races (0.55 auc score)
* Out of box performance = 0.64 for DNF prediction

November 20, 2016:

* Continue working front end of webapp
* Early freeze of both models (DNS & DNF) for incorporation into webapp
* Writing python scripts for creating and pickling models

November 21, 2016:

* Completed model pickling
* Continue working on functionality of webapp
* Working on integrating models into webapp with user input

November 22, 2016:

* Working on backend of webapp to get everything connected
* Worked towards getting webapp plumbed for model inputs. Used average values per age group for non-directly entered values into form.
* Made pickled files for X and y test data for final pickled DNS model statistics calculations
* Still need to flesh out JS/Ajax calls to server

November 23, 2016:

* Cleaning up code some
* Continue with backend work on app
* Prepping slides for presentation of MVP

November 25, 2016:

* Cleaning up API scripting work for interpreting and returning json calls from/to webapp.
* Working back end of app/static site
* API now works with form submittals for both racer section and race director sections.
* #optoutside for the afternoon

November 26, 2016:

* Model Version 1 online after modifications to js to allow for html calls rather than json calls
* Deployed heroku app: https://ultrasignup-model-app.herokuapp.com/
* Scoping next phase to migrate to Django for blog incorporation purposes

November 27, 2016:

* Compiling feedback from social media suggestions for minor edits to Version 1 of app for Capstone presentation

November 28, 2016:

* Finishing touches on slides
* Migrating webapp hosting to AWS with endurostew.com domain
* Updates to webapp to increase readibility and navigation

November 29, 2016:

* Subdomain created for existing blog for interim
* Modifying html to reroute to endurostew

November 30, 2016:

* Launched to endurostew.com
* Need to fix broken links on blog

December 1, 2016:

* Links and pictures fixed on blog
* Capstone Presentation
* Moving this log to a new file and start compiling more succinct readme
Contact GitHub API Training Shop Blog About

December 3, 2016:

* Lottery day for 2017 WSER
  * Will run lottery pulls through model when loaded to ultrasignup
