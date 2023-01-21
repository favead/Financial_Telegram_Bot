from typing import List


class ExpensesModel:
  def __init__(self, user_id: int) -> None:
    self.user_id = user_id
    self.expenses = self._get_user_expenses()

  def _get_user_expenses(self) -> List[str]:
    pass



class Expense:
  def __init__(self, user_id: int, category: str, cost: float) -> None:
    self.user_id = user_id
    self.category = category
    self.cost = cost

  