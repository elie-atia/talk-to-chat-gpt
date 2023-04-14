import speech_recognition as sr

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



if __name__ == "__main__":
    voice_to_text()

    
