from pydub import AudioSegment

try:
    # Load the .m4a file
    song = AudioSegment.from_file("my_full_audio_file.m4a", format="m4a")

    # Check the length of the file in milliseconds
    song_length_ms = len(song)
    song_length_minutes = song_length_ms / (60 * 1000)  # Convert to minutes
    print(f"Original song length: {song_length_minutes:.2f} minutes")

    # PyDub handles time in milliseconds
    thirty_minutes = 30 * 60 * 1000

    # Initialize segment counters
    segment_start = 0
    segment_end = thirty_minutes
    segment_counter = 1

    # Loop through the file and extract 30-minute segments
    while segment_start < song_length_ms:
        # Extract segment
        segment = song[segment_start:segment_end]
        
        # Export segment
        segment_filename = f"my_audio_segment_{segment_counter}.mp3"
        segment.export(segment_filename, format="mp3")
        print(f"Exported: {segment_filename}")

        # Move to the next segment
        segment_start += thirty_minutes
        segment_end += thirty_minutes
        segment_counter += 1

except Exception as e:
    print(f"An error occurred: {e}")
