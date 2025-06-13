import logging
from logging.handlers import RotatingFileHandler

from config import LOG_FILE_NAME

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - [%(asctime)s - %(name)s - %(message)s] -> [%(module)s:%(lineno)d]",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME, mode="w+", maxBytes=5242880, backupCount=1
        ),
        logging.StreamHandler(),
    ]
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.ERROR)

# Setting ntgcalls logger level and disabling propagation
ntgcalls_logger = logging.getLogger("ntgcalls")
ntgcalls_logger.setLevel(logging.CRITICAL)
ntgcalls_logger.propagate = False


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
