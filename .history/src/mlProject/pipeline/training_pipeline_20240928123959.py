from src.mlProject.components.data_ingestion import *
from src.mlProject import logging
from src.mlProject.config.configuration import *

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.Extract_all()