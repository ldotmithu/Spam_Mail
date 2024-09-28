from mlProject.config.configuration import *
import pandas as pd 
from mlProject import logging
import nltk,re,joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer

class ModelTrain:
    def __init__(self,config:ModelTrainconfig):
        self.config=config
        
        
    def preprocess(self,content):
        
        st_content=re.sub(r'\W',' ',content)
        st_content=re.sub('\s+',' ',st_content)
        st_content=st_content.lower()
        st_content=st_content.split()
        st_content=[ PorterStemmer.stem(word)for word in st_content]
        
        return ' '.join(st_content)
        
        
            
    def model_set(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        traget_col='spam'\\       
  