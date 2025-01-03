import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import modeltrainer




if __name__ == '__main__':
    obj=DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    transfer_data = DataTransformation()
    train_array,test_array,_= transfer_data.initaite_data_transformation(train_data_path,test_data_path)
    model_trainner = modeltrainer()
    model_trainner.initiate_model_training(train_array,test_array)

