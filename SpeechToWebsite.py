import speech_recognition as sr
import webbrowser as wb
r=sr.Recognizer()

with sr.Microphone() as source:
    print('Ask for a website to open')
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("You asked for : {}".format(text)+" website")
        if('.com' in text):
            wb.open('http://'+text)
        else:
            wb.open('http://'+text+'.com')
    except:
        print("Couldn't recognize your voice")
