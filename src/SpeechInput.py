import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index = 1, sample_rate = 48000, chunk_size = 2048) as source:
  r.adjust_for_ambient_noise(source)
  print("Say something!")
  audio = r.listen(source)
  try:
    print("Wait...")
    text = r.recognize_google(audio)
    print(text)
  except:
    print("I didnt quite catch that")
