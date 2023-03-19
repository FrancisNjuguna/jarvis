import json
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is currently down.")
            return ""

def assistant(request):
    data = json.loads(request)
    command = data.get("command", "").lower()
    if "hello" in command:
        return "Hello there!"
    elif "goodbye" in command:
        return "Goodbye!"
    else:
        return "Sorry, I did not understand."

if __name__ == "__main__":
    request = input()
    response = assistant(request)
    print(response)
