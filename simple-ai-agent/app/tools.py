import httpx
from config import WEATHER_API, GOLD_API_KEY
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
    # print(data)

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    return f"{city}: {temp}°C, {weather}"



@tool
def get_gold_price() -> str:
    """ 
    Returns the current gold proice
    """

    url ="https://api.metalpriceapi.com/v1/latest"
    params = {
        "api_key" : GOLD_API_KEY,
        "base":"INR",
        "currencies":"XAU"
    }

    response = httpx.get(
                            url,
                            params = params,
                            timeout = 10
                        )
    
    data = response.json()
    print(data)

    XAU_price = data["rates"]["INRXAU"]
    
    price_per_gram = XAU_price /31.1035
    price_per_sovereign = price_per_gram *8

    return f"""
        Gold Price:
        1 gram ≈ ₹{price_per_gram:.2f}
        1 sovereign (8g) ≈ ₹{price_per_sovereign:.2f}
        """

