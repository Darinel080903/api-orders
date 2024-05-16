from pydantic import BaseModel
from typing import Optional


class Base_response(BaseModel):
    message: str
    data: Optional[dict]
