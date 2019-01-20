#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    
    ### your code goes here
    length_of_data=len(predictions)
    dataSet=[]
    for i in range(length_of_data):
        error=pow((predictions[i][0]-net_worths[i][0]),2)
        dataSet.append((ages[i][0],net_worths[i][0],error))
    dataSet.sort(key=lambda s : s[2])
    cleaned_data=dataSet[:int(length_of_data*0.9)]
    return cleaned_data

