from config import OPENAI_API_KEY
import openai
from tools import calculator_tool
from tools import get_current_time_by_city
from tools import web_search

functions = [
    {
        "name": "calculator_tool",
        "description": "Safely evaluate a math expression",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Math expression like '2 + 3 * 4' or 'sqrt(16)'"
                }
            },
            "required": ["expression"]
        }
    },
    {
        "name": "get_current_time_by_city",
        "description": "Get current time in a given city or timezone",
        "parameters": {
            "type": "object",
            "properties": {
                "city_or_timezone": {
                    "type": "string",
                    "description": "City or timezone string, like 'Tokyo' or 'UTC'"
                }
            },
            "required": ["city_or_timezone"]
        }
    },
    {
        "name": "web_search",
        "description": "Search the web for general information",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query like 'Python tutorials' or 'AI news'"
                },
                "num_results": {
                    "type": "integer",
                    "description": "Number of results to return (1–5)",
                    "default": 3
                }
            },
            "required": ["query"]
        }
    }
]


client = openai.OpenAI(api_key=OPENAI_API_KEY)

def chat_with_openai(message, chat_history):
    try:
        chat_history.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0613",  # supports function calling
            messages=chat_history,
            tools=functions,
            tool_choice="auto"
        )

        response_message = response.choices[0].message

        # If tool call is triggered
        if response_message.tool_calls:
            tool_call = response_message.tool_calls[0]
            function_name = tool_call.function.name
            arguments = eval(tool_call.function.arguments)  

            # Call corresponding tool
            if function_name == "calculator_tool":
                tool_result = calculator_tool(arguments['expression'])
            elif function_name == "get_current_time_by_city":
                tool_result = get_current_time_by_city(arguments['city_or_timezone'])
            elif function_name == "web_search":
                tool_result = web_search(arguments['query'], arguments.get("num_results", 3))
            else:
                tool_result = "❌ Unknown tool."

            # Send tool result back to GPT for final response
            chat_history.append({
                "role": "assistant",
                "tool_calls": [tool_call]
            })
            chat_history.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": tool_result
            })

            # Re-ask GPT with the tool result
            final_response = client.chat.completions.create(
                model="gpt-3.5-turbo-0613",
                messages=chat_history,
            )

            return final_response.choices[0].message.content
        return response_message.content

    except Exception as e:
        return f"❌ Error: {str(e)}"    

if __name__ == "__main__":
    print("🧠 Your bot says hi - Ready! Type 'exit' to quit.")
    history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        result = chat_with_openai(user_input, history)
        
        #result = web_search(user_input)
                                 
        print("GPT:", result)
