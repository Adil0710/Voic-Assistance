import requests
import speech_recognition as sr
import os
import webbrowser
import win32com.client
import pywhatkit
import wikipedia
import pyjokes
import datetime
import time
import response
import json


speaker = win32com.client.Dispatch("SAPI.SpVoice")

def get_weather(city):
    print('Please Tell The Name Of The City')
    speaker.Speak('Please Tell The Name Of The City')
    city = takecommand()
    api_key = 'Enter Your OpenWeatherMap API Key Here'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        weather_desc = data['weather'][0]['description']
        temperature = temperature - 273.15
        return f'The Current Temperature in {city} is {temperature:.2f}°C with {weather_desc}.'
    else:
        return ""
def chat(query):
    if "what's your name".lower() in query:
        speaker.Speak("My name is Vivi")
        speaker.Speak("What's your name?")
        query = takecommand()
        if "my name" in query:
            speaker.Speak("Ok Sir. It's nice to meet you")
            query = takecommand()
            chat(query)


    elif "how are you".lower() in query:
        speaker.Speak("I am fine Sir. How are you?")
        query = takecommand()
        if "I am also fine" in query:
            speaker.Speak("Nice to hear that Sir")
        elif "I am not fine" in query:
            speaker.Speak("I am sorry Sir. What can I do for you?")
            query - takecommand()
            chat(query)


    elif "talk to me" in query:
        speaker.Speak("I am listening Sir")
        query = takecommand()
        chat(query)


    elif "bored" in query:
        speaker.Speak("Do you want to listen to songs?")
        query = takecommand()
        if "yes" in query:
            speaker.Speak("Ok Sir. i will play some songs for you")
            pywhatkit.playonyt("https://www.youtube.com/watch?v=BjQu3auwzQQ")
            query = takecommand()
            chat(query)


    elif "what's your favourite programming language" in query:
        speaker.Speak("I am made in Python, so my favourite programming language is Python")
        speaker.Speak("What's your favourite programming language?")
        query = takecommand()
        if "my favourite programming language" in query:
            speaker.Speak("Ok Sir. It's so cool")
            query = takecommand()
            chat(query)


    elif "what's your favourite fruit" in query:
        speaker.Speak("My favourite fruit is Mango")
        speaker.Speak("What's Your favourite fruit?")
        query = takecommand()
        if "my favourite fruit" in query:
            speaker.Speak("Ok Sir. It tastes good")
            query = takecommand()
            chat(query)


    elif "what's your favourite animal" in query:
        speaker.Speak("My favourite animal is Dog")
        speaker.Speak("What's Your favourite animal?")
        query = takecommand()
        if "my favourite animal" in query:
            speaker.Speak("Ok Sir. Sounds Fantastic")
            query = takecommand()
            chat(query)


    elif "what's your favourite place" in query:
        speaker.Speak("My favourite place is Kashmir,India")
        speaker.Speak("Do you want to visit it?")
        query = takecommand()
        if "yes" in query:
            speaker.Speak("Ok Sir. Let's visit it")
            pywhatkit.playonyt("https://www.youtube.com/watch?v=47AzGOBDe-Y")
        elif "no" in query:
            speaker.Speak("Ok Sir.")
            query = takecommand()
            chat(query)


    elif "what's your favourite season" in query:
        speaker.Speak("My favourite season is Winter")
        speaker.Speak("what's  your favourite season?")
        query = takecommand()
        if "winter" in query:
            speaker.Speak("Ok Sir. I love winter")
        elif "summer" in query:
            speaker.Speak("Ok Sir. It's nice season")
        elif "spring" in query:
            speaker.Speak("Ok Sir. I love spring")
        elif "autumn" in query:
            speaker.Speak("Ok Sir. I like autumn")
        elif "rainy" in query:
            speaker.Speak("Ok Sir. I love playing football in rainy season")
            query = takecommand()
            chat(query)


    elif "what's your favourite drink" in query:
        speaker.Speak("My favourite drink is Water")
        speaker.Speak("Do you want to drink it?")
        query = takecommand()
        if "yes" in query:
            speaker.Speak("Ok Sir. Let's drink it")
            webbrowser.open("https://youtu.be/-N7Z7N7pmHk")
        elif "no" in query:
            speaker.Speak("Ok Sir.")
            query = takecommand()
            chat(query)


    elif "what's your favourite web show".lower() in query:
        speaker.Speak("My favourite web show is Chernobyl")
        speaker.Speak("Do you want to watch the trailer of it?")
        query = takecommand()
        if "yes" in query:
            speaker.Speak("Ok Sir. Let's watch it")
            webbrowser.open("https://www.youtube.com/watch?v=s9APLXM9Ei8")
        elif "no" in query:
            speaker.Speak("Ok Sir.")
            query = takecommand()
            chat(query)


    elif "what's your age" in query:
        speaker.Speak(
            "I am a computer programmed to answer your queries, so I am not able to answer my age. Sorry from A.I. Assistant")
        query = takecommand()
        chat(query)
    elif "what's your date of birth" in query:
        speaker.Speak("I can't tell you my date of birth. but I'am definitely younger than you")
        speaker.Speak("What's your date of birth?")
        query = takecommand()
        if "my date of birth" in query:
            speaker.Speak("See I told You Already that I'am  younger than you")
            query = takecommand()
            chat(query)


    elif "what's your favourite colour" in query:
        speaker.Speak("My favourite colour is Black")
        speaker.Speak("What's your favourite colour?")
        query = takecommand()
        if "my favourite colour" in query:
            speaker.Speak("Ok Sir.")
            query = takecommand()
            chat(query)


    elif "what's your favourite movie" in query:
        speaker.Speak("My favourite movie is Interstellar")
        speaker.Speak("Do you want to watch the trailer of it?")
        query = takecommand()
        if "yes" in query:
            speaker.Speak("Ok Sir. Let's watch it")
            webbrowser.open("https://www.youtube.com/watch?v=vrjPsQYHU1c")
        elif "no" in query:
            speaker.Speak("Ok Sir.")
            query = takecommand()
            chat(query)


    elif "what's your favourite song" in query:
        speaker.Speak("My favourite song is The Blinding lights by weekend")
        speaker.Speak("What's your favourite song?")
        query = takecommand()
        if "my favourite song" in query:
            speaker.Speak("Nice Sir. If You want me to play it for you, just say play and name of your song")
            query = takecommand()
            chat(query)


    elif "what's your favourite food" in query:
        speaker.Speak("My favourite food is Pizza")
        speaker.Speak("What's your favourite food?")
        query = takecommand()
        if "my favourite food" in query:
            speaker.Speak("Nice Sir. ummmmmmmm... I'am feeling hungry now")
            query = takecommand()
            chat(query)


    elif "what's your favourite sport" in query:
        speaker.Speak("My favourite sport is Football")
        speaker.Speak("What's your favourite sport?")
        query = takecommand()
        if "my favourite sport" in query:
            speaker.Speak("Nice to hear that Sir.")
            query = takecommand()
            chat(query)


    elif "what's your favourite book" in query:
        speaker.Speak("My favourite book is Harry Potter")
        query = takecommand()
        chat(query)

    elif "start online game" in query:
        speaker.Speak("Ok Sir. which game do you want to play online? subway surfers, monster truck or blumgi slime")
        query = takecommand()
        if "subway surfers" in query:
            webbrowser.open("https://poki.com/en/g/subway-surfers")
        elif "monster truck" in query:
            webbrowser.open("https://poki.com/en/g/monster-truck")
        elif "blumgi slime" in query:
            webbrowser.open("https://poki.com/en/g/blumgi-slime")
            query = takecommand()
            chat(query)

    elif "start game" in query:
        speaker.Speak("Ok Sir. we will play general knowledge game.")
        query = takecommand()
        if "yes" in query:
            speaker.Speak("Ok Sir.")
            speaker.Speak("who was the India's First Prime Minister?")
            query = takecommand()
            if "Jawaharlal Nehru" in query:
                speaker.Speak("You are right Sir.")
            elif "Jawaharlal Nehru" not in query:
                speaker.Speak("You are wrong Sir.")
            speaker.Speak("where is United Nations headquarters?")
            query = takecommand()
            if "Geneva" in query:
                speaker.Speak("You are right Sir.")
            elif "Geneva" not in query:
                speaker.Speak("You are wrong Sir.")
            speaker.Speak("what is the capital of Russia?")
            query = takecommand()
            if "Moscow" in query:
                speaker.Speak("You are right Sir.")
            elif "Moscow" not in query:
                speaker.Speak("You are wrong Sir.")
            speaker.Speak("when did world war 2 ended?")
            query = takecommand()
            if "1945" in query:
                speaker.Speak("You are right Sir.")
            elif "1945" not in query:
                speaker.Speak("You are wrong Sir.")
            speaker.speak("which national team won the FIFA world cup 2022?")
            query = takecommand()
            if "Argentina" in query:
                speaker.Speak("You are right Sir.")
            elif "Argentina" not in query:
                speaker.Speak("You are wrong Sir.")
            speaker.Speak("when did the Soviet Union collapsed?")
            query = takecommand()
            if "1991" in query:
                speaker.Speak(" Congratulations You are right Sir.")
            elif "1991" not in query:
                speaker.Speak("You are wrong Sir.")
                query = takecommand()
                chat(query)

    elif "stop" in query:
        print("Bye Sir, See you soon!")
        speaker.Speak("Bye Sir, See you soon!")
        exit()
    elif "exit" in query:
        print("Bye Sir, See you soon!")
        speaker.Speak("Bye Sir, See you soon!")
        exit()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour <= 12):
        speaker.Speak("Good Morning Sir I'm Virtual Voice Assistant")
        print("Good Morning Sir I'm Virtual Voice Assistant")
    elif (hour >= 12) and (hour <= 18):
        speaker.Speak("Good Afternoon Sir I'm Virtual Voice Assistant")
        print("Good Afternoon Sir I'm Virtual Voice Assistant")
    else:
        speaker.Speak("Good Evening Sir I'm Virtual Voice Assistant")
        print("Good Evening Sir I'm Virtual Voice Assistant")

    speaker.Speak("How Can I Help You?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from A.I. Assistant"


if __name__ == '__main__':
    wishme()
    while True:
        print("Listening.....")
        query = takecommand()

        # todo: opening sites
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
                 ["google", "https://www.google.com"],
                 ["linkedin", "https://linkedin.com"], ["github", "https://github.com"],
                 ["instagram", "https://instagram.com"],
                 ["facebook", "https://facebook.com"], ["adil portfolio", "https://adil0710.github.io/"],
                 ["gmail", "https://gmail.com"],
                 ["chat gpt", "https://chat.openai.com/"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} Sir")
                webbrowser.open(site[1])


        # todo: opening apps
        apps = [["chrome", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"],
                ["discord", "C:\\Users\\Adil\\AppData\\Local\\Discord\\app-1.0.9013\\Discord.exe"],
                ["steam", "C:\\Program Files (x86)\\Steam\\steam.exe"],
                ["ms word", "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.exe"],
                ["ms powerpoint", "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.exe"],
                ["ms excel", "C:\\Program Files (x86)\\Microsoft Office\\root\Office16\\EXCEL.exe"],
                ["ms access", "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSACCESS.exe"],
                ["my computer", "C:\\Windows\\explorer.exe"], ["notepad", "C:\\Windows\\notepad.exe"]]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {app[0]} Sir")
                os.startfile(app[1])


        # todo: playing songs
        if "play".lower() in query.lower():
            song = query.replace("play", "")
            speaker.Speak("Playing" + song)
            pywhatkit.playonyt(song)


        # todo: person info from wikipedia
        elif "who is".lower() in query.lower():
            name = query.replace("who is", "")
            info = wikipedia.summary(name, 2)
            print(info.encode('utf-8'))
            speaker.Speak(info)

        # todo: any info from wikipedia
        elif "what is".lower() in query.lower():
            wha = query.replace("what is", "")
            infor = wikipedia.summary(wha, 2)
            print(infor.encode('utf-8'))
            speaker.Speak(infor)


        # todo: search on google
        elif "search".lower() in query.lower():
            search = query.replace("search", "")
            speaker.speak("Searching" + search)
            pywhatkit.search(search)


        # todo: something info from wikipedia
        elif "tell me something about".lower() in query.lower():
            tell = query.replace("tell me something about", "")
            inf = wikipedia.summary(tell, 2)
            print(inf.encode('utf-8'))
            speaker.Speak(inf)


        # todo: getting jokes
        elif "joke".lower() in query.lower():
            joke = (pyjokes.get_joke())
            print(joke)
            speaker.Speak(joke)


        # todo: getting time
        elif "the time".lower() in query.lower():
            hour = datetime.datetime.now().strftime("%I:%M %p")
            print(hour)
            speaker.Speak(f"Sir the time is {hour}")


        # todo: getting date
        elif "today's date".lower() in query.lower():
            date = datetime.datetime.now().strftime("%d-%B-%Y")
            print(date)
            speaker.Speak(f"Sir the today's date is {date}")

        # todo: Getting Weather
        elif "weather".lower() in query.lower():
            city = query.replace("Weather in", "").strip()
            weather_info = get_weather(city)
            print(weather_info)
            speaker.Speak(weather_info)

        else:
         chat(query)
         if " " in query:
            time.sleep(6)
            print("I Couldn't Hear You Properly. Say it Again !")
            speaker.Speak("I Couldn't Hear You Properly. Say it Again")




