'''text to speech
conda env voice
21/05/2024'''

import pyttsx3

engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# engine.say('Hello sir, how may I help you, sir.')

# engine.runAndWait()
# engine.stop()


# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')

# engine.runAndWait()


# def change_voice(engine, language, gender='VoiceGenderFemale'):
#     for voice in engine.getProperty('voices'):
#         if language in voice.languages and gender == voice.gender:
#             engine.setProperty('voice', voice.id)
#             return True
#     raise RuntimeError(f"Language '{language}' for gender '{gender}' not found")

# # Example usage:
# change_voice(engine, "fr_FR", "VoiceGenderFemale")
# engine.say("Bonjour tout le monde")
# engine.runAndWait()


engine.setProperty('rate', 150)  # Adjust the speech rate if needed
engine.setProperty('voice', 'fr')  # Set the voice to French

with open("blandine.txt", "r", encoding="utf8") as file:
    contenu = file.read()

engine.say(contenu)

engine.runAndWait()
