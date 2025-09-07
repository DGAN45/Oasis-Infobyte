import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import sys

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speaking speed

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source) 

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there is a network issue.")
            return ""

def respond(command):
    if "hello" in command:
        speak("Hi! How can I help you?")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
    elif "date" in command:
        date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {date}")
    elif "search" in command:
        topic = command.replace("search", "")
        speak(f"Searching for {topic}")
        pywhatkit.search(topic)
    elif "open youtube" in command:
        speak("Opening YouTube")
        pywhatkit.playonyt("YouTube")
    elif "open google" in command:
        speak("Opening Google")
        pywhatkit.search("Google")
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        engine.stop()  
        sys.exit()
    else:
        speak("I didn't understand. Please try again.")

def main():
    speak("Voice Assistant Activated")
    while True:
        command = listen()
        if command:
            respond(command)

main()
