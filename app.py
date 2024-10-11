import speech_recognition as sr
import os
import pyttsx3

# Inicializar el reconocedor de voz y el sintetizador de voz
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Captura de voz y ejecución de comandos
with sr.Microphone() as source:
    speak("Que hacemos hoy...")
    print("Que hacemos hoy...")
    audio = r.listen(source)
    
    try:
        command = r.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {command}")
        if "word" in command.lower():
            speak("Abriendo Word")
            os.system("start winword")
        elif "excel" in command.lower():
            speak("Abriendo Excel")
            os.system("start excel")
        elif "bloc de notas" in command.lower() or "notepad" in command.lower():
            speak("Abriendo Bloc de notas")
            os.system("start notepad")
        elif "cmd" in command.lower() or "símbolo del sistema" in command.lower():
            speak("Abriendo CMD")
            os.system("start cmd")
        elif "eclipse" in command.lower():
            speak("Abriendo Eclipse")
            os.system("start eclipse")
        elif "toad" in command.lower():
            speak("Abriendo Toad")
            os.system("start toad")
        elif "visual studio code" in command.lower() or "code" in command.lower():
            speak("Abriendo Visual Studio Code")
            os.system("start code")
        elif "google" in command.lower():
            speak("Abriendo Google")
            os.system("start chrome https://www.google.com")
        elif "github" in command.lower():
            speak("Abriendo GitHub")
            os.system("start chrome https://www.github.com")
        elif "amazon" in command.lower():
            speak("Abriendo Amazon")
            os.system("start chrome https://www.amazon.com")
        else:
            speak("Comando no reconocido")
    except sr.UnknownValueError:
        speak("No se entendió el comando")
