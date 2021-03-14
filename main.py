import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak('Heyy Abhishek, what can I do for you?')

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening now.......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print('You said ' + command)
    except:
        print("Sorry, couldn't recognize your voice!")
    return command

def run():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        print('Playing ' + song + ' now')
        speak('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time: ' + time)
        speak('Current time is' + time)

    #elif 'what is' or 'who is' in command:
     #   wiki = command.replace('what is' or 'who is', '')
      #  info = wikipedia.summary(wiki, 1)
       # print(info)
        #speak(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif 'open' or 'search' or 'show' in command:
        search = command.replace('open' or 'search' or 'show', '')
        speak('showing results for' + search)
        webbrowser.open('https://google.com/?#q=' + search)

    else:
        print('Could you please say the command again?')
        speak('Could you please say the command again?')

while True:
    run()
