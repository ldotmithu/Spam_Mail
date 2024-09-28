from mlProject.pipeline.training_pipeline import *

Stage_Name='Data Ingestion '
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f'{Stage_Name} completed')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')