from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# print(GROQ_API_KEY)

WEATHER_API = os.getenv("OPENWEATHERMAP_API_KEY")
# print(WEATHER_API)