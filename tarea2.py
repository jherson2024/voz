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
    # Conectar a Chrome en modo de depuración remota
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")  # Conectarse a Chrome en modo de depuración

    driver = webdriver.Chrome(options=options)
    
    # La URL de la plataforma UNSA
    url = "https://aulavirtual.unsa.edu.pe/2024B/my/"
    
    # Variable para saber si encontramos la pestaña
    found_tab = False
    
    # Iterar sobre las ventanas y verificar si la pestaña ya está abierta
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if driver.current_url == url:
            found_tab = True
            break
    
    # Si no se encontró la pestaña, abrirla
    if not found_tab:
        driver.get(url)

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
    
    # No cerrar el navegador
    # driver.quit()  # Puedes comentar esta línea si quieres mantener la ventana abierta

# Captura de voz y ejecución de comandos utilizando el micrófono con índice 1
with sr.Microphone(device_index=1) as source:
    speak("Di un comando...")
    print("Di un comando...")
    audio = r.listen(source)
    
    try:
        command = r.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {command}")
        
        if "tareas" in command.lower() or "qué tareas tengo hoy" in command.lower():
            speak("Verificando las tareas...")
            leer_tarea()
        
        else:
            speak("Comando no reconocido")
    except sr.UnknownValueError:
        speak("No se entendió el comando")
