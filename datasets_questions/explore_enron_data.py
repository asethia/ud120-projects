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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print("dataset length :", len(enron_data))

#get all keys from the dictionary
keys=list(enron_data)

#total people/POI

count=len(keys)

#length of first key value
print("features length :",len(enron_data[keys[0]]))

#list of features
#for f in enron_data[keys[0]]:
#    print(f)


#total people 
print("total people  :",count)

#number of keys - POI
poi_count=0
for k in keys:
    features=enron_data[k]
    if(features["poi"]==1):
        poi_count=poi_count+1
       
print("POI Count :",poi_count)

#stock belonging to James Prentice

print("stock belonging to James Prentice :",enron_data["PRENTICE JAMES"]["total_stock_value"])

#email messages do we have from Wesley Colwell to persons of interest

print("email messages do we have from Wesley Colwell to persons of interest :",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

#stock options exercised by Jeffrey K Skilling

print("stock options exercised by Jeffrey K Skilling :",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

salary_count=0
salary_email_address=0
total_payments=0
total_payments_and_poi=0
for k in keys:
    features=enron_data[k]
    if("NaN"!=features["total_payments"]):
        total_payments=total_payments+1
    if("NaN"!=features["total_payments"] and features["poi"]==1):
        total_payments_and_poi=total_payments_and_poi+1    
    if("NaN"!=features["salary"]):
        salary_count=salary_count+1
    if(features["email_address"]!="NaN"):
        salary_email_address=salary_email_address+1
        
doesnot_have_total_payments=(len(keys)-total_payments)
print("number of people qualified for salary: ", salary_count)
print("number of people does have total payments: ", (count-total_payments))
print("% of people does have total payments: ", doesnot_have_total_payments*100/count)
print("number of people has email address with qualified salary: ", salary_email_address)
print("number of people has payments and POI: ", total_payments_and_poi)
print("% of people has payments and POI: ", (poi_count-total_payments_and_poi)*100/count)
