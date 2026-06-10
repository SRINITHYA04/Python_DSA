# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0
# )

# response = llm.invoke("Say hello")

# print(response.content)

from tools import get_weather
print (get_weather.invoke("Bengaluru"))
