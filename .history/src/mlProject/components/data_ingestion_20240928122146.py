import urllib.request
from mlProject.entity.config_entity import *
import zipfile,os 
from mlProject import logging
import joblib
import urllib

class DataIngestion:
    def __init__(self) -> None:
        self.config=config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
            urllib.request.urlretrieve(self.config.URL,self.config.local_data_path)
            logging.info('Zip file Download')
            
        else:
            logging.info('File  Alrady Exists')    
            