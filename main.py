from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class City(BaseModel):
    city_name : str
    weather : int = 0
    
class ResponseModel(BaseModel):
    msg : str
    content : List[City]

cities : list = []

@app.get("/")
def index():
    return {"msg":"This is the index "}

@app.get("/cities", response_model=ResponseModel)
def get_city():
    return ResponseModel(msg="All cities", content=cities)

@app.post("/city/create", response_model=ResponseModel)
def create_city(city : City):
    cities.append(city)
    return ResponseModel(msg="Added new city", content=cities)

@app.put("/cities/update/{index}", response_model=ResponseModel)
def update_city(city:City, index:int):
    cities[index] = city
    return ResponseModel(msg="Update city successfully", content=cities)
@app.delete("/cities/delete/{index}", response_model=ResponseModel)
def delete_city(index:int):
    del cities[index]
    return ResponseModel(msg=f"deleted city with id: {index}", content=cities)