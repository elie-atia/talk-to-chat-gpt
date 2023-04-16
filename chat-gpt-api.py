import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Accéder à la variable d'environnement chargée
api_key = os.getenv("API_KEY")

openai.api_key = api_key

def talk_with(persona, tell_user, ask_user):
    message_history = []
    while True:
        user_input = ask_user()
        if user_input == "":
            return message_history

        message_history.append({"role": "user", "content": user_input})
        query = [{"role": "system", "content": persona}]
        query.extend(message_history)
        result = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=query,
          max_tokens=30

        )
        gpt_message = result["choices"][0]["message"]
        message_history.append({"role": gpt_message["role"], "content": gpt_message["content"]})
        tell_user("GPT: " + gpt_message["content"])


talk_with(
    persona="""Comportez vous comme quelqun de tres naif et simple. Et repond moi en francais""",
    tell_user=print,
    ask_user=input
)

