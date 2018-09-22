import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import time

if __name__ == "__main__":
    logger = logging.getLogger("test2")
    logger.setLevel(logging.DEBUG)

    fileHandle = TimedRotatingFileHandler("mylog", when="M", interval=1, backupCount=7)
    fileHandle.suffix = "%Y%m%d_%H%M%S.log"
    fileHandle.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] : %(message)s")
    fileHandle.setFormatter(formatter)
    logger.addHandler(fileHandle)

    for i in range(0, 100):
        logger.debug(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(2)