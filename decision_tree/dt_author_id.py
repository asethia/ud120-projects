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
features_train_1, features_test_1, labels_train_1, labels_test_1 = preprocess(selectPercentile=1)

#when selectPercentile=10
features_train_10, features_test_10, labels_train_10, labels_test_10 = preprocess(selectPercentile=10)


print("number of features in training data when selectPercentile=1:",len(features_train_1[0]))

print("number of features in training data when selectPercentile=10:",len(features_train_10[0]))


#########################################################
### your code goes here ###

from sklearn import tree
clf_1=tree.DecisionTreeClassifier(min_samples_split=minSamplesSplit)
clf_1=clf_1.fit(features_train_1, labels_train_1)

acc1=clf_1.score(features_test_1,labels_test_1)

clf_10=tree.DecisionTreeClassifier(min_samples_split=minSamplesSplit)
clf_10=clf_10.fit(features_train_10, labels_train_10)

acc10=clf_10.score(features_test_10,labels_test_10)

#########################################################

print("accuracy when selectPercentile=1:",acc1)

print("accuracy when selectPercentile=10:",acc10)

