from pydantic import BaseModel
from typing import List, Optional

class UserRequest(BaseModel):
    message: str
    documents: Optional[List[str]] = None