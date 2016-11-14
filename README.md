# ultrasignup

# DFL < DNF < DNS? More Accurately Predicting No Shows

In trail racing there is the common adage of DFL (dead last) is better than a DNF (did not finish) is better than a DNS (did not start). With the increasing popularity and selling out of ultra-distance trail races, many race directors are having difficulties in predicting how many applicants to accept. Sometimes they are resource-constricted and other times permit-constricted on how many racers can start a race. For the purposes of this study, I will be focusing on the “worst of all evils” in trail racing, predicting the DNS rate based on the individual characteristics of racers in the entrant list for a race. Racers don’t like to DNS and neither do the directors. Ultimately, this will allow a race director to allocate their resources more effectively leading up to and on race day. It will also allow the most popular of races to more accurately predict how it can approach “overselling” a race or how many to place on the waitlist.

This is a repo documenting my workflow in modeling this problem. This is evergreen as of November 12, 2016.

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
