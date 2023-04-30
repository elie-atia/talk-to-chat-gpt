from dotenv import load_dotenv
import os
import openai

class GPTAssistant:
    def __init__(self):
        load_dotenv() # Load environment variables from .env file
        api_key = os.getenv("API_KEY") # Access the loaded environment variable
        openai.api_key = api_key

    def talk_with(self, persona, tell_user, ask_user):
        message_history = []
        while True:
            user_input = ask_user()
            print(user_input)
            if user_input == "" or user_input == None:
                return message_history

            message_history.append({"role": "user", "content": user_input})
            query = [{"role": "system", "content": persona}]
            query.extend(message_history)
            result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=query,
            max_tokens=300

            )
            gpt_message = result["choices"][0]["message"]
            message_history.append({"role": gpt_message["role"], "content": gpt_message["content"]})
            tell_user("GPT: " + gpt_message["content"])