from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir:Path
    URL:str
    local_data_path:Path
    unzip_dir:Path
@dataclass
class DataTransfomationConfig:
    root_dir:Path
    data_path:Path    
    
@dataclass
class ModelTrainconfig:
    root_dir:Path
    train_data_path:Path
    test_data_path:Path
    model_path:Path
    vector_path:Path    
    preprocess_path:Path
    
@dataclass
class ModelEvaluationConfig:
    root_dir:Path
    test_data_path:Path
    model_path:Path
    vector_path:Path 
    metrics_path:str   