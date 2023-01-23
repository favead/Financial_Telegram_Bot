from typing import Dict
import json


def get_configs() -> Dict[str, str]:
  with open("config.cfg") as f:
    data = json.dump(f)
  return data