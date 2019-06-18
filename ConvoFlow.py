import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index = 1, sample_rate = 48000, chunk_size = 2048) as source:
  r.adjust_for_ambient_noise(source)
  while (True):
    print("Say something!")
    audio = r.listen(source)
    try:
      print("Wait...")
      text = r.recognize_google(audio)
      if text == "bye-bye":
        break
      else:
        print(text)
    except:
      print("I didnt quite catch that")
  print("\nCome back soon!")
