import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import webbrowser
import pymysql
import os
from pynput.keyboard import Key, Controller
import time
import wikipedia

keyboard = Controller() #modo para controlar teclado

user = "señor"

name = 'yarbiss'

chrome = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"

listener = sr.Recognizer()

engine=pyttsx3.init()

engine.setProperty('rate', 170)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen(text):
    try:
        with sr.Microphone() as source:
            print(text)
            voice = listener.listen(source)#voice escuchara lo que digamos por el microfono
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower() #rec
           
            if name in rec:
                rec = rec.replace(name, '')
                print('Usted dijo: '+ rec)
    except:
        pass

    return rec


def functions():
    #musica y youtube
    rec = listen("Esperando ordenes..")
    
    if 'reproduce' in rec:
        music = rec.replace('reproduce','')
        talk('Reproduciendo '+ music)
        pywhatkit.playonyt(music)

    #Hora
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)

    #Saludo 1
    elif 'hola' in rec:
        talk("Buenos dias "+ user)

    #Saludo 1 
    elif 'buenos' in rec:
        talk("Un gusto tenerlo de vuelta, "+ user)

    #Buscador 
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        talk('Buscando '+ order)
        pywhatkit.search(order)

    #Fecha
    elif 'fecha' in rec:
        fecha = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Hoy es " + fecha) 
        
    elif 'ejecuta' in rec:
        order = rec.replace('ejecuta','')
        talk('Abriendo '+ order)
        app = order+'.exe'
        os.system(app)  

#ABRIR ALGUNA APLICACION
    elif 'abre' in rec:

        order = rec.replace('abre','')
        talk('Por supuesto, abriendo '+ order)
        keyboard.press(Key.cmd_l)
        keyboard.release(Key.cmd_l)
        time.sleep (0.1)
        keyboard.type(order)
        time.sleep (0.1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

#sonidos
    elif 'dime un chiste' in rec:
        talk(pyjokes.get_joke('es'))

#enviar mensaje

    elif 'nuevo mensaje' in rec:
        talk('A quien quieres enviarle un mensaje?')
        with keyboard.pressed(Key.ctrl):
         keyboard.press('n')
         keyboard.release('n')

#escribir

    elif 'escribe' in rec:

        order = rec.replace('escribe','')
        talk('Por supuesto contactando a'+ order)
        time.sleep (0.1)
        keyboard.type(order)
        time.sleep (0.1)

#enter
    elif 'enter' in rec:

        order = rec.replace('enter','')
        talk('Entendido')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

#referencia peggy cap
    elif 'ha pasado un largo tiempo' in rec:

         webbrowser.open("https://www.youtube.com/watch?v=4OtcskeRBJw")         
         talk('definitivamente '+ user)

#WIKIPEDIA
    elif 'qué es' in rec:
        order = rec.replace('qué es','')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, sentences=1)
        talk(info)

    elif 'que significa' in rec:
        order = rec.replace('que significa','')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, sentences=1)
        talk(info)
#charla
    elif 'quien sos' in rec:
       
         talk('Soy yarbiss, un placer')

    elif 'cómo te llamas' in rec:       
         talk('mi nombre es yarbis')

    elif 'apagar' in rec:
        talk("Espero poder servirlo nuevamente "+ user)

    else:
        talk("No te entendi muy bien, vuelve a intentarlo")

#iniciador
if __name__ == '__main__':
        functions()