import logging
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "../logs/test.log")

logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def get_logger():
    return logging.getLogger()