from typing import Dict, Union, List, Tuple
import json
from peewee import SqliteDatabase, Model
from settings.config import get_configs


class MetaSingleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
    return cls._instances[cls]


class Database(SqliteDatabase, metaclass=MetaSingleton):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(args, kwargs)


db = Database(get_configs("db_name"))


class BaseModel(Model):
  class Meta:
    database = db

def get_db() -> Database:
  return db