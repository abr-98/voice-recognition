import pyaudio
import wave
import speech_recognition as sr
import os
from gtts import gTTS

r = sr.Recognizer()
"""
FORMAT = pyaudio.paInt16   #a format of audio
CHANNELS = 2        #no of samples in a frame
RATE = 44100        #no of samples per second
CHUNK = 1024        #no of frames
RECORD_SECONDS = 2      #time for records
WAVE_OUTPUT_FILENAME = "file.wav"       #file to be written in


audio = pyaudio.PyAudio()       #PyAudio func()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,       #recording AudioFile
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []                 #initializing frames

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  #frames in loop from 0 to required number of frames -1
    data = stream.read(CHUNK)     # Reading chunks
    frames.append(data)             #adding sound frames
print( "finished recording")


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

#chunk=1024
#f=wave.open(r"/home/abhijit/atom_projects/file.wav","rb")       #opening files

#p=pyaudio.PyAudio()

#stream = p.open(format = p.get_format_from_width(f.getsampwidth()),             #retrieving audio characteristics
#                channels = f.getnchannels(),
#                rate = f.getframerate(),
#                output = True)
#read data
#data = f.readframes(chunk)                  #Reading the frame data

#while data:
#    stream.write(data)                  #playing stream data
#    data = f.readframes(chunk)

#stop stream
#stream.stop_stream()
#stream.close()

#close PyAudio
#p.terminate()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)            # use "test.wav" as the audio source
    audio = r.listen(source)
try:
    tells=r.recognize_google(audio)
#print(tells)
    test=tells.lower()
    test2="hello"
    #print(test2)
    to_compare=test2.lower()
    #print(to_compare)
    if to_compare in test:
        #print("k")
        mytext = 'yes, what do you want'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("respond.mp3")
        os.system("mpg321 respond.mp3")
        os.remove("respond.mp3")
        #engineio = pyttsx3.init()
        #engineio.say('yes, what do you want')
        #engineio.runAndWait()
    #os.remove('file.wav')
    #print("Transcription: " + tells)
except sr.UnknownValueError:
    chunk = 1024

#open a wav format music
    f = wave.open("disconnect.wav","rb")
#instantiate PyAudio
    p = pyaudio.PyAudio()
#open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
#read data
    data = f.readframes(chunk)

#play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

#stop stream
    stream.stop_stream()
    stream.close()

#close PyAudio
    p.terminate()
#print(test)

#print(type(tells))
