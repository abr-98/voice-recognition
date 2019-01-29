import pyaudio
import wave
import speech_recognition as sr
import pyttsx3
import engineio
from test_meaning import meaning
r = sr.Recognizer()
"""FORMAT = pyaudio.paInt16   #a format of audio
CHANNELS = 2        #no of samples in a frame
RATE = 44100        #no of samples per second
CHUNK = 1024        #no of frames
RECORD_SECONDS = 3      #time for records
WAVE_OUTPUT_FILENAME = "command.wav"       #file to be written in
audio = pyaudio.PyAudio()       #PyAudio func()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,       #recording AudioFile
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
#print ("recording...")
frames = []                 #initializing frames

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  #frames in loop from 0 to required number of frames -1
    data = stream.read(CHUNK)     # Reading chunks
    frames.append(data)             #adding sound frames
#print( "finished recording")


# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')            #opening the audio file in write binary mode
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)                     #setting profiles
waveFile.writeframes(b''.join(frames))      #saving as byte literal
waveFile.close()"""
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)            # use "test.wav" as the audio source
    audio = r.listen(source)
    print("k")
    tells=r.recognize_google(audio)
    test=tells.lower()
    test2="means"
    print("m")
    print(tells)
    #print(test2)
    to_compare=test2.lower()
    if to_compare in test:
        pos=test.find(to_compare)
        pos_1=pos-1
        if pos==0:
          str=tells[6:]
        else:
          str=test[:pos_1]



#except sr.UnknownValueError:
#    engineio = pyttsx3.init()
#    print("l")
#    engineio.say('Sorry could not understand')
#    engineio.runAndWait()
