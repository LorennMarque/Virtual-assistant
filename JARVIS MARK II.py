import clipboard
import datetime
import os
import psutil
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import time
import webbrowser as we
import time
from time import sleep
import pyjokes
from pynput.keyboard import Key, Controller
import wikipedia

keyboard = Controller() #modo para controlar teclado

user = 'señor'

name = 'yarbiss'

chrome = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"

listener = sr.Recognizer()

engine=pyttsx3.init()

engine.setProperty('rate', 180)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    orden = ""
    with sr.Microphone(device_index=2) as source:
        print("Escuchando...")
        try:
            orden = r.recognize_google(r.listen(source), language="es-ES")
        except Exception as e:
            talk("Dilo otra vez porfavor")
        if name in orden:
            orden = orden.replace(name, '')
            print('Usted dijo: '+ orden)
    return orden

def bienvenida():
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        talk(f"Buenos dias {user}")
    elif (hour >= 12) and (hour < 18):
        talk(f"Buenas tardes {user}")
    elif (hour >= 18) and (hour < 21):
        talk(f"Buenas noches {user}")
    talk("Como puedo servirle?")

bienvenida()
while True:
    orden = listen().lower()

    if 'reproduce' in orden:
        music = orden.replace('reproduce','')
        talk('Reproduciendo '+ music)
        pywhatkit.playonyt(music)

    #Saludo 1
    elif 'hola' in orden:
        talk("Buenos dias "+ user)
    #Saludo 1 
    elif 'buenos' in orden:
        talk("Un gusto tenerlo de vuelta, "+ user)

    #Buscador 
    elif 'abre' in orden:

        order = orden.replace('abre','')
        talk('Por supuesto, abriendo '+ order)
        keyboard.press(Key.cmd_l)
        keyboard.release(Key.cmd_l)
        time.sleep (0.1)
        keyboard.type(order)
        time.sleep (0.1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    elif ("google" in orden):
        talk("Que le gustaria buscar "+ user + "?")
        we.open("https://www.google.com/search?q="+listen())

    elif 'busca' in orden:
        order = orden.replace('busca', '')
        talk('Buscando '+ order)
        pywhatkit.search(order)

    #Fecha
    elif 'fecha' in orden:
        fecha = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Hoy es " + fecha) 
        
    elif 'ejecuta' in orden:
        order = orden.replace('ejecuta','')
        talk('Abriendo '+ order)
        app = order+'.exe'
        os.system(app)  

#ABRIR ALGUNA APLICACION


#sonidos
    elif 'dime un chiste' in orden:
        talk(pyjokes.get_joke('es'))

#enviar mensaje

    elif 'nuevo mensaje' in orden:
        talk('A quien quieres enviarle un mensaje?')
        with keyboard.pressed(Key.ctrl):
         keyboard.press('n')
         keyboard.release('n')

#escribir

    elif 'escribe' in orden:

        order = orden.replace('escribe','')
        talk('Por supuesto contactando a'+ order)
        time.sleep (0.1)
        keyboard.type(order)
        time.sleep (0.1)

    #enter
    elif 'enter' in orden:

        order = orden.replace('enter','')
        talk('Entendido')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    #WIKIPEDIA
    elif 'qué es' in orden:
        order = orden.replace('qué es','')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, sentences=1)
        talk(info)

    elif 'que significa' in orden:
        order = orden.replace('que significa','')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, sentences=1)
        talk(info)

    elif ("youtube" in orden):
        talk("Que le gustaria buscar en Youtube "+ user + "?")
        pywhatkit.playonyt(listen())

#charla
    elif 'quien sos' in orden:
       
         talk('Soy yarbiss, un placer')

    elif 'cómo te llamas' in orden:       
         talk('mi nombre es yarbis')

    elif ("portapapeles" in orden):
        talk(clipboard.paste())
    #Hora
    elif 'hora' in orden:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)

    elif "cpu" in orden:
        talk(f"su procesador se encuentra a {str(psutil.cpu_percent())} porciento, " + user)

    elif "apagar" in orden:
        hour = datetime.datetime.now().hour
        if (hour >= 21) and (hour < 6):
            talk("Buenas noches" + user + "! Espero disfrute su descanso")
        else:
            talk("Me despido" + user + "espero servirlo nuevamente")
        quit()