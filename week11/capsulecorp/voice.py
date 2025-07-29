import pyttsx3

engine = pyttsx3.init()

# Change voice properties for robotic effect
def setup_robotic_voice():
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'robot' in voice.name.lower() or 'david' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150)    # Speed: 150 wpm
    engine.setProperty('volume', 1.0)  # Max volume

def speak(text):
    setup_robotic_voice()
    engine.say(text)
    engine.runAndWait()
