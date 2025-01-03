import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from src.exception import CustomException
from src.logger import logging
from src.utiles import save_object
from dataclasses import dataclass
import sys
import os
from src.utiles import evalute_model


@dataclass
class ModelTrainerConfig:
    train_model_file_path: str = os.path.join('artifacts','model.pkl')

class modeltrainer:
    def __init__(self):
        self.model_training_config = ModelTrainerConfig()
    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("Spitting dependent and Independent variable from train and test ")
            xtrain,ytrain,xtest,ytest = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]

            )
            #training the multiple model
            models = {
            'LinearRegression':LinearRegression(),
            'Lasso':Lasso(),
            'Ridge':Ridge(),
            'ElasticNet':ElasticNet()

            }
            model_report:dict = evalute_model(xtrain,ytrain,xtest,ytest,models)
            print("MODEL REPORT...")
            print('\n===================================================================================\n')
            logging.info(f'Model report: {model_report}')

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]
            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(
                 file_path=self .model_training_config.train_model_file_path,
                 obj=best_model
            )
        except Exception as e:
            logging.info("Error is Occered in model training")
            raise CustomException(e,sys)