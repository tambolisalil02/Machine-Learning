import os
import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataInjestion
from src.mlproject.components.data_ingestion import DataInjestionConfig
if __name__ == "__main__":
    logging.info("The execution has started") 
    try:
        data_ingestion_config = DataInjestionConfig()
        data_injestion =  DataInjestion()
        data_injestion.initiate_data_injestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)