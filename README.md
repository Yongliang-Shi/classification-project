# Drivers of Customer Churn

## About the Project

### Goals

![project_overview](https://github.com/Yongliang-Shi/classification-project/blob/master/goal_slide.png)

My goal for this project is to construct a classification model that accurately predicts customer churn. At the same time, I would like to idendity which of these conditions and attributes are the biggest dirivers for customer churn. I will deliver the following: acquire.py, prepare.py, report.ipynb, and predictions.csv.

## Data Dictionary

**gender**: female or male.<br>
**senior_citizen**: yes or no.<br>
**partner**: yes or no.<br>
**depedents**: yes or no.<br>
**tenure**: number of months that a customer has subscribed for.<br>
**phone_service**: yes or no.<br> 
**multiple_lines**: yes, no or no phone service.<br> 
**online_security**: yes, no, or no internect service.<br>
**online_backup**: yes, no, or no internect service.<br>
**tech_support**: yes, no, or no internect service.<br>
**streaming_tv**: yes, no, or no internect service.<br>
**streaming_movies**: yes, no, or no internect service.<br>
**paperless_billing**: yes or no.<br> 
**monthly_charges**: bill for the subscribed services every month (dollars).<br>
**total_charges**: total bill for the subscribed services (dollars).<br>
**churn**: customer stop using services (yes or no).<br>
**contract_type**: month-to-month, one-year or two-year.<br>
**internet_service_type**: none, fiber optic, or DSL (digital subsriber line).<br>
**payment_type**: credit card (automatic), bank transfer (automatic), mailed check or electronic check.<br>

## Project Planning

### acquire.py

acquire data from the telco_churn database on the codeup data science database server. 

### Prepare.py

* Address missing data

* Merge variables with similarit

* Encode variable as needed

* Drop object columns

* Split data into train/validate/test

### Explore

* Explore target variable:
    * Compute overall churn rate
    * Barplot target variable
    
* Explore `churn`'s interactions with the categorical variables by treating it as a number 
    * Demographic: senior_citizen, parnter_dependent and Male
    * Services: multiple_lines, device_protection, tech_support, internet_service_type, streaming, and online_service
    * Payment methods: paperless_billing and payment_type
    * Contract: contract_type
    
* Explore `churn`'s interaction with the numeric variables
    * tenure
    * monthly_tenure
    
* Test 2 early hypothesis

### Modeling and Evaluation

* Try 4 different algorithms: logistic regression, decision tree, random forest and knn

* Which features are most influential?

* Evaluate on train

* Select top 3 models to evaluate on validate

* Select top model

* Run model on test to verify

### Conclusion

* Summarize findings

* Present key takeaways

* Next steps

### Predictions.csv

* csv file with customer_id, probability of churn, and prediction of churn (1=churn, 0=not_churn)

## How to Reproduce

1. Download data from codeup data science database server (You must be logged in first).
2. Install acquire.py and preapre.py into your working directory.
3. Run the jupyter notebook. 
