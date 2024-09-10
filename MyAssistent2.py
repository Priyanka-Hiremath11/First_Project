#importing pyttsx will convert text to speech.
#importing webrowser will open respective web url mentioned.

import pyttsx3
import webbrowser
import datetime
engine=pyttsx3.init()
engine.say("hello i am a AI, created by priyanka; working as her assistent......How can i help?")
engine.runAndWait()
while True:
    print("Enter what you want me to do")
    a=input()
 
    if a=="say":
        print("What you want me to spell:")
        p=input()
        engine.say(p)
        engine.runAndWait()
    
    elif a=="open google":
        engine.say("opeing google")
        engine.runAndWait()
        webbrowser.open("https://google.com")

    elif a=="open youtube":
        engine.say("opeing youtube")
        engine.runAndWait()
        webbrowser.open("https://youtu.be")

    elif a=="open whatsapp":
        engine.say("opeing whatsapp")
        engine.runAndWait()
        webbrowser.open("https://web.whatsapp.com/")

    elif a=="open spotify":
        engine.say("opeing spotify")
        engine.runAndWait()
        webbrowser.open("https://spotify.com")

    elif a=="hello":
        engine.say("Hi,whatsapp with you")
        engine.runAndWait()
        print("Hello what'sup with you","\U0001F917")

    elif a=="Create QR Code":
        import pyqrcode 
        import png 
        from pyqrcode import QRCode 


# String which represents the QR code
        print("Enter url")
        s =input()
        
# Generate QR code 
        url = pyqrcode.create(s) 

# Create and save the svg file naming "myqr.svg" 
        url.svg("yourqr", scale = 8) 

# Create and save the png file naming "myqr.png" 
        url.png("yourqr", scale = 6) 




    else:
        engine.say("sorry! I am unable to do that or something went wrong")
        engine.runAndWait()
        print("OOPS...ERROR")
        
    
