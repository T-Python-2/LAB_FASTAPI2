from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class city(BaseModel):
    name : str
    weather: int


class ResponseModel(BaseModel):
    msg : str
    content : List[city]


cities : list = []



@app.get("/")
def index():
    return {"msg":"This is Home page"}



@app.post("/city/create",response_model=ResponseModel)
def add_city(city : city):
    cities.append(city)
    return ResponseModel(msg="New City Has Been Added" , content=cities)


@app.get("/cities",response_model=ResponseModel)
def get_all_cities():
    return ResponseModel(msg="All Cities",content=cities)


@app.put("/cities/update/{index}",response_model=ResponseModel)
def update_city(city:city ,index:int):
    cities[index] = city
    return ResponseModel(msg="City Updated Successfully",content=cities)



@app.delete("/cities/delete/{index}",response_model=ResponseModel)
def delete_city(index:int):
   del cities[index]
   return ResponseModel(msg=f" City with Index {index} Has Been Deleted",content=cities)

