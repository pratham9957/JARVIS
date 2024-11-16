import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice input from the user
def listen_command():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        speak("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the service.")
        speak("Sorry, I'm having trouble connecting to the service.")
        return ""

# Main function
def main():
    speak("Hello, I am your assistant. How can I help you today?")
    
    while True:
        command = listen_command()
        
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}.")
        
        elif "open youtube" in command:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
        
        elif "open google" in command:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        
        elif "play music" in command:
            # Change this to a path to your music file or YouTube link
            music_path = "/path/to/your/music/file.mp3"
            if os.path.exists(music_path):
                os.system(f"start {music_path}")
                speak("Playing music now.")
            else:
                speak("Sorry, I couldn't find the music file.")
        
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't quite catch that. Can you please repeat?")
        
if __name__ == "__main__":
    main()
