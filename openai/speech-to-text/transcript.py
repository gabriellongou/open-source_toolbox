import openai

# Transcribe the audio file created thanks to cut.py code
audio_file = open("my_audio_30_first_minutes.mp3", "rb")
response = openai.Audio.transcribe("whisper-1", audio_file)

transcript_text = dict(response)["text"]

# Save the transcript to a .txt file
with open("transcript30-end.txt", "w") as txt_file:
    txt_file.write(transcript_text)


audio_file.close()
