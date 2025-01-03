from gtts import gTTS
from pydub import AudioSegment

output = "/app/output_files/output_030124.mp3"

def convert_text_to_audio(text: str, output_filename: str = output):
    # Generate the audio using gTTS
    tts = gTTS(text, lang='en', tld='ca', slow=False)
    tts.save(output_filename)
    print(f"Audio saved as {output_filename}")

if __name__ == "__main__":
    # Open the file in read mode
    try:
        with open('story.txt', 'r') as file:
            text = file.read()  # Reads the entire content of the file
        convert_text_to_audio(text)
        audio = AudioSegment.from_mp3(output)
        speed_audio = audio.speedup(playback_speed=1.25) # speed up by 2x
        # export to mp3
        speed_audio.export(output, format="mp3")
    except FileNotFoundError:
        print("Error: 'story.txt' file not found.")
