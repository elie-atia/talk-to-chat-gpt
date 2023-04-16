import speech_recognition as sr
import pyttsx3
import openai
from dotenv import load_dotenv
import os

r = sr.Recognizer()

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Accéder à la variable d'environnement chargée
api_key = os.getenv("API_KEY")

openai.api_key = api_key

def record_voice(duration):

    with sr.Microphone() as source:
        print("Parlez maintenant...")
        audio = r.record(source, duration=int(duration))
        print("Enregistrement terminé.")
    
    return audio


def voice_to_text():
    print("Combien de temps voulez vous que l'enregistement dure (en seconde)?")
    duration = input()
    audio = record_voice(duration)

    try:
        text = r.recognize_google(audio, language='fr-FR')
        print("Texte transcrit: " + text)
        return text
    except sr.UnknownValueError:
        print("Je n'ai pas compris ce que vous avez dit.")
    except sr.RequestError as e:
        print("Erreur lors de la récupération des résultats depuis Google Speech Recognition service; {0}".format(e))



def text_to_voice(text):
    # Initialisation du moteur de synthèse vocale
    engine = pyttsx3.init()

    # Récupération des voix installées
    voices = engine.getProperty('voices')

    # Configuration de la voix française
    for voice in voices:
        if voice.name == 'Microsoft Hortense Desktop - French':
            engine.setProperty('voice', voice.id)

    engine.say(text)
    engine.runAndWait()

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
          max_tokens=300

        )
        gpt_message = result["choices"][0]["message"]
        message_history.append({"role": gpt_message["role"], "content": gpt_message["content"]})
        tell_user("GPT: " + gpt_message["content"])



if __name__ == "__main__":
    # text = voice_to_text()
    # text = "Bonjour, comment allez-vous ?"
    talk_with(
        persona="""Repond moi en francais, avec des reponses courtes et precises.""",
        tell_user=text_to_voice,
        ask_user=voice_to_text
    )
    # text_to_voice(text)


    
