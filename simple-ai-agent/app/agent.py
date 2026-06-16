from tools import get_weather
from langchain_groq import ChatGroq
from config import GROQ_API_KEY


llm = ChatGroq(groq_api_key = GROQ_API_KEY,
               model="llama-3.1-8b-instant",
               temperature =0)

#bind the lmm and the tools
Tools =[
    get_weather
 ]

llm_with_tools = llm.bind_tools(Tools)

# response1 = llm_with_tools.invoke("who is donald trump?")
# print(response1)

response = llm_with_tools.invoke("what is the weather in chennai?")

for tool_call in response.tool_calls:
    if(tool_call["name"] == "get_weather"):
        result = get_weather.invoke(tool_call["args"])

print(result)

# print(get_weather.invoke("chennai"))

    
