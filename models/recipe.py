from pydantic import BaseModel
from typing import List

class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    instructions: str
    prep_time: int | None = None
    source: str
    url: str
