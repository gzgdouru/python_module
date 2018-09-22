#coding:utf-8
import logging

logger = logging.getLogger("simple_exemle")
logger.setLevel(logging.DEBUG)

#建立一个fileHandler来把日志记录在文件里,级别为DEBUG以上
fh = logging.FileHandler("spam.log")
fh.setLevel(logging.DEBUG)

#建立一个stringHandler来把日志打印到屏幕上,级别为DEBUG以上
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

#设置日志格式
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] : %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")


