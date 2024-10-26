from pydantic import BaseModel

class ReviewValidation(BaseModel):
    product: str
    description: str
    rating: int
    username: str