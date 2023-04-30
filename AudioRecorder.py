import speech_recognition as sr
import queue
import numpy as np
import threading

class AudioRecorder:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio_queue = queue.Queue()
        self.recording = True
        self.silence_threshold = 5  # in seconds
        self.silence_window = 1  # in seconds
        self.silence_time = 0

    def is_silent(self, audio_data, threshold=-50):
        audio_samples = np.frombuffer(audio_data, dtype=np.int16)
        return np.mean(audio_samples) < threshold

    def record_audio(self):
        silence_time = 0
        with sr.Microphone() as src:
            self.r.adjust_for_ambient_noise(src, duration=0.5)
            sample_rate = src.SAMPLE_RATE
            sample_width = src.SAMPLE_WIDTH
            self.audio_queue.put((sample_rate, sample_width))

            while self.recording:
                try:
                    temp_audio = self.r.listen(src, timeout=self.silence_window)
                    if self.is_silent(temp_audio.get_raw_data()):
                        silence_time += self.silence_window
                    else:
                        silence_time = 0
                        self.audio_queue.put(temp_audio.get_raw_data())
                    if silence_time >= self.silence_threshold:
                        break
                except sr.WaitTimeoutError:
                    break

    def record_voice(self):
        print("Parlez maintenant...")
        recording_thread = threading.Thread(target=self.record_audio)
        recording_thread.start()

        try:
            recording_thread.join()
        except KeyboardInterrupt:
            self.recording = False
            recording_thread.join()

        print("Enregistrement terminé.")
        sample_rate, sample_width = self.audio_queue.get()
        audio_data = bytearray()
        while not self.audio_queue.empty():
            audio_data += self.audio_queue.get()
        return sr.AudioData(audio_data, sample_rate, sample_width)


    def voice_to_text(self):
        audio = self.record_voice()

        try:
            text = self.r.recognize_google(audio, language='fr-FR')
            print("Texte transcrit: " + text)
            return text
        except sr.UnknownValueError:
            print("Je n'ai pas compris ce que vous avez dit.")
        except sr.RequestError as e:
            print("Erreur lors de la récupération des résultats depuis Google Speech Recognition service; {0}".format(e))

