import speech_recognition as sr
import pyttsx3

def voice_to_text():
    r = sr.Recognizer()

    print("Combien de temps voulez vous que l'enregistement dure (en seconde)?")
    duration = input()

    with sr.Microphone() as source:
        print("Parlez maintenant...")
        audio = r.record(source, duration=int(duration))
        print("Enregistrement terminé.")

    try:
        text = r.recognize_google(audio, language='fr-FR')
        print("Texte transcrit: " + text)
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


if __name__ == "__main__":
    # voice_to_text()
    text = "Bonjour, comment allez-vous ?"
    text_to_voice(text)
    print("main called")

    
