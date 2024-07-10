import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
r= sr.Recognizer()
engine = pyttsx3.init('sapi5')




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=6 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("i m friday, please tell me how can i help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    with sr.Microphone() as source:


        try:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")

        except:
            # print(e)
            print("Say that again plaese...")
            return "None"
        return query


if  __name__ == "_main_":
    wishMe()
    while True:
        query = takeCommand().lower()
# logic for executing task based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)