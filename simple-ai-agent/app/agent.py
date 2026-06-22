from tools import get_weather, get_gold_price
from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(groq_api_key = GROQ_API_KEY,
            #    model="llama-3.1-8b-instant",
            model="llama-3.3-70b-versatile",
               temperature =0)



#bind the lmm and the tools
Tools =[
    get_weather,
    get_gold_price
 ]
llm_with_tools = llm.bind_tools(Tools)


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
                

            elif(tool_call["name"] == "get_gold_price"):
                tool_result = get_gold_price.invoke(tool_call["args"])
                print(tool_result)

        final_response = llm.invoke(f"""
                                    user asked: {user_query}
                                    Tool_result :{tool_result}
                                    Generate a final response to the user.                              
                                """)

    else:
        # print(response)
        final_response = response
        
    print(final_response.content)


    
