import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function for speaking
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function for listening
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
        except sr.RequestError:
            print("Sorry, my speech service is currently down.")

# Define your voice assistant's behavior
def assistant():
    speak("Hello, I'm your voice assistant. How can I help you?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello there!")
        elif "goodbye" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I did not understand.")

# Start the voice assistant
assistant()

