#Change male and female voice

import pyttsx3 as pt
 
# init function to get an engine instance for the speech synthesis  
engine = pt.init() 
name=input("Enter your name ")
# say method on the engine that passing input text to be spoken 
engine.setProperty('rate', 120) 
# Set volume 0-1 
engine.setProperty('volume',1) 

  
voices = engine.getProperty('voices')
#print(voices)
# run and wait method, it processes the voice commands.  


"""for voice in voices: 
    # to get the info. about various voices in our PC  
    print("Voice:") 
    print("ID: %s" %voice.id) 
    print("Name: %s" %voice.name) 
    print("Age: %s" %voice.age) 
    print("Gender: %s" %voice.gender) 
    print("Languages Known: %s" %voice.languages)"""
    
#voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voices[1].id) 
engine.say('Hello {} , how may I help you'.format(name)) 
engine.setProperty('voice', voices[0].id) 
engine.say('Hello {} , Thank you'.format(name)) 

engine.runAndWait() 