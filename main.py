from AudioRecorder import AudioRecorder
from TextToSpeech import TextToSpeech
from GPTAssistant import GPTAssistant


if __name__ == "__main__":
    audio_recorder = AudioRecorder()
    tts = TextToSpeech()
    gpt_assistant = GPTAssistant()

    gpt_assistant.talk_with(
        persona="""Repond moi en francais, avec des reponses courtes et precises.""",
        ask_user=audio_recorder.voice_to_text,
        tell_user=tts.text_to_voice,
    )
