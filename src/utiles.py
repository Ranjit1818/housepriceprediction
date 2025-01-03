#for generic functionlities
import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)
 
def evalute_model(xtrain,ytrain,xtest,ytest,models):
    try:
        report ={}
        for i in range(len(models.values())):
            model  = list(models.values())[i]
            #Train model 
            model.fit(xtrain,ytrain)
          
            #prediciting the testing data
            y_test_pred = model.predict(xtest)
            
            #getting r2_score for train and test data
        
            test_model_score = r2_score(ytest,y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        logging.info("Error is occerd during the evaluating the model")
        raise CustomException(e, sys)

