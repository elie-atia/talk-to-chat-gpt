import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Accéder à la variable d'environnement chargée
api_key = os.getenv("API_KEY")

openai.api_key = api_key

query = [
    {"role": "system", "content": "You are a MySQL database. Return responses in the same format as MySQL."},
    {"role": "user", "content": "insert into users(name, email) values ('John', 'john@galt.example');"},
    {"role": "user", "content": "select count(*) from users"}
]

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=query
)


message_content = response.choices[0].message.content
print(message_content)
