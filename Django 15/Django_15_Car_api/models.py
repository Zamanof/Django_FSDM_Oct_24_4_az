from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class Car(BaseModel):
    model: str = Field(min_length=1, max_length=100)
    manufacturer: str = Field(min_length=1, max_length=100)
    year: int

    @field_validator('year')
    def year_validator(cls, value):
        if not 1885<= value <= datetime.now().year:
            return ValueError("Year must be between 1885 and current year")
        return value

class CarCreate(Car):
    pass


class CarUpdate(Car):
    pass

class CarRead(Car):
    id: int
