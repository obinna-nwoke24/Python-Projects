import speech_recognition as sr
import pyttsx3
import speech_recognition.exceptions

r = sr.Recognizer()


def SpeakText(command):
    """
    SpeakText takes the text as a command and speaks out loud the result
    :param command: a text value
    :return:
    """
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def run():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)

            myText = r.recognize_google(audio2)
            myText = myText.lower()

            print("--- audio transcript ---\n" + myText)
            SpeakText(myText)
    except speech_recognition.exceptions.UnknownValueError as e:
        print("Audio not recorded")


run()
