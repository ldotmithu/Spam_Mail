from mlProject.components.data_ingestion import *
from mlProject import logging
from mlProject.config.configuration import *
from mlProject.components.data_transomation import *

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