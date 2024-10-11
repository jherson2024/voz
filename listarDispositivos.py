import speech_recognition as sr

# Listar todos los micrófonos disponibles
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with index {index}: {name}")
