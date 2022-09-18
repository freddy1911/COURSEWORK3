import logging


logging.basicConfig(filename='./logs/api.log', level=logging.INFO)
formatter = logging.Formatter("%(asctime)s :: [%(levelname)s] :: %(message)s :: %(pathname)s")


def my_logger(name, file, level=logging.INFO):
    """ Функция логирования """
    file_handler = logging.FileHandler(file)
    file_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)

    return logger

