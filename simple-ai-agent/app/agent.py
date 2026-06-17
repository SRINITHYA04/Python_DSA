from tools import get_weather
from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(groq_api_key = GROQ_API_KEY,
               model="llama-3.1-8b-instant",
               temperature =0)


# print ((llm.invoke("What is rag?")).content)
# print ((llm.invoke("What is 8*15?")).content)
# print ((llm.invoke("What is weather in chennai today?")).content)

#bind the lmm and the tools
Tools =[
    get_weather
 ]
llm_with_tools = llm.bind_tools(Tools)

# # user queries
# query1 = "what is the weather in chennai?"
# query2 = "what is RAG in AI?"


while True:
    user_query = input("Ask me something: ")
    if user_query.lower() == "exit":
        break

    # AIMessege
    response = llm_with_tools.invoke(user_query)

    if response.tool_calls:
        print(response.tool_calls)
        tool_result = None
        for tool_call in response.tool_calls:
            if(tool_call["name"] == "get_weather"):
                tool_result = get_weather.invoke(tool_call["args"])
                # print (tool_result+"")


        final_response = llm.invoke(f"""
                                    user asked: {user_query}
                                    Tool_result :{tool_result}
                                    Generate a final response to the user.                              
                                """)

    else:
        print(response.tool_calls)
        final_response = llm.invoke(f"""
                                    user asked: {user_query}
                                    Generate a final response to the user with examples.                              
                                """)
        
    print(final_response.content)
# print(get_weather.invoke("chennai"))

    
