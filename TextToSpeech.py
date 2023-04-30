import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init() # Initialization of the speech synthesis engine

    def configure_voice(self):
        # Recovery of installed voices
        voices = self.engine.getProperty('voices')

        # French voice configuration
        for voice in voices:
            if voice.name == 'Microsoft Hortense Desktop - French':
                self.engine.setProperty('voice', voice.id)


    def text_to_voice(self, text):
        self.engine.say(text)
        self.engine.runAndWait()