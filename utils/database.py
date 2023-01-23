from typing import Dict, Union, List, Tuple
import json
from tinydb import TinyDB, Query
from settings.config import get_configs


class MetaSingleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
    return cls._instances[cls]


class Database(TinyDB, metaclass=MetaSingleton):
  __INSTANCE = None

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(args, kwargs)


def get_db() -> Database:
  return Database(get_configs("db_name"))