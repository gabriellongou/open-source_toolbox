# Audio Transcript Tool

## Overview
Tired of writing meeting reports? With the **Audio Transcript Tool**, you can easily transcribe your audio recordings from meetings, lectures, interviews, and more. This tool is designed to efficiently extract a segment of an audio file starting from the 30-minute mark and then transcribe it into a readable text format.

The tool utilizes two main libraries:
- **OpenAI**: For audio transcription.
- **PyDub**: For audio file manipulation.

## Prerequisites
1. You need to have Python installed on your machine.
2. An OpenAI account to use the transcription API.
3. Install `ffmpeg` to help `pydub` process audio files.

## Installation of ffmpeg
`ffmpeg` is a multimedia framework used to handle audio, video, and other multimedia files and streams. It's essential for the functionality of `pydub`. Here's how you can install it:

### On Windows:
1. Download a static build from [ffmpeg's official site](https://ffmpeg.org/download.html).
2. Unzip the downloaded file.
3. Add the `bin` directory from the unzipped folder to your system's PATH.

## Code Breakdown
The tool has two main parts:

1. **Audio Segmentation**: 
    - The audio file (`my_full_audio.m4a`) is loaded.
    - The audio segment starting from the 30-minute mark until the end is extracted and saved as `my_audio_30_first_minutes.mp3`.

2. **Transcription**:
    - The extracted audio file (`my_audio_30_first_minutes.mp3`) is transcribed using OpenAI's Whisper ASR system.
    - The transcript is saved to a `.txt` file named `transcript30-end.txt`.

## Usage
1. Make sure your audio file is named `my_full_audio.m4a` and is in the same directory as the script.
2. Run the script.
3. The transcribed text will be saved in `transcript30-end.txt`.

## Known Limitations
- The tool currently assumes the audio file format to be `.m4a` for input. If you have another format, minor adjustments might be necessary.
- The transcription accuracy might vary based on the audio quality and clarity of speech.
