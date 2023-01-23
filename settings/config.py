from typing import Dict
import json


def get_configs(key: str = None) -> Dict[str, str]:
  with open("config.cfg") as f:
    data = json.dump(f)
  if key:
    return data[key]
  return data