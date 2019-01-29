from nltk.corpus import wordnet
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
def meaning(word):
    #engineio = pyttsx3.init()
    language = 'en'
    syn=wordnet.synsets(word)
    text1="meaning:"+syn[0].definition()
    #engineio.runAndWait()
    #print(syn[0].examples()[1])
    myobj1 = gTTS(text=text1, lang=language, slow=False)
    myobj1.save("meaning.mp3")
    text2="used as:"+syn[0].examples()[0]
    myobj2 = gTTS(text=text2, lang=language, slow=False)
    myobj2.save("synonyms.mp3")

    os.system("mpg321 meaning.mp3")
    os.system("mpg321 synonyms.mp3")
    os.remove("meaning.mp3")
    os.remove("synonyms.mp3")

    #engineio.runAndWait()
    #print()
if __name__ == '__main__':
    word=input("enter the word ")
    meaning(word)
