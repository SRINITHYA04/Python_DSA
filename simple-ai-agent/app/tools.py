from langchain.tools import tool

@tool
def get_weather(city : str) -> str:
    """
    get weather information"""

    weather_data ={
        "chennai" : "34°C, Sunny",
        "bengaluru" : "28°C, Cloudy",
        "delhi" : "38°C, hot",
    }

    return weather_data.get(
                            city.lower(),
                            "weather info unavailable!!!!1"
                            )