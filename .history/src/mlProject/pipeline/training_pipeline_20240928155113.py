from mlProject.components.data_ingestion import *
from mlProject import logging
from mlProject.config.configuration import *
from mlProject.components.data_transomation import *
from mlProject.components.model_train import *

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.Extract_all()
    
class DataTrnsfomationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_transfomation_config=config.get_data_transfomatio_config()
        data_transomation=DataTransfomation(config=data_transfomation_config)
        data_transomation.split()
        
class ModelTrainPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        model_train_config=config.get_model_train_config()
        model_train=ModelTrain(config=model_train_config)
        model_train.model_set()        