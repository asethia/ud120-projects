#!/usr/bin/python

import pickle
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]

salary_data=[]
for key in data_dict:
    if(data_dict[key]["salary"]!="NaN" and data_dict[key]["bonus"]!="NaN"):
        salary_data.append((key,data_dict[key]["salary"],data_dict[key]["bonus"]))
salary_data.sort(key=lambda s:s[1],reverse=True)                       

print("outlier :",salary_data[0][0])                       

data_dict.pop(salary_data[0][0],0) 

data = featureFormat(data_dict, features)

#Two people made bonuses of at least 5 million dollars, 
#and a salary of over 1 million dollars find those outlier
print("three people made bonuses of at least 5 million dollars")
for s in salary_data[1:3]:
    print(s[0])

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()


