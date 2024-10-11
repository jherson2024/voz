import speech_recognition as sr
import pyttsx3

# Inicializar el reconocedor de voz y el sintetizador de voz
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Elegir el micrófono correcto (reemplaza el índice por el que corresponda en tu caso)
mic_index = 1  # Aquí pones el índice del micrófono que quieras usar
mic = sr.Microphone(device_index=mic_index)

# Captura de voz y ejecución de comandos
with mic as source:
    r.adjust_for_ambient_noise(source)  # Ajusta a los ruidos ambientales
    speak("Por favor, di algo...")
    print("Por favor, di algo...")
    
    # Escuchar el audio
    audio = r.listen(source)
    
    try:
        # Reconocer el audio y convertirlo a texto
        command = r.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {command}")
    
    except sr.UnknownValueError:
        # Si no se reconoce el audio
        print("No se pudo entender lo que dijiste")
    
    except sr.RequestError as e:
        # Si hay un problema con el servicio de reconocimiento
        print(f"Error al solicitar resultados del servicio de reconocimiento de voz; {e}")