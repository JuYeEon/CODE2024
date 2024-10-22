import playsound3
import gtts

def voice(text):
    tts = gtts.gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound3.playsound(filename)

voice("안녕하세요")
