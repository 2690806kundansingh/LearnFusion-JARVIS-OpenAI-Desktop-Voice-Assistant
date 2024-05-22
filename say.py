import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random

chatStr=""
def chat(query):
    global chatStr
    openai.api_key =apikey
    chatStr+=f"kundan: {query}\n Jarvis"
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt= chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside of a try catch block
    say(response["choice"[0]["text"]])
    chatStr+=f"{response['choice'][0]['text']}\n"
    return response["choice"][0]["text"]


    # with open(f"Openai/prompt -{random.random(1,234567453)}","w") as f:
    with open(f"Openai/{''.join(prompt.split("intelligence")[1:]).strip()}.text","w") as f:
        f.write(text)
def say(text):
    os.system(f"say{text}")

#taking sound
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =0.6
        audio= r.listen(source)
        try:
            print("recognizing...")
            query =r.recognize_google(audio, language="en-in")
            print(f" user said: {query}")
            return query
        except Exception as e:
            return "some Error occurred. Sorry from Jarvis"
if __name__ == '__main__':
     print('pycharm')
     say("hellow i am jarvis made by you what can i help")
     while True:
         print("listening ...")
         query = takeCommand()
         sites=[["youtube","https://www.youtube.com"],["github","https://www.github.com"]
             ,["linkedin","https://www.linkedin.com"],
                ["google","https://www.google.com"]]
         #how to open site
         # todo: add more sites
         for site in sites:
             if  f"open {site[0]}".lower() in query.lower():
                 say(f"openning {site[0]} sir...")
                 webbrowser.open(site[1])
          #how to open music
         # todo: Add a features to play a specific song
         if "open music" in query:
             musicPath = "C:\Users\chand\Downloads\Despacito(PaglaSongs).mp3"
             os.system(f"open {musicPath}")

          #how to know time
         elif "the time" in query:
             strfTime = datetime.datetime.now().strfTime("%H:%M:%S")
             say(f" Sir the time is {strfTime}")

         elif "open google docs".lower() in query.lower():
             os.system(f"open/application/google docs.app")

            #use open ai to get next level

         elif "using artificial intelligence ".lower() in query.lower():
             ai(prompt =query)

         elif "Jarvis Quit".lower() in query.lower():
             exit()
         elif "reset chat".lower() in query.lower():
             chatStr=""
         else:
             print("chating...")
             chat(query,chatStr)

