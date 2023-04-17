import speech_recognition as sr
import pyttsx3
import openai
from dotenv import load_dotenv
import os
import threading
import time
import numpy as np
import queue

r = sr.Recognizer()

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Accéder à la variable d'environnement chargée
api_key = os.getenv("API_KEY")

openai.api_key = api_key








def record_voice():
    r = sr.Recognizer()
    audio_queue = queue.Queue()
    recording = True

    silence_threshold = 5  # en secondes
    silence_window = 1  # en secondes
    silence_time = 0

    def is_silent(audio_data, threshold=-50):
        audio_samples = np.frombuffer(audio_data, dtype=np.int16)
        return np.mean(audio_samples) < threshold

    def record_audio():
        nonlocal silence_time
        with sr.Microphone() as src:
            r.adjust_for_ambient_noise(src, duration=0.5)
            sample_rate = src.SAMPLE_RATE
            sample_width = src.SAMPLE_WIDTH
            audio_queue.put((sample_rate, sample_width))

            while recording:
                try:
                    temp_audio = r.listen(src, timeout=silence_window)
                    if is_silent(temp_audio.get_raw_data()):
                        silence_time += silence_window
                    else:
                        silence_time = 0
                        audio_queue.put(temp_audio.get_raw_data())
                    if silence_time >= silence_threshold:
                        break
                except sr.WaitTimeoutError:
                    break

    print("Parlez maintenant...")
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()

    try:
        recording_thread.join()
    except KeyboardInterrupt:
        recording = False
        recording_thread.join()

    print("Enregistrement terminé.")
    sample_rate, sample_width = audio_queue.get()
    audio_data = bytearray()
    while not audio_queue.empty():
        audio_data += audio_queue.get()
    return sr.AudioData(audio_data, sample_rate, sample_width)














def voice_to_text():
    # print("Combien de temps voulez vous que l'enregistement dure (en seconde)?")
    # duration = input()
    audio = record_voice()

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



if __name__ == "__main__":
    # text = voice_to_text()
    # text = "Bonjour, comment allez-vous ?"
    talk_with(
        persona="""Repond moi en francais, avec des reponses courtes et precises.""",
        tell_user=text_to_voice,
        ask_user=voice_to_text
    )
    # text_to_voice(text)


    
