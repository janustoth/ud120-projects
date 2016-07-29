#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np
import pandas as pd

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

number_of_people = len(enron_data)
print "number_of_people:", number_of_people

number_of_features = len(enron_data.values()[0])
print "number_of_features:", number_of_features

# put data into a data frame where each person is a row and each feature an index
data = pd.DataFrame.from_dict(enron_data, orient='index')

# convert numerical columns
#data[['total_payments']] = data[['total_payments']].apply(pd.to_numeric, errors='coerce')

number_of_poi = len(data[data['poi'] == 1])
print "number_of_poi:", number_of_poi

# load poi_name into panda dataframe from a text file
poi_names = pd.read_table(open("../final_project/poi_names.txt", "r"), skiprows=1, header=None, names=['have_emails', 'name'], sep='(?<=\(n\)|\(y\)) ', skipinitialspace=True, true_values=["(y)"], false_values=["(n)"] )

number_of_poi_names = len(poi_names)
print "number_of_poi_names:", number_of_poi_names

prentice_james_total_stock_value = data.loc['PRENTICE JAMES']['total_stock_value']
print "prentice_james_total_stock_value:", prentice_james_total_stock_value

number_of_people_without_salary_info = len(data[data.total_payments != 'NaN'])
percentage_of_people_without_salary_info = number_of_people_without_salary_info/ float(len(data))*100

colwell_wesley_email_to_poi = data.loc['COLWELL WESLEY']['from_this_person_to_poi']
print "colwell_wesley_email_to_poi:", colwell_wesley_email_to_poi

skilling_jeffregy_exercised_stock_options = data.loc['SKILLING JEFFREY K']['exercised_stock_options']
print "skilling_jeffregy_exercised_stock_options:", skilling_jeffregy_exercised_stock_options

skilling_jeffrey_total_payments = data.loc['SKILLING JEFFREY K']['total_payments']
print "skilling_jeffrey_total_payments:", skilling_jeffrey_total_payments
lay_kenneth_total_payments = data.loc['LAY KENNETH L']['total_payments']
print "lay_kenneth_total_payments:", lay_kenneth_total_payments
fastow_andrew_total_payments = data.loc['FASTOW ANDREW S']['total_payments']
print "fastow_andrew_total_payments:", fastow_andrew_total_payments

person_that_made_the_most = data[data.total_payments.max()]

number_of_people_with_email_addresses = len(data[data.email_address != 'NaN'])
print "number_of_people_with_email_addresses", number_of_people_with_email_addresses
number_of_people_with_known_salary = len(data[data.salary != 'NaN'])
print "number_of_people_with_known_salary", number_of_people_with_known_salary

number_of_people_without_salary_info = len(data[data.total_payments == 'NaN'])
print "number_of_people_without_salary_info", number_of_people_without_salary_info
percentage_of_people_without_salary_info = number_of_people_without_salary_info/ float(len(data))*100
print "percentage_of_people_without_salary_info", percentage_of_people_without_salary_info

number_of_poi_without_total_payments_info = len(data[data.total_payments == 'NaN'][ data.poi == True])
print "number_of_poi_without_total_payments_info", number_of_poi_without_total_payments_info