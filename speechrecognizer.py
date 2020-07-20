import speechrecognizer as sr

def getStringOutVoive():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text
        except:
            return "Sorry couldn't understand you"
