from faster_whisper import WhisperModel
import ffmpeg
import os

def extract_audio(input_file, output_file="temp_audio.wav"):
    """
    Extrae el audio de cualquier archivo de video usando FFmpeg.
    """
    (
        ffmpeg
        .input(input_file)
        .output(output_file, ac=1, ar="16000")
        .overwrite_output()
        .run(quiet=True)
    )
    return output_file


def transcribe_audio(audio_path, model_size="small"):
    """
    Transcribe audio y detecta idioma automáticamente.
    """
    print("Cargando modelo Whisper...")
    model = WhisperModel(model_size, device="cpu", compute_type="float32")

    print("Transcribiendo audio...")
    segments, info = model.transcribe(audio_path, beam_size=5)

    print(f"Idioma detectado: {info.language}")

    text = ""
    for seg in segments:
        text += seg.text + " "

    return text.strip()


def convert_media_to_text(file_path):
    """
    Función principal que convierte cualquier audio/video a texto.
    """
    print("Extrayendo audio...")
    audio = extract_audio(file_path)

    text = transcribe_audio(audio)

    os.remove(audio)  # Limpia el archivo temporal

    return text


if __name__ == "__main__":
    ruta = input("Ingresa la ruta del archivo de audio o video: ")
    resultado = convert_media_to_text(ruta)

    print("\n===== RESULTADO =====\n")
    print(resultado)
