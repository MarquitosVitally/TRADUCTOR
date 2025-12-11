# {} [ ] \
import speech_recognition as sr

filename = "C:\Users\marqu\Documents\TRADUCTOR\SRC\audio\audio_utils.py"
output_txt ="transcription.txt"

r = sr.Recognizer()

try:
    with sr.AudioFile(filename) as source:
        print("Procesando el archivo de audio...")
        audio_data = r.record(source)  # <<-- CORREGIDO: leer todo el audio

        try:
            text = r.recognize_google(audio_data, language="es-ES")
        except sr.UnknownValueError:
            text = "[No se pudo entender el audio]"
        except sr.RequestError as e:
            text = f"[Error conectando con Google: {e}]"

        with open(output_txt, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Transcripción completada y guardada en {output_txt}")

except FileNotFoundError:
    print(f"El archivo {filename} no se encontró. Asegúrate de que esté en la carpeta correcta.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
