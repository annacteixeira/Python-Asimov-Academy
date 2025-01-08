from pydantic import BaseModel, Field

class User(BaseModel):
    telegram_id: int
    name: str
    gender: str
    age: str
    height_cm: str
    weight_kg: str
    has_diabetes: str
    goal: str