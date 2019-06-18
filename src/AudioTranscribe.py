# Método para la transcripción a texto de un audio .wav

import speech_recognition as sr

from os import path


audio_file = "/audio/audio-test.wav"
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
  r.adjust_for_ambient_noise(source)
  audio = r.record(source)
  try:
    print("Wait...")
    text = r.recognize_google(audio)
    print(text)
  except:
    print("I didnt quite catch that")
