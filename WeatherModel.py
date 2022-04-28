from pydantic import BaseModel

class Weather(BaseModel):
    city_name:str
    temp:float

