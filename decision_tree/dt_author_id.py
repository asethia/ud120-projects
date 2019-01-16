#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

minSamplesSplit=40
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess(selectPercentile=10)


print("number of features in training data:",len(features_train[0]))

#########################################################
### your code goes here ###

from sklearn import tree
clf=tree.DecisionTreeClassifier(min_samples_split=minSamplesSplit)
clf=clf.fit(features_train, labels_train)

acc=clf.score(features_test,labels_test)

#########################################################

print("accuracy:",acc)

