from pydub import AudioSegment

AudioSegment.from_file("WhatsApp Ptt 2025-11-06 at 8.59.53 PM.wav").export(
    "audio_file.wav", format="wav"
)

print("Conversión completa")

