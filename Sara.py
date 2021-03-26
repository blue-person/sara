import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import random
import sys
import wolframalpha

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('4VK6W8-UTHAEWRYUA')
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', voices[1].id)
wikipedia.set_lang("es")

def decir(audio):
    engine.say(audio)
    engine.runAndWait()

def deseo():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        decir("¡Buenos días!")

    elif hour>=12 and hour<18:
        decir("¡Buenas tardes!")

    else:
        decir("¡Buenas noches!")

    msg = ['Hola Alejandro, Soy Sara. ¿Como puedo ayudarte?', 'Hola Alejandro. ¿En qué puedo ayudarte?', '¿Qué puedo hacer por ti?', 'Bienvenido a Sara. ¿En qué te puedo ayudar?']
    decir(random.choice(msg))

deseo()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Reconociendo...")
        query = r.recognize_google(audio, language='es-CO')
        print(f"Usted dijo: {query}\n")

    except Exception as e:
        decir("No te he entendido bien, ¿puedes decirlo de nuevo?")
        print("Di eso de nuevo por favor...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pruebasprousuario@gmail.com', 'SonicSpeeder1991')
    server.sendmail('pruebasprousuario@gmail.com', to, email_text)
    server.close()

if __name__ == "__main__":

    while True:
        query = takeCommand().lower()

        if 'adiós' in query or 'apagate' in query:
            decir('Adiós Alejandro')
            sys.exit()

        elif 'Sara' in query:
            pass

        elif 'hola' in query:
            decir('Hola Alejandro')

        elif 'gracias' in query:
            msg = ['No te preocupes', 'De nada', 'No hay de qué', 'Con gusto']
            decir(random.choice(msg))

        elif 'youtube' in query or 'Youtube' in query:
            if query.split()[-1] != 'youtube':
                cuest = query.split()[-1]
                direccion = 'https://www.youtube.com/results?search_query='
                busqueda = direccion + cuest
                webbrowser.open(busqueda)

            else:
                decir('¿Qué te gustaría que buscara en Yutub?')
                ans = takeCommand()
                direccion = 'https://www.youtube.com/results?search_query='
                busqueda = direccion + ans
                webbrowser.open(busqueda)

            msg = ['Con gusto', 'Vale', 'De inmediato', 'Claro', 'Ok']
            decir(random.choice(msg))

        elif 'google' in query or 'Google' in query:
            if query.split()[-1] != 'google':
                cuest = query.split()[-1]
                direccion = 'https://www.google.com/search?q='
                busqueda = direccion + cuest
                webbrowser.open(busqueda)

            else:
                decir('¿Qué te gustaría que buscara en Gugol?')
                ans = takeCommand()
                direccion = 'https://www.google.com/search?q='
                busqueda = direccion + ans
                webbrowser.open(busqueda)

            msg = ['Con gusto', 'Vale', 'De inmediato', 'Claro', 'Ok']
            decir(random.choice(msg))

        elif 'música' in query:
            music_folder = 'C:\\Users\\aleja\\Music\\Gorillaz\\Humanz - (2017)'
            music = ['"10. Andromeda (feat. D.R.A.M.).mp3"', '"03. Strobelite (feat. Peven Everett).mp3"']
            os.chdir(music_folder)
            os.system(random.choice(music))

            msg = ['Con gusto', 'Vale', 'De inmediato', 'Claro', 'Ok']
            decir(random.choice(msg))

        elif 'hora' in query:
            strTime = datetime.datetime.now().strftime("%#I:%M:%p")
            decir(f"Son las {strTime}")

        elif 'reiniciate' in query:
            decir('Reiniciando sistema...')
            os.execl(sys.executable, sys.executable, *sys.argv)

        elif 'editor' in query:
            codePath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(codePath)

            msg = ['Con gusto', 'Vale', 'De inmediato', 'Claro', 'Ok']
            decir(random.choice(msg))

        elif 'dónde queda' in query or 'dónde está' in query:
            lugar = query.split()[-1]
            direccion = 'https://www.google.com/maps/place/'
            busqueda = direccion + lugar
            decir('Estoy abriendo Gugol Maps para mostrarte la ubicacion de' +lugar)
            webbrowser.open(busqueda)

        elif 'correo' in query:
            try:
                decir('¿A quién se lo deseas enviar?')
                quiene = takeCommand() + '@gmail.com'
                to = quiene
                decir("¿Qué quieres que ponga en el mensaje?")
                email_text = takeCommand()
                sendEmail(to, email_text)
                decir("¡He enviado el correo")
            except Exception as e:
                print(e)
                decir("Lo siento Alejandro. Sucedió un error y no pude enviar tu correo.")

        elif 'cuánto es' in query or 'quién es' in query or 'qué es' in query or 'qué fue' in query:
            decir('Realmente no lo sé. ¿Quieres que intente responderte usando mis bases de datos?')
            respuesta = takeCommand()

            if 'si' in respuesta or 'sí' in respuesta:
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        decir('Lo tengo.')
                        decir('Según Wolfram-Alpha...')
                        decir(results)

                    except Exception as e:
                        print(e)
                        results = wikipedia.summary(query, sentences=2)
                        decir('Lo tengo.')
                        decir('Según Wikipedia...')
                        decir(results)

                except:
                    decir('Perdón Alejandro. No logre encontrar una respuesta a lo que pediste. Lo buscare en Gugol.')
                    ansGoErr = query
                    direccionGoErr = 'https://www.google.com/search?q='
                    busquedaGoErr = direccionGoErr + ansGoErr
                    webbrowser.open(busquedaGoErr)


            else:
                decir('Vale')
