import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

running = True

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    
    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )
    
    data_stream = wf.readframes(chunk)
    
    while(data_stream):
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
        
    stream.close()
    pa.terminate()
    
r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print('Listening...')
    # play_audio("./audio/harp.wav")
    
    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)
        
    # play_audio("./audio/harp.wav")
    
    command = ""
    
    try:
        command = r.recognize_google(audio)
        print('Your command:', command)
        if command in ['quit', 'bye', 'exit', 'goodbye']:
            cmd.respond('See you later!')
            global running
            running = False
            return
        cmd.discover(command)
        
    except:
        print('Could not understand you bro')
        

while(running == True):
    initSpeech()
