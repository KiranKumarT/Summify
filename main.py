from Summify.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Summify.logging import logger

logger.info("Starting Summify")

STAGE_NAME = "Stage 01: Data Ingestion"
try:
    logger.info(f">>>>>> {STAGE_NAME} starting <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(str(e))
    raise e