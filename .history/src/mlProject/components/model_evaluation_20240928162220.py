from mlProject.config.configuration import *
from mlProject import logging
import pandas as pd 
import os,re,joblib
from sklearn.metrics import accuracy_score

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config
        
        
    def preprocess(self,content):
        
        st_content=re.sub(r'\W',' ',content)
        st_content=re.sub('\s+',' ',st_content)
        st_content=st_content.lower()
        st_content=st_content.split()
        st_content=[self.poter.stem(word)for word in st_content]
        
        return ' '.join(st_content)    
    
    def evaluation(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)
        vector=joblib.load(self.config.vector_path)
        
        traget_col='spam'  
        
        X_test=test_data['text']
        y_test=test_data[traget_col]
        
        X_test=X_test.apply(self.preprocess)
        X_test=vector.transform(X_test)
        
        pred=model.predict(X_test)
        score=accuracy_score(y_test,pred)
        logging.info(f'score : {score}')
                
        
        
        
        
    