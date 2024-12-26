from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    interested_in: str
    location: str
    hobbies: List[str]
    interests: List[str]
    occupation: str
    education_level: str
    personality_traits: List[str]
