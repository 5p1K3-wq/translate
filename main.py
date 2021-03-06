from transliterate import translit
from num2words import num2words
from gtts import gTTS
import os
import pyglet

grandfather_speech = """
Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is 
mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance 
of my enemies. Neither will happen.\n
More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...
"""

print(translit(grandfather_speech, "ru"))
print("78", translit(num2words(78), "ru"), sep=" - ")
print("15", translit(num2words(15), "ru"), sep=" - ")
print("3", translit(num2words(3), "ru"), sep=" - ")
print("40", translit(num2words(40), "ru"), sep=" - ")
print("8", translit(num2words(8), "ru"), sep=" - ")


# play grandfather's speech in Russia
filename_en = '/tmp/speech_en.mp3'
filename_ru = '/tmp/speech_ru.mp3' 

tts_ru = gTTS(text=grandfather_speech, lang="ru")
tts_en = gTTS(text=grandfather_speech, lang="en")

tts_ru.save(filename_ru)
tts_en.save(filename_en)

os.system("mpg321 " + filename_ru)
os.system("mpg321 " + filename_en)

os.remove(filename_ru)
os.remove(filename_en)