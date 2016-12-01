# ultrasignup

# DFL < DNF < DNS? More Accurately Predicting No-Shows

In trail racing there is the common adage of DFL (dead last) is better than a DNF (did not finish) is better than a DNS (did not start). With the increasing popularity and selling out of ultra-distance trail races, many race directors are having difficulties in predicting how many applicants to accept. Sometimes they are resource-constricted and other times permit-constricted on how many racers can start a race. For the purposes of this study, I will be focusing on the “worst of all evils” in trail racing, predicting the DNS rate based on the individual characteristics of racers in the entrant list for a race. Racers don’t like to DNS and neither do the directors. Ultimately, this will allow a race director to allocate their resources more effectively leading up to and on race day. It will also allow the most popular of races to more accurately predict how it can approach “overselling” a race or how many to place on the waitlist.

This is a repo documenting my journey in modelling this problem. Project is evergreen as of December 1, 2016.

For a detailed log of my workflow, check out log.md, located in this repo.

# Motivation:

Trail racing, ultramarathons in particular, are widely becoming more and more popular in the running community. Even Runner's World has posed the question in a 2015 article "Is 100 Miles the Next Marathon?" http://www.runnersworld.com/racing/is-100-miles-the-new-marathon.

One of the most popular of 100-mile runs, the Western States Endurance Run, has been on a lottery system since 2000. However in 2016 decided to reduce the available slots to implement a waitlist model. 

How does one most effectively manage the depth of a waitlist? 

Previous years averages for no-shows is typically used to create the depth of waitlists for popular ultramarathons. With the wealth of data available to race directors, there has to be a better way to predict, based on characteristics of their race and entrants list to better determine who will show.

Furthermore, for races who are newer or don't have participant caps, how can a race director more effectively allocate resources come race day?

Not only could this result in savings in money, but also volunteer hours and headaches.

# Methods:

* 39 races were scraped from ultrasignup.com, which included >10k runners. 
* Final model had 12 features.
* Both race-specific and runner specific characteristics included.
* Challenges:
  * Data leakage
  * Imbalanced class (only ~5% DNS)
* Tested 3 models:
  * Logistic Regression
  * Random Forest
  * Gradient Boosted Classifier

# Results:

* Gradient Boosted Classifier model produced the most stable results with 10-fold cross-validation (0.67-0.70 area under ROC curve). 
* When applying a given cost-benefit matrix to the ROC curve, profit curves can be developed for Race Directors to see how their race can be impacted through using predicitive modeling. 

# Deployment:

* First generation model has been deployed to http://endurostew.com
* Also included a fun little form for athletes to predict the conditional (on proper training) probability of success at the ultramarathons trained in my current model. 

# Future Work:

* Reach out to Race Directors for more specific data to make the model more robust.
* Ask Race Directors what they want to see in future generations of the model and for more specific use cases.
* Continue developing athlete-specific products, crowdsourcing showed demand is high for predictive modeling products.
