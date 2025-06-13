from async_pymongo import AsyncClient as _mongo_client_
from pymongo import MongoClient

import config
from ..logging import LOGGER


DB_NAME = config.BOT_USERNAME

if not config.MONGO_DB_URI:
    LOGGER(__name__).warning(
        "No MONGO DB URL found!"
    )
    raise RuntimeError

_mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
_mongo_sync_ = MongoClient(config.MONGO_DB_URI)
mongodb = _mongo_async_[DB_NAME]
pymongodb = _mongo_sync_[DB_NAME]
