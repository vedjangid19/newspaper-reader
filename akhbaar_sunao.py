from win32com.client import Dispatch
from newsapi import NewsApiClient

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == '__main__':

    import requests
    import json

    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=4f097fd65f8a48d28e1b47b688463f6c"

    r = requests.get(url)
    #print(r.status_code)
    re=r.text
    a = json.loads(re)

    for i in range(11):
        

        print(a['articles'][i]['title'])
        speak(a['articles'][i]['title'])


    




