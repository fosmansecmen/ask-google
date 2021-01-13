import subprocess, os
import pyttsx3
from get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ['yes', 'affirmative', 'si', 'sure', 'do it', 'yeah', 'confirm']
        self.cancel = ['no', 'negative', "don't", "wait", "cancel"]
        
    def discover(self, text):
        if "what" in text and "your name" in text:
            self.respond('My name is python commander. How are you?')
        else:
            f = Fetcher(url='https://www.google.com/search?q='+text)
            answer = f.lookup()
            if not answer:      # might return None
                answer = 'Retry again bro'
            self.respond(answer)
        
        if "open" or "launch" in text:
            app = text.split(" ", 1)[-1]
            os.system("open -a " + app + ".app")        # for MAC, opens the said app
            
            
    def respond(self, response):
        self.say(response)
            
    def say(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        # subprocess.call('say ' + text, shell=True)