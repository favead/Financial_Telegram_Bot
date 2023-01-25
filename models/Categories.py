from peewee import Model, CharField, ForeignKeyField
from utils.database import BaseModel, get_db
from models.Users import User


class Category(BaseModel):
  category_name = CharField()
  user_id = ForeignKeyField(User, backref="categories")

  @staticmethod
  def add_new_category(cls, user_id: int, category_name: str) -> int:
    return Category.create(category_name=category_name, user_id=user_id)

  