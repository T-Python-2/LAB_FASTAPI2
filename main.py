from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


cityTemp = {"Riyadh" : 40 ,"Abha" : 23, "Jedda" : 45, "Dammam" : 37}

#http Method GET
@app.get("/")
def index():
    return {"msg": f"cities tempreture {cityTemp}"}

#http Method GET with path parameters
@app.get("/tempreture/{city}")
#query parameters , any parameter that is not a path parameter
def index(city : str ):
    return {"msg": f"{city} tempreture is: {cityTemp[city]}"}


"""
#user model
class User(BaseModel):
    user_name : str
    age : int = 0
    email: str

#response model 
class ResponseModel(BaseModel):
    msg : str
    content : List[User]


#CRUD operations on Model - Create:Post Read:Get Update:Put Delete:Delete


users : list = []

#http Method GET
@app.get("/")
def index():
    return {"msg":"This is the index , or the home page"}


#http Method GET with path parameters
@app.get("/hello/{name}")
#query parameters , any parameter that is not a path parameter
def index(name : str, toUpper:bool = False):
    return {"msg": f"Hello {name}"}


#http Method Get / read
@app.get("/users", response_model=ResponseModel)
def get_users():
    return ResponseModel(msg="All users", content=users)




#http Method Post / create
@app.post("/user/create", response_model=ResponseModel)
def create_user(user : User):
    users.append(user)
    return ResponseModel(msg="Added new user", content=users)



#http Method Put / update
@app.put("/users/update/{index}", response_model=ResponseModel)
def update_user(user:User, index:int):
    users[index] = user
    return ResponseModel(msg="Update user successfully", content=users)




@app.delete("/users/delete/{index}", response_model=ResponseModel)
def delete_user(index:int):
    del users[index]
    return ResponseModel(msg=f"deleted user with id: {index}", content=users)
"""