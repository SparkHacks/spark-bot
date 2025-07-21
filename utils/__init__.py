import json
from collections.abc import Callable
from dacite import from_dict
from typing import TypeVar

T = TypeVar("T")

def load_data(filename: str, data_class: Callable[[object], T]) -> list[T]:
    with open(filename, "r") as f_data:            
        return [from_dict(data_class, item) for item in json.load(f_data)]