#import logging
# import os
# from datetime import datetime
# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(log_path,exist_ok=True)
# LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
import logging
import os
from datetime import datetime
# Define the log file name and directory
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = os.path.join(os.getcwd(), "logs")  # Directory for log files
# Create the logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)
# Full log file path
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)
# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)