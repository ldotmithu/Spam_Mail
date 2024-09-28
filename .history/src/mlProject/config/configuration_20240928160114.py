from mlProject.entity.config_entity import *
from mlProject.constants import *
from mlProject.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(self) -> None:
        self.config=read_yaml(CONFIG_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self):
        config=self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            URL=config.URL,
            local_data_path=config.local_data_path,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_data_transfomatio_config(self):
        config=self.config.data_transfomation
        
        create_directories([config.root_dir])
        
        data_transfomation_config=DataTransfomationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transfomation_config
    
    def get_model_train_config(self):
        config=self.config.model_train
        
        create_directories([config.root_dir])
        
        model_train_config=ModelTrainconfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            vector_path=config.vector_path,
            preprocess_path=config.preprocess_path
        )
        return model_train_config
    
    def get_model_evaliation_config(self):
        config=self.config.model_evaluation
        
        create_directories([config.root_dir])
        
        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            vector_path=config.vector_path,
            metrics_path=config.metrics_path
        )