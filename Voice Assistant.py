import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import speedtest

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.setProperty("rate", 200)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alexa sir!... please tell me how may i help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.phrase_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
        if "Alexa" in query:
            query = query.replace("Alexa", "")
            print(query)


    except Exception as e:
        # print(e)    
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshavasu72@gmail.com', "password")
    server.sendmail('harshavasu72@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    print("Hello Harsha")
    wishMe()

    while True:
        # if 1:  #used for infinite loop
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...give me a second sir!')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("That's it sir! Anything else...")
            e = takeCommand().lower()
            if e == "no thanks":
                speak("Thanks for searching sir!")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'search' in query:
            speak("What do you want to search?...")
            s = str(takeCommand())
            pywhatkit.search(s)

        elif 'play music' in query:
            music_dir = 'D:\VS CODE\songs'  # this is my local drive
            songs = os.listdir(music_dir)
            print([songs])
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open video' in query:
            video_dir = "E:\Harsha\Movies\Videos"  # this is my local drive
            videos = os.listdir(video_dir)
            for i in videos:
                print([i])
            speak("Please tell index of the video sir!")
            try:
                a = int(takeCommand())
                # print(videos)   
                os.startfile(os.path.join(video_dir, videos[a]))
                speak("Opened Sir!")
            except:
                speak("Sorry error occured sir!...Please say the index correctly")


        elif 'open image' in query:
            image_dir = 'D:\VS CODE\Python\Jarvis\images'
            images = os.listdir(image_dir)
            for i in images:
                print(i)
            speak("Please tell index of the image sir!")
            try:
                b = int(takeCommand())
                # print(videos)   
                os.startfile(os.path.join(image_dir, images[b]))
                speak("Opened Sir!")
            except:
                speak("Sorry error occured sir!...Please say the index correctly...")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harshavasu72@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harsha. I am not able to send this email")

        elif 'play' in query:
            songs = query.replace("play", "")
            speak("playing" + songs)
            pywhatkit.playonyt(songs)

        elif 'joke' in query:
            speak(pyjokes.get_jokes())

        elif 'speed' in query:
            st = speedtest.Speedtest()
            speak("Checking the internet speed sir!..")
            d = int(st.download())
            u = int(st.upload())
            print("The download speed is " + str(d) + " mbps")
            speak("The download speed is.." + str(d) + "mbp..s")
            print("The upload speed is " + str(u) + " mbps")
            speak("The upload speed is.." + str(u) + "mbp..s")
