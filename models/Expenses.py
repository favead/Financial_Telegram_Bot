from datetime import datetime
from peewee import Model, CharField, ForeignKeyField, FloatField, DateTimeField
from utils.database import BaseModel, get_db
from models.Users import User
from models.Categories import Category


class Expense(BaseModel):
  user_id = ForeignKeyField(User, backref="expenses")
  cost = FloatField()
  datetime = DateTimeField()

  @staticmethod
  def add_new_expense(cls, user_id: int, category_id: int, cost: float, \
    datetime: datetime) -> int:
    pass