from mlProject.entity.config_entity import *
from mlProject.constants import *
from mlProject.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(self) -> None:
        self.config=read_yaml(CONFIG_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self):
        config=self.config.data_ingestion
        
            