from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

#city class 
class City(BaseModel):
    city_name : str
    temperature : int

#response model 
class ResponseModel(BaseModel):

    msg : str
    cities_list : List[City]

cities : list = []

#http Method Get to view all citites 
@app.get("/cities" ,response_model= ResponseModel )
def get_cities():
    return ResponseModel(msg="All cities", cities_list= cities)

#http Method Post to add new city
@app.post("/cities/create", response_model=ResponseModel)
def create_city(city : City):
    cities.append(city)
    return ResponseModel(msg="Added new city", cities_list=cities)


#http Method Put to update the weather temperature for a spcicif city
@app.put("/cities/update/{index}", response_model=ResponseModel)
def update_temp(city:City, index:int):
    cities[index] = city
    return ResponseModel(msg="Update city temperature successfully", cities_list=cities)

#http Method Delete to delete a city
@app.delete("/cities/delete/{index}", response_model=ResponseModel)
def delete_city(index:int):
    del cities[index]
    return ResponseModel(msg=f"deleted city with id: {index}", cities_list=cities)


