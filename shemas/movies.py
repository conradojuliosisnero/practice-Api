from pydantic import BaseModel,Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=5,max_length=30)
    año:int = Field(le=2024)
    rating: float = Field(ge=1,le=10)
    categoria: str = Field(min_length=5,max_length=15)
    class Config:
        json_schema_extra = {
					"example": {
						"id": 1,
    					"nombre": "Soul",
    					"año": 2020,
    					"rating": 8.1,
    					"categoria": "Animación"
					}
				}