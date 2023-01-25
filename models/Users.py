from peewee import Model, CharField, IntegerField
from utils.database import get_db, BaseModel


class User(BaseModel):
  user_telegram_id = IntegerField()