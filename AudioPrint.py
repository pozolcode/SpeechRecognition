import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index = 1, sample_rate = 48000, chunk_size = 2048) as source:
  r.adjust_for_ambient_noise(source)
  print("Say something!")
  audio = r.listen(source)
  with open("Audio/microphone-test.wav", "wb") as f:
    print("Wait...")
    f.write(audio.get_wav_data())
