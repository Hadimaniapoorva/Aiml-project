import speech_recognition as sr
import webbrowser
import aiml
import pyttsx3

# Initialize the AIML kernel
kernel = aiml.Kernel()

# Load AIML files
kernel.learn("path_to_your_aiml_file.aiml")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Check available voices and select one
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}, ID: {voice.id}")

# Optionally, set a specific voice if needed
# engine.setProperty('voice', voices[0].id)  # Example: Setting the first voice

# Initialize the speech recognizer
recognizer = sr.Recognizer()

def speak(text):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print("User said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down")
            return None

def perform_task(command):
    if 'open google' in command:
        print("Opening Google...")
        webbrowser.open('https://www.google.com')
        speak("Opening Google")
    elif 'open youtube' in command:
        print("Opening YouTube...")
        webbrowser.open('https://www.youtube.com')
        speak("Opening YouTube")
    elif 'open gmail' in command:
        print("Opening Gmail...")
        webbrowser.open('https://mail.google.com')
        speak("Opening Gmail")
    elif 'open facebook' in command:
        print("Opening Facebook...")
        webbrowser.open('https://www.facebook.com')
        speak("Opening Facebook")
    else:
        response = kernel.respond(command)
        print("Assistant:", response)
        speak(command)

if __name__ == "__main__":
    stop_commands = ["exit", "quit", "goodbye"]
    while True:
        command = listen()
        if command:
            if any(stop_command in command for stop_command in stop_commands):
                print("Assistant: Goodbye!")
                speak("Goodbye!")
                break
            perform_task(command)
