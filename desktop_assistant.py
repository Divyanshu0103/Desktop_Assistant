import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os

'''for taking the commands and recognizing the command from the
speech_Recognition module and the recongizer method for recognizing'''

def TakeCommands():

    r = sr.Recognizer()

    '''from the speech_Recognition module, the Microphone module
    for listening the command'''

    with sr.Microphone() as source:

        print("Listening.....")

        r.pause_threshold = 0.7 
        audio = r.listen(source)
        
        '''seconds of non-speaking audio before 
        a phrase is considered complete'''


    ''' using the try and catch method so that if sound is recognized
        it is good else we will have exception handling'''

    try:
        print("Recognizing....")     
        Query = r.recognize_google(audio, language ='en-in')
        print("The command is printed=", Query)

        '''for Listening the command in indian english and'hi-In'
           for hindi recognizing'''

    except Exception as e:
        print(e)
        print("Please say that again Sir")
        return "None"

    return Query 

def speak(audio):

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice',voices[1].id)

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.

    engine.say(audio) #Method for the speaking of the assistant

    engine.runAndWait() #Blocks while processing all the currently queued commands

def Hello():
    
    speak("Hello Sir I am your Desktop Assistant Friday.Tell me how may I help you")

def TellDay():
    
    day = datetime.datetime.today().weekday() + 1

    day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        
        speak(" The day is " + day_of_the_week)

def TellTime():

    time = str(datetime.datetime.now())
    print(time)
    hour = str(datetime.datetime.now().hour)
    min = str(datetime.datetime.now().minute)

    speak("The time is {} Hours and {} Minutes ".format(hour,min))

            

def Take_query():

    Hello()

    while(True):

        Query = TakeCommands().lower()
        if "open google" in Query:
            speak(" Opening Google sir")

            webbrowser.open("www.google.com")
            continue

        elif "open youtube" in Query:
            speak(" Opening Youtube sir")
            webbrowser.open("www.youtube.com")
            continue

        elif "open wikipedia" in Query:
            speak(" Opening Wikipedia sir")
            webbrowser.open("www.wikipedia.com")
            continue

        elif "from wikipedia" in Query:

            speak("Checking the Wikipedia")
            Query = Query.replace("Wikipedia","")

            result = wikipedia.summary(Query,sentences = 4)
            speak(" According to wikipedia ")
            print(result)
            speak(result)
            continue

        elif "tell me about yourself " in Query:
            speak(" I am Friday . Your personal desktop Assistant here to help you .")
            continue

        elif "tell me the time" in Query:
            TellTime()
            continue

        elif "tell me the day" in Query:
            TellDay()
            continue

        elif "open vscode" in Query:
            speak(" Opening Vscode Sir ")
            codePath = r"C:\Users\91745\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
            continue

        elif "play music" in Query:
            codepath = r"C:\Users\91745\AppData\Local\Programs\Resso\Resso.exe"
            speak(" playing music sir ")
            continue
        
        elif "bye bye friday" in Query:
            speak(" Bye Sir . Have a marvelous day")
            exit()

if __name__ == '__main__':

    Take_query()
