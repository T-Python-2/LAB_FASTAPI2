from typing import List
from pydantic import BaseModel
from WeatherModel import Weather

class Response(BaseModel):
    msg:str
    content:List[Weather]

class CityResponse(BaseModel):
    content:str