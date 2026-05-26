import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s |%(message)s')
    file_handler = logging.FileHandler('test.txt',encoding='utf-8')
    file_streamer = logging.StreamHandler()
    file_handler.setFormatter(formatter)
    file_streamer.setFormatter(formatter) 
    logger.addHandler(file_handler)
    logger.addHandler(file_streamer)
    return logger