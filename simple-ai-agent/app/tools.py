import httpx
from config import WEATHER_API, GROQ_API_KEY


from langchain.tools import tool

@tool
def get_weather(city : str) -> str:

    """
    get current weather information for a city
    """

    url = "https://api.openweathermap.org/data/2.5/weather"
    params ={
        "q":city,
        "appid": WEATHER_API,
        "units":"metric"
    }

    response = httpx.get(
        url,
        params=params,
        timeout=10
        )
    
    data = response.json()
    # print(data.keys())

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    return f"{city}: {temp}°C, {weather}"

