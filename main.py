import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Parlez maintenant...")
    audio = r.record(source, duration=5)
    print("Enregistrement terminé.")

try:
    text = r.recognize_google(audio, language='fr-FR')
    print("Texte transcrit: " + text)
except sr.UnknownValueError:
    print("Je n'ai pas compris ce que vous avez dit.")
except sr.RequestError as e:
    print("Erreur lors de la récupération des résultats depuis Google Speech Recognition service; {0}".format(e))
