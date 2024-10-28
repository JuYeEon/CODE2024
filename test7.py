import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
import playsound3
import json
import os
import requests

GOOGLE_API_KEY = ""

def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("듣고 있어요")
        audio = r.listen(source) #마이크로부터 음성 듣기

    try:
        #구글 API 로 인식
        text = r.recognize_google(audio, language = 'ko')
        print(text)
        return text

    except sr.UnknownValueError:
        print('인식 실패') #음성 인식 실패한 경우
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e)) #API Key 오류, 네트워크 단절 등


genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') 

text = speech()

response = model.generate_content(text)

print(response.text)
