# Talk-to-chat-gpt

The purpose of this project is to communicate with ChatGPT.  
The program transcribes your voice into text and sends it to ChatGPT through an API.  
The response from ChatGPT is then transformed back into speech.

## Installation

Create a virtual environment using `python -m venv ./my_venv`.

Activate the virtual environment using `.\my_venv\Scripts\activate` (for Windows)  
or `source ./my_venv/bin/activate` (for Linux/Mac).

Install the required packages using `pip install -r requirements.txt`.

Put your API-KEY in the .`env` file.

## Usage

run this command: `python ./main.py`

## Examples


## Credits

This project uses the OpenAI API to generate chatbot responses.  
To learn more about OpenAI, visit their website: https://openai.com/.

It also uses the following libraries:  

  -`speech_recognition` for speech recognition  
  -`pyttsx3` for text-to-speech conversion  

To learn more about these libraries, please visit their respective websites.

## Références

- [ChatGPT API with Python](https://www.mikulskibartosz.name/chatgpt-api-with-python/)


To learn more about these libraries, please visit their respective websites.

## Documentation

# ChatGPT API
The API uses the entire chat history to generate the next message every time.  
The API returns only the next message, so we must keep the history of messages ourselves if we want to implement a longer interaction.

Each message is a chat interaction:
  - `system`: to specify the context  
  - `user`: the message I sent  
  - `assistant`: the model's response (for in-context-learning, we can provide them)  
