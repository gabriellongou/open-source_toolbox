from pydub import AudioSegment

try:
    # Load the .m4a file
    song = AudioSegment.from_file("my_full_audio.m4a", format="m4a")

    # Check the length of the song
    song_length = len(song) / (60 * 1000)  # Convert to minutes
    print(f"Original song length: {song_length} minutes")

    # PyDub handles time in milliseconds
    thirty_minutes = 30 * 60 * 1000

    # Extract audio from 30 minutes until the end
    after_30_minutes = song[thirty_minutes:]

    after_30_minutes.export("my_audio_30_first_minutes.mp3", format="mp3")

    # Check the length of the extracted segment
    extracted_length = len(after_30_minutes) / (60 * 1000)  # Convert to minutes
    print(f"Extracted segment length: {extracted_length} minutes")

except Exception as e:
    print(f"An error occurred: {e}")
