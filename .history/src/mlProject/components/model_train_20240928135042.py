from mlProject.config.configuration import *
import pandas as pd 
from mlProject import logging

class ModelTrain:
    def __init__(self,config:ModelTrainconfig):
        self.config=config
        
    def model_set(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        