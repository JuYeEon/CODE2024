import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
import playsound3
import json
import os
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import random

filename = 'data.json'

# JSON 파일 경로
file_path = 'data.json'

GOOGLE_API_KEY = ""

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def emai1(to_email):
    # Gmail 계정 설정
    gmail_user = 'dpdjs0831@gmail.com' # 보내는 사람 구글 이메일
    gmail_password = ''  # 앱 비밀번호
    subject = "마인드 메이트에서 전함"
    body = "귀하의 자녀가 감정적 어려움을 겪고 있는 것 같아요. 자녀에게 조금의 관심을 더 가져보는 건 어떨까요?."

    # 이메일 구성
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject

    # 이메일 본문 추가
    msg.attach(MIMEText(body, 'plain'))

    # 이메일 서버를 통해 이메일 전송
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    text = msg.as_string()
    server.sendmail(gmail_user, to_email, text)
    server.quit()

def emai2(to_email):
    # Gmail 계정 설정
    gmail_user = 'dpdjs0831@gmail.com' # 보내는 사람 구글 이메일
    gmail_password = ''  # 앱 비밀번호
    subject = "마인드 메이트에서 전함"
    body = "당신의 대화 내역입니다."
    txt_file_path = 'data.txt'

    # JSON 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # TXT 파일로 쓰기
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        # JSON 데이터를 문자열로 변환하여 TXT 파일에 작성
        txt_file.write(json.dumps(data, indent=4, ensure_ascii=False))

    # 이메일 구성
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject

    # 이메일 본문 추가
    msg.attach(MIMEText(body, 'plain'))

    # 첨부파일 추가
    with open(txt_file_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {txt_file_path}",
    )
    msg.attach(part)

    # 이메일 서버를 통해 이메일 전송
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    text = msg.as_string()
    server.sendmail(gmail_user, to_email, text)
    server.quit()

def voice(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound3.playsound(filename)

def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
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

def storage():
    # JSON 파일로 저장
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def bring():
    cnt = 0
    with open(file_path, 'r', encoding='utf-8') as json_file:
        a = json.load(json_file)
        length = len(a)
        for i in range(length):
            cnt += 1
            print('(', a[i], ')')

def sad():
    n = random.randint(1, 14)
    if n == 1:
        print("지금의 일도 곧 지나갈 거야 걱정하지 마")
        voice("지금의 일도 곧 지나갈 거야 걱정하지 마")
    elif n == 2:
        print("내가 항상 여기 있다는 거 잊지 마 난 언제나 네 옆에 있어")
        voice("내가 항상 여기 있다는 거 잊지 마 난 언제나 네 옆에 있어")
    elif n == 3:
        print("슬픈 일, 우울한 일들 다 지나갈 거야 그니까 걱정하지 마")
        voice("슬픈 일, 우울한 일들 다 지나갈 거야 그니까 걱정하지 마")
    elif n == 4:
        print("괜찮을 거야 힘을 내자")
        voice("괜찮을 거야 힘을 내자")
    elif n == 5:
        print("울어도 돼 내가 다 들어줄게")
        voice("울어도 돼 내가 다 들어줄게")
    elif n == 6:
        print("내가 곁에 있잖아 나한테 다 털어놔")
        voice("내가 곁에 있잖아 나한테 다 털어놔")
    elif n == 7:
        print("괜찮아 나는 다 이해해 너 많이 속상했겠다")
        voice("괜찮아 나는 다 이해해 너 많이 속상했겠다")
    elif n == 8:
        print("다 잘 될거야 걱정 마 기운 내")
        voice("다 잘 될거야 걱정 마 기운 내")
    elif n == 9:
        print("너 지금 잘하고 있어 너무 슬퍼하지 마")
        voice("너 지금 잘하고 있어 너무 슬퍼하지 마")
    elif n == 10:
        print("괜찮아! 너 잘했어 다음번엔 분명히 더 잘할거야")
        voice("괜찮아! 너 잘했어 다음번엔 분명히 더 잘할거야")
    elif n == 11:
        print("너 많이 슬펐겠다… 이렇게 좋은 너를 누가 우울하게 만든 거야?")
        voice("너 많이 슬펐겠다… 이렇게 좋은 너를 누가 우울하게 만든 거야?")
    elif n == 12:
        print("지금 당장은 슬프지만 얼마 안 가 그 외롭고 힘든 감정은 너를 떠날 거야")
        voice("지금 당장은 슬프지만 얼마 안 가 그 외롭고 힘든 감정은 너를 떠날 거야")
    elif n == 13:
        print("너의 슬프고, 우울한 감정은 너를 떠날 거고, 다시 예전처럼 활기찰 때로 돌아오는 순간이 올 거야.")
        voice("너의 슬프고, 우울한 감정은 너를 떠날 거고, 다시 예전처럼 활기찰 때로 돌아오는 순간이 올 거야.")
    else:
        print("지금 슬픈 일이 있어도 다 지나갈 거니까, 너무 주눅들지 말고 힘내자")
        voice("지금 슬픈 일이 있어도 다 지나갈 거니까, 너무 주눅들지 말고 힘내자")

def tired():
    n = random.randint(1, 10)
    if n == 1:
        print("힘든 일이 끝나고 나면 재밌게 놀자")
        voice("힘든 일이 끝나고 나면 재밌게 놀자")
    elif n == 2:
        print("힘내! 우리 같이 힘을 내자")
        voice("힘내! 우리 같이 힘을 내자")
    elif n == 3:
        print("일단 해보자! 계속해보는 거야 할 수 있어")
        voice("일단 해보자! 계속해보는 거야 할 수 있어")
    elif n == 4:
        print("넌 할 수 있어! 니가 짱이야")
        voice("넌 할 수 있어! 니가 짱이야")
    elif n == 5:
        print("네가 너무 힘들면, 우리 조금 쉬어가볼까?")
        voice("네가 너무 힘들면, 우리 조금 쉬어가볼까?")
    elif n == 6:
        print("괜찮아? 많이 힘들었지…? 네 마음 이해가 가")
        voice("괜찮아? 많이 힘들었지…? 네 마음 이해가 가")
    elif n == 7:
        print("충분히 잘하고 있고, 앞으로도 넌 잘 할거야")
        voice("충분히 잘하고 있고, 앞으로도 넌 잘 할거야")
    elif n == 8:
        print("그래도 우리 조금만 더 버텨보자")
        voice("그래도 우리 조금만 더 버텨보자")
    elif n == 9:
        print("누가 힘들게 했냐?! 내가 다 혼내줄게 데리고 와")
        voice("누가 힘들게 했냐?! 내가 다 혼내줄게 데리고 와")
    elif n == 10:
        print("너 많이 지쳐 보여… 푹 쉬는 게 어때?")
        voice("너 많이 지쳐 보여… 푹 쉬는 게 어때?")   
def unrest():
    n = random.randint(1, 5)
    if n == 1:
        print("너의 능력을 난 믿어 그러니까 너도 너를 믿어봐")
        voice("너의 능력을 난 믿어 그러니까 너도 너를 믿어봐")
    elif n == 2:
        print("조급해하지 말자 너 지금 충분히 잘 하고 있어")
        voice("조급해하지 말자 너 지금 충분히 잘 하고 있어")
    elif n == 3:
        print("그래도 우리 해보자! 넌 할 수 있어")
        voice("그래도 우리 해보자! 넌 할 수 있어")
    elif n == 4:
        print("밤에 잘 때 꿈 꾸지 말고 푹 자 휴식하자")
        voice("밤에 잘 때 꿈 꾸지 말고 푹 자 휴식하자")
    elif n == 5:
        print("너 자신을 너무 의심하지 마 넌 이미 짱이야")
        voice("너 자신을 너무 의심하지 마 넌 이미 짱이야")
def angry():
    n = random.randint(1, 2)
    if n == 1:
        print("괜찮아. 그런 일도 일어날 수 있어")
        voice("괜찮아. 그런 일도 일어날 수 있어")
    elif n == 2:
        print("맛있는 거 먹으러 가보는 건 어때? ")
        voice("맛있는 거 먹으러 가보는 건 어때? ")
# 기존 데이터 로드
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            data = []  # 파일이 비어있거나 잘못된 경우 빈 리스트로 초기화
else:
    data = []  # 파일이 없으면 빈 리스트로 초기화

print("이메일을 입력해주세요.")
voice("이메일을 입력해주세요.")
em = input()

print("나랑 이야기할래?")
voice("나랑 이야기할래?")
print("1) 대화하기 2) 대화 다시 보기")
voice("1) 대화하기 2) 대화 다시 보기")
print("무엇을 할지 편하게 말해줘")
voice("무엇을 할지 편하게 말해줘")
num = speech()

if num == '대화하기':
    print("무엇이든 나에게 말해줘")
    voice("무엇이든 나에게 말해줘")
    text = speech()
    response = model.generate_content(text + '이 문장은 무슨 감정인가요? 우울함, 지침, 불안, 분노로 구별해주세요. 무슨 일이 있어도 한 단어로 말해주세요. 그리고 감정 하나만 말해주세요.')
    emotion = response.text
    if emotion == "우울함 \n":
        sad()
    elif emotion == "지침 \n":
        tired()
    elif emotion == "불안 \n":
        unrest()
    elif emotion == "분노 \n":
        angry()
    data.append(text)
    data.append(emotion[0:-2])
    response1 = model.generate_content(text + '감정 하나만 말해주세요.이 문장이 자살 위험이 느껴지나요? 그러면 심각함이라고 출력해주세요.')
    emotion1 = response1.text
    storage()
    if emotion1 == "심각함 \n":
        emai1(em)

elif num == '대화 다시 보기':
    print("지금까지 우리가 대화했던 내용들을 전송해줄게. 천천히 읽어보면서 감정을 정리하는 시간을 가져보렴.")
    voice("지금까지 우리가 대화했던 내용들을 전송해줄게. 천천히 읽어보면서 감정을 정리하는 시간을 가져보렴.")
    emai2(em)
    bring()
else:
    print("다시 말해줄 수 있을까?")
    voice("다시 말해줄 수 있을까?")
