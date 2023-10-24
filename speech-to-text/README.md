# Audio Transcript Tool

## Overview
Tired of writing meeting reports? With the **Audio Transcript Tool**, you can easily transcribe your audio recordings from meetings, lectures, interviews, and more. You just need to record it (with the authorization of stakeholders). This tool is designed to efficiently extract a segment of an audio file starting from the 30-minute mark and then transcribe it into a readable text format. This cut is necessary to use OpenAi Whisper API.

The tool utilizes two main libraries:
- **OpenAI**: For audio transcription.
- **PyDub**: For audio file manipulation.

## Prerequisites
1. You need to have Python installed on your machine.
2. An OpenAI account to use the transcription API. (Espacially a OpenAI Key)
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
    - The audio segment starting from the beginning to 30-minute steps  until the end is extracted and saved as `my_audio_segment_XXX.mp3`.

2. **Transcription**:
    - The extracted audio file (`my_audio_segment_XXX.mp3`) is transcribed using OpenAI's Whisper ASR system.
    - The transcript is saved to a `.txt` file named `my_audio_segment_XXX.txt`.
