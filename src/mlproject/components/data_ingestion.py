import os
import sys 
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
@dataclass
class DataInjestionConfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')
class DataInjestion:
    def __init__(self):
        self.injestion_config=DataInjestionConfig()
    
    def initiate_data_injestion(self):
        try:
            #reading
            df=pd.read_csv("E:\Data Science Projects\Dataset For ML\StudentsPerformance.csv")
            logging.info("Reading completed mysql database")
            
            os.makedirs(os.path.dirname(self.injestion_config.train_data_path),exist_ok=True) #Make artifacts folder
        
            df.to_csv(self.injestion_config.raw_data_path,index=False,header=True) 
            #Train test split
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.injestion_config.train_data_path,index=False,header=True) 
            test_set.to_csv(self.injestion_config.test_data_path,index=False,header=True) 
            logging.info("data injestion is completed")
            return (
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)