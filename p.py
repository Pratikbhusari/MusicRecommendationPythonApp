import moviepy.editor as mp 
import speech_recognition as sr 


# Load the video 
video = mp.VideoFileClip("Why You Should Learn Physics.mp4") 

# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile("audiofile.wav") 

# Initialize recognizer 
r = sr.Recognizer() 

# Load the audio file 
with sr.AudioFile("audiofile.wav") as source: 
	data = r.record(source) 

# Convert speech to text 
text = r.recognize_google(data) 

# Print the text 
print("\nThe resultant text from video is: \n") 
print(text) 

# import the module 
from indic_transliteration import sanscript 
from indic_transliteration.sanscript import transliterate 

# the text to be transliterated 
newtext = text

print("\n Text in Gujarati language : \n ")

# printing the transliterated text 
print(transliterate(newtext, sanscript.ITRANS, sanscript.GUJARATI))

# print("\n Text in Hindi language : \n ")
# print(transliterate(newtext, sanscript.ITRANS, sanscript.DEVANAGARI))


# print("\n Text in Tamil language : \n ")
# print(transliterate(newtext, sanscript.ITRANS, sanscript.TAMIL))

# print("\n Text in Kannada language : \n ")
# print(transliterate(newtext, sanscript.ITRANS, sanscript.KANNADA))