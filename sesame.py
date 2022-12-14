#!/usr/bin/env python3
import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import wikipedia
import webbrowser
import requests
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
import nmap
import sys
import socket

begin = 1
end = 1024

def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("Your command is: " + data)
            
        except sr.UnknownValueError:
            print("Sorry I did not hear your command, Please repeat.")
        return data

def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)

if __name__=='__main__':
    respond("Hi, I am Sesame")
          
    while(1):
        respond("What is your command")
        text=talk().lower()
        
        if text==0:
            continue  
        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Turning off... Bye")
            break
        if "help" in text:
            respond('Useful commands can be found at github.com/n0s3y/sesam')
            
        if 'scan' in text:
            respond('What IP?')
            target = input("Enter target IP: " )
            respond(target)            
            scanner = nmap.PortScanner()
            for i in range(begin,end+1):
               
                # scan the target port
                res = scanner.scan(target,str(i))
               
                # the result is a dictionary containing 
                # several information we only need to
                # check if the port is opened or closed
                # so we will access only that information 
                # in the dictionary
                res = res['scan'][target]['tcp'][i]['state']
                respond(f'port {i} is {res}.')

        if 'get' in text:
            respond('What IP?')
            target = input("Enter target IP: ")
            respond(target)
            cmd = './n0s3y.sh'
            os.system(cmd)

        if 'ping' in text:
                    respond('What IP?')
                    target = input("Enter target IP: " )
                    respond(target)            
                    output = os.system("ping ", target)
                    respond(output)   

        if "install" in text:
                    respond('What do you want to install?')
                    install = input('please type: (choose between FirmAE)')
                    if "FirmAE" in install: 
                     os.system("git clone --recursive https://github.com/n0s3y/FirmAE && cd FirmAE && ./firm.sh")
                    
        if 'update' in text:
            respond('Updating system...')
            os.system("sudo apt update")



        else:
           respond("I do not understand that command.")
