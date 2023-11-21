import logging
from datetime import datetime
from time import sleep

logging.basicConfig(
    format="%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s",
    level=logging.INFO,
)


def startup():
    """
    Rotina de inicialização
    """
    logging.info("Iniciando...")
    with open("src/static/log_art.ascii", "r", encoding="utf-8") as log_art:
        logging.info(log_art.read())


def app():
    """
    Rotina principal
    """
    startup()
    while True:
        logging.info("%s", datetime.now())
        sleep(2)
