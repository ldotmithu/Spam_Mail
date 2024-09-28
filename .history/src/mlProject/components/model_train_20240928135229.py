from mlProject.config.configuration import *
import pandas as pd 
from mlProject import logging
import nltk,re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


class ModelTrain:
    def __init__(self,config:ModelTrainconfig):
        self.config=config
        
        
    def preprocess(self):
        
            
    def model_set(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        