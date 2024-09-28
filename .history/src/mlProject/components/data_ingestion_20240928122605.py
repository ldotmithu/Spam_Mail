import urllib.request
from mlProject.entity.config_entity import *
import zipfile,os 
from mlProject import logging
import joblib
import urllib

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
            urllib.request.urlretrieve(self.config.URL,self.config.local_data_path)
            logging.info('Zip file Download')
            
        else:
            logging.info('File  Alrady Exists')    
            
    def Extract_all(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_path,'r') as f :
            f.extractall(unzip_path) 
            logging.info('Extract All Files')       