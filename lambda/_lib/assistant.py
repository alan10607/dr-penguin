import os
import time
import json
from openai import OpenAI
from functions import Functions
    
class ChatAI:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), timeout=600)
        self.assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
        self.thread = self.client.beta.threads.create()
        func = Functions(self.client)
        self.tools = [
            func.google_search, 
            func.dalle3_image_generator
        ]

    def run(self, question):
        client = self.client
        assistant_id = self.assistant_id
        thread = self.thread

        # 1. Prepare user question message
        message = client.beta.threads.messages.create(
            thread_id = thread.id,
            role = "user",
            content = question
        )

        # 2. Create a new run
        run = client.beta.threads.runs.create(
            thread_id = thread.id,
            assistant_id = assistant_id,
        )

        
        while True:
            print("Run status: " + run.status)
            if run.status not in ["queued", "in_progress", "requires_action"]:
                break

            if run.status in ["queued", "in_progress"]:
                # 3. Wait for message retrieval
                run = client.beta.threads.runs.retrieve(
                    thread_id = thread.id,
                    run_id = run.id
                )
                time.sleep(1)
                

            elif run.status == "requires_action":
                # 4. Submit tool outputs
                tool_outputs = self.process_tools(run)

                run = client.beta.threads.runs.submit_tool_outputs(
                    thread_id = thread.id,
                    run_id = run.id,
                    tool_outputs = tool_outputs
                )

            elif run.status == "failed":
                raise Exception("Run Failed. Error: ", run.last_error)
            
                
        # 5. Return the result message
        result = self.get_message()
        return result

    def get_message(self):
        messages = self.client.beta.threads.messages.list(
            thread_id = self.thread.id
        )
        return messages.data[0].content[0].text.value or "<no message>"

    def process_tools(self, run):
        tool_calls = run.required_action.submit_tool_outputs.tool_calls
        tool_outputs = []

        for tool_call in tool_calls:
            function = self.find_matching_function(tool_call.function.name)
            output = self.execute_function(function, tool_call.function.arguments)
            print(f"{tool_call.function.name}: ", tool_call.function.arguments, "=>", output)

            tool_outputs.append(
                {
                    "tool_call_id": tool_call.id,
                    "output": json.dumps(output)
                }
            )

        return tool_outputs

    def find_matching_function(self, function_name):
        return next((func for func in self.tools if func.__name__ == function_name))

    def execute_function(self, function, arguments):
        try:
            return function(**eval(arguments))
        except Exception as e:
            return "Execute function error: " + str(e)
        


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    ai = ChatAI()

    print("Type 'quit' to quit chat")
    while True:
        question = input("Question >>> ")
        if question.lower() == "quit":
            print("Quit chat...")
            break
        
        result = ai.run(question)
        print(f"Answer >>>  {result}")
        print("-----------------\n")

