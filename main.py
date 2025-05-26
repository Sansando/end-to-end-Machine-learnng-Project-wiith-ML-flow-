import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline    
from mlProject.pipeline.satge_02_data_validation import DataValidationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e