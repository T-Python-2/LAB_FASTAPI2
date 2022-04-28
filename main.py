from fastapi import FastAPI
from WeatherModel import Weather
from ResponseModel import Response,CityResponse





cities_weather = [Weather(city_name="Riyadh",temp=50),Weather(city_name="Abha",temp=14),Weather(city_name="Jedda",temp=34),Weather(city_name="Dammam",temp=40)]

app = FastAPI()

@app.get("/")
def index():
    return "This is the index page.For information, try /docs"

#GET all cities weather
@app.get("/cities",response_model= Response)
def get_all_cities_weather():
    return Response(msg= "Weather for all cities", content=cities_weather)

@app.get("/cities/{city_name}",response_model= CityResponse)
def get_city_weather(city_name:str):
    city_weather = next((f"The temperature in {weather.city_name} is {weather.temp} degrees." for weather in cities_weather if city_name == weather.city_name),f"Error: There is no city named {city_name}")
    return CityResponse(content=city_weather)

#Add a new city 
@app.post("/cities/create",response_model=Response)
def create_city(city_weather: Weather):
    cities_weather.append(city_weather)
    return Response(msg="Added a new city", content= cities_weather)


#Update the weather for a specific city
@app.put("/cities/update/{index}",response_model= Response)
def update_city(city_weather: Weather, index:int):
    cities_weather[index] = city_weather
    return Response(msg= f"The weather for the city {city_weather.city_name} is updated!", content= cities_weather)

#Delete a city
@app.delete("/cities/delete/{index}", response_model= Response)
def delete_city(index:int):
    del cities_weather[index]
    return Response(msg = f"Deleted weather for the city with the id {index}",content= cities_weather )

