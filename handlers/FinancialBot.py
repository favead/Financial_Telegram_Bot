from datetime import datetime
from typing import List, Dict, Tuple
from models.Expenses import Expense
from models.Categories import Category
from models.Users import User


class FinancialBotHandler:
  def __init__(self) -> None:
    self.user = User
    self.category = Category
    self.expense = Expense
    self.user_id = None

  def add_new_user(self, user_id: int) -> None:
    self.user_id = user_id
    self.user.create(user_telegram_id=user_id)

  def add_new_category(self, user_id: int, category_name: str) -> int:
    cat = self.category.add_new_category(user_id, category_name)
    return cat.id

  def add_new_expense(self, user_id: int, cost: float, datetime: datetime) -> int:
    self.expense.add_new_expense(user_id, cost, datetime)