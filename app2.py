import speech_recognition as sr
import os
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar el reconocedor de voz y el sintetizador de voz
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def leer_tarea():
    # Configuración del webdriver (Chrome en este caso)
    driver = webdriver.Chrome()  # Si el ChromeDriver no está en el PATH, proporciona la ruta completa aquí.
    
    # Abrir el enlace de la plataforma UNSA
    driver.get("https://aulavirtual.unsa.edu.pe/2024B/my/")
    
    # Esperar unos segundos para que cargue la página
    time.sleep(5)

    # Intentar extraer el contenido de la tarea
    try:
        # Usamos XPath para encontrar el evento del 17 de octubre
        tarea = driver.find_element(By.XPATH, "//span[contains(text(), 'Vencimiento de Enviar Practica 3')]").text
        speak(f"La tarea para hoy es: {tarea}")
    except Exception as e:
        speak("No se encontró la tarea o hubo un error.")
        print(e)
    
    # Cerrar el navegador
    driver.quit()

# Captura de voz y ejecución de comandos
with sr.Microphone() as source:
    speak("Di un comando...")
    print("Di un comando...")
    audio = r.listen(source)
    
    try:
        command = r.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {command}")
        
        if "tareas" in command.lower() or "qué tareas tengo hoy" in command.lower():
            speak("Abriendo la plataforma y verificando las tareas...")
            leer_tarea()
        
        else:
            speak("Comando no reconocido")
    except sr.UnknownValueError:
        speak("No se entendió el comando")
