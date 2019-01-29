import pyttsx3
import engineio

import speech_recognition as sr

r = sr.Recognizer()
engineio = pyttsx3.init()

engineio.say('say something.')
engineio.runAndWait()
with sr.Microphone(device_index = 6, sample_rate = 16000, chunk_size = 1024) as source:
  audio = r.listen(source)
  try:
      print("You said " + r.recognize_google(audio))
  except sr.UnknownValueError:
      print("Could not understand audio")
  except sr.RequestError as e:
      print("Could not request results; {0}".format(e))
