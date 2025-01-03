# text_2_speech_container with playback speed tuning

# Audio Generation with gTTS and Pydub

This repository provides a Python-based solution for generating audio from text using Google Text-to-Speech (gTTS) and speeding up the generated audio using Pydub. The text is read from a `story.txt` file, converted to speech, and saved as an audio file. The audio is then sped up to make it more suitable for quick narrations.

## Description

The project reads a text file (`story.txt`) that contains the content you want to be narrated. It then converts this text to speech using the `gTTS` library (Google Text-to-Speech), and the audio file is saved in the `/app/output_files` directory inside the container. The generated audio is further sped up using `Pydub` to create a faster-paced narration. The result is exported as a `.mp3` file.

### Key Features:
- Text-to-Speech conversion using gTTS.
- Audio speed-up using Pydub to adjust the playback speed.
- Output is saved as a `.mp3` file in the `/app/output_files` directory.

## Prerequisites

Before running this project, you need to have the following installed:

- Docker (for containerized execution)
- Python 3.x (for building the Docker image)
- A text file named `story.txt` that contains the text you want to convert to audio.

## Project File Organization

The project is structured as follows:
```
├── app.py # Main Python script that handles text-to-speech conversion and speed adjustment
├── Dockerfile # Docker configuration to build the application container
├── requirements.txt # Python dependencies file
├── story.txt # Text file containing the story or content to be converted to speech
└── output_files/ # Directory where generated audio files are saved
  └── output.mp3 # Example output audio file
```

## Installation

To build and run the Docker container:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/oubaaid/text_2_speech_container.git
    cd text_2_speech_container
    ```

2. **Build the Docker image**:
    ```bash
    docker build -t tortoise-orm-app .
    ```

3. **Run the Docker container**:
    ```bash
    docker run -p 8000:8000 -v C:/path/to/output_files:/app/output_files tortoise-orm-app
    ```

   - Replace `C:/path/to/output_files` with the actual path where you want the output `.mp3` files to be saved.
   - The container will mount the `output_files` directory from your local machine to the `/app/output_files` directory inside the container.

## Usage

1. Ensure that the `story.txt` file is present in the root directory of the project.
2. Run the Docker container as described above.
3. The program will read the content of `story.txt`, convert it to speech, and save it as an `.mp3` file in the output folder.
4. The generated `.mp3` file will be sped up by 1.25x (you can modify this value in the `app.py` code).

### Example output

After running the program, you should see an output message similar to:
Audio saved as output_files/output.mp3

