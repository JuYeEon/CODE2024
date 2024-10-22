import speech_recognition as sr
from gtts import gTTS
import playsound3
import json
import os
import requests

filename = 'data.json'

# JSON 파일 경로
file_path = 'data.json'

def classify(text):
    key = "3f639840-8e0f-11ef-b63d-5157506f1f968430c501-f870-4fb4-930c-980bfa33a8ec"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def voice(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound3.playsound(filename)

# 기존 데이터 로드
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            data = []  # 파일이 비어있거나 잘못된 경우 빈 리스트로 초기화
else:
    data = []  # 파일이 없으면 빈 리스트로 초기화


r = sr.Recognizer()
with sr.Microphone() as source:
    voice("듣고 있어요")
    print("듣고 있어요")
    audio = r.listen(source) #마이크로부터 음성 듣기

try:
    #구글 API 로 인식
    text = r.recognize_google(audio, language = 'ko')
    print(text)
    data.append(text)
    demo = classify(text)
    label = demo["class_name"]
    data.append(label)

except sr.UnknownValueError:
    print('인식 실패') #음성 인식 실패한 경우
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e)) #API Key 오류, 네트워크 단절 등

# JSON 파일로 저장
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

with open(file_path, 'r', encoding='utf-8') as json_file:
    a = json.load(json_file)

ad = len(a)

cnt = 0
for i in range(ad):
    cnt += 1
    print(a[i], end = ' ')
    if cnt % 2 == 0:
        print()
