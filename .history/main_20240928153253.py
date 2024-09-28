from src.mlProject.pipeline.training_pipeline import (DataIngestionPipeline,
                                                      DataTrnsfomationPipeline,
                                                      ModelTrainPipeline)
from mlProject import logging



Stage_Name='Data Ingestion '
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f'{Stage_Name} completed')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise e     


Stage_Name='Data Transfomation '
try:
    data_transomation=DataTrnsfomationPipeline()
    data_transomation.main()
    logging.info(f'{Stage_Name} completed')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise e    


Stage_Name='Model Train  '
try:
    model_train=ModelTrainPipeline()
    model_train.main()
    logging.info(f'{Stage_Name} completed')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise e    
