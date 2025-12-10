# {} [ ] \
import speech_recognition as sr

filename ="audio_file.wav"
output_txt ="transcription.txt"

r = sr.Recognizer()

try:
    with sr.AudioFile(filename) as source:
        duration = int(source.DURATION)
        fill_transcription = ""
        print ("Procesando el archivo de audio...")
        for i in range(0, duration, 10):
            try:
                audio_data = r.record(source, duration = 10)
                text = r.recognize_google(audio_data, lenguage="es-ES")
                full_transcription += text + "\n"
                print(f"Fragmento {i// 10 + 1} : {text}")
            except sr.UnknownValueError:
                print(f"Fragmento {i // 10 + 1}: No se pudo entender el audio " )
                full_transcription +="[No se pudo entender el audio]\n"
            except sr.RequestError as e:
                print(f"Error al comunicarse con el servidor de google: {e} ")
                break
        wite open (output_txt, "w", encoding=ut)