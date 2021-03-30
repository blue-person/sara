import speech_recognition as sr
import os, sys, pyttsx3, datetime, webbrowser, smtplib, random, wikipedia, wolframalpha

# Variables
nombreUsuario = "Usuario"
api_WolframAlpha = "4VK6W8-UTHAEWRYUA"
correoEmisor = "pruebasprousuario@gmail.com"
contraseñaCorreo = "SonicSpeeder1991"

# Configuracion de la voz
voz = pyttsx3.init("sapi5")
listadoVoces = voz.getProperty("voices")
voz.setProperty("voice", listadoVoces[0].id) # Si la voz se escucha en ingles con palabras en español, hay que intercambiar el 0 por un 1 (o viceversa segun el caso)

# Configuracion de librerias
solicitud_WolframAlpha = wolframalpha.Client(api_WolframAlpha)
wikipedia.set_lang("es")

# Funciones principales
def decir(audio):
    voz.say(audio)
    voz.runAndWait()

def escucharOrden():
    r = sr.Recognizer()
    segundosEspera = 0.5

    with sr.Microphone() as audioMicrofono:
        print("Escuchando...")
        r.pause_threshold = segundosEspera
        audio = r.listen(audioMicrofono)

    try:
        print("Reconociendo...")
        ordenUsuario = r.recognize_google(audio, language="es-CO")
        print(f"Usted dijo: {ordenUsuario}\n")
        return ordenUsuario
    except:
        decir("No te he entendido bien, ¿puedes decirlo de nuevo?")
        print("Di eso de nuevo por favor...")
        return "Error"

# Frases
def fraseConfirmacion():
    msg = ["Con gusto", "Vale", "De inmediato", "Claro", "Ok"]
    decir(random.choice(msg))

def fraseAgradecimiento():
    msg = ["No te preocupes", "De nada", "No hay de qué", "Con gusto"]
    decir(random.choice(msg))

def fraseSaludo():
    frases = [
        f"Hola {nombreUsuario}, Soy Sara. ¿Como puedo ayudarte?",
        f"Hola {nombreUsuario}. ¿En qué puedo ayudarte?", 
        "¿Qué puedo hacer por ti?",
        "Bienvenido a Sara. ¿En qué te puedo ayudar?"
        ]
    saludoAleatorio = random.choice(frases)
    decir(saludoAleatorio)

# Envio de correos
def enviarCorreo_Conexion(destinatario, contenido):
    servidorCorreo = smtplib.SMTP("smtp.gmail.com", 587)
    servidorCorreo.ehlo()
    servidorCorreo.starttls()
    servidorCorreo.login(correoEmisor, contraseñaCorreo)
    servidorCorreo.sendmail(correoEmisor, destinatario, contenido)
    servidorCorreo.close()

def enviarCorreo():
    try:
        decir("¿A quién se lo deseas enviar?")
        correoDestinatario = escucharOrden() + "@gmail.com"

        decir("¿Qué quieres que ponga en el mensaje?")
        contenido = escucharOrden()

        enviarCorreo_Conexion(correoDestinatario, contenido)
        decir("¡He enviado el correo")
    except Exception as error:
        print(error)
        decir(f"Lo siento {nombreUsuario}. Sucedió un error y no pude enviar tu correo.")

# Acciones - Inicio
def saludoFormal():
    momentoDia = int(datetime.datetime.now().hour)
    saludoDia = ""
    
    if (momentoDia >= 0) and (momentoDia < 12):
        saludoDia = "¡Buenos días!"
    elif (momentoDia >= 12) and (momentoDia < 18):
        saludoDia = "¡Buenas tardes!"
    else:
        saludoDia = "¡Buenas noches!"
    decir(saludoDia)

def despedida():
    decir(f"Adiós {nombreUsuario}")
    sys.exit()

def saludar():
    decir(f"Hola {nombreUsuario}")

def internet(pagina, ordenUsuario):
    direccion = ""
    cuest = ""
    palabra = ""
    solicitud = ordenUsuario.split()[-1]

    if (pagina == "google"):
        palabra = "Gugol"
        direccion = "https://www.google.com/search?q="

    elif (pagina == "youtube"):
        palabra = "Yutub"
        direccion = "https://www.youtube.com/results?search_query="

    elif (pagina == "maps"):
        direccion = "https://www.google.com/maps/place/"
        decir("Estoy abriendo Gugol Maps para mostrarte la ubicacion de" + solicitud)

    else:
        decir(f"Perdón {nombreUsuario}. No logre encontrar una respuesta a lo que pediste. Lo buscare en Gugol.")
        ans = ordenUsuario
        direccion = "https://www.google.com/search?q="
        busqueda = direccion + ans
        webbrowser.open(busqueda)
        return
    
    if (solicitud != pagina):
        cuest = solicitud
    else:
        decir(f"¿Qué te gustaría que buscara en {palabra}?")
        cuest = escucharOrden()
    
    busqueda = direccion + cuest
    webbrowser.open(busqueda)
    fraseConfirmacion()

def musica():
    directorio = os.path.expanduser("~") + "\\Music\\Gorillaz\\Humanz - (2017)"
    canciones = ["'10. Andromeda (feat. D.R.A.M.).mp3'", "'03. Strobelite (feat. Peven Everett).mp3'"]
    os.chdir(directorio)
    os.system(random.choice(canciones))
    fraseConfirmacion()

def horaActual():
    hora = datetime.datetime.now().strftime("%#I:%M:%p")
    decir(f"Son las {hora}")

def reiniciar():
    decir("Reiniciando sistema...")
    os.execl(sys.executable, sys.executable, *sys.argv)

def editor():
    codePath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
    os.startfile(codePath)
    fraseConfirmacion()

def respuestaDesconocida(alternativa, ordenUsuario):
    decir("Realmente no lo sé. Quieres que intente buscarlo por medios externos?")
    respuesta = escucharOrden()

    if ("si" in respuesta) or ("sí" in respuesta):
        try:
            alternativa(ordenUsuario)
        except:
            internet("error", ordenUsuario)
    else:
        decir("Vale")

def wolfram(ordenUsuario):
    orden = ordenUsuario.split("cuánto es ")
    res = solicitud_WolframAlpha.query(orden)
    results = next(res.results).text
    decir("Lo tengo! Según Wolfram-Alpha...")
    decir(results)
            
def wiki(ordenUsuario):
    results = wikipedia.summary(ordenUsuario, sentences=2)
    decir("Lo tengo! Según Wikipedia...")
    decir(results)
# Acciones - Fin

# Ejecucion Sara
if __name__ == "__main__":
    saludoFormal()
    fraseSaludo()
    
    while True:
        ordenUsuario = escucharOrden().lower()
        if ("adiós" in ordenUsuario) or ("apagate" in ordenUsuario):
            despedida()

        elif ("hola" in ordenUsuario):
            saludar()

        elif ("gracias" in ordenUsuario):
            fraseAgradecimiento()

        elif ("youtube" in ordenUsuario) or ("Youtube" in ordenUsuario):
            internet("youtube", ordenUsuario)

        elif ("google" in ordenUsuario) or ("Google" in ordenUsuario):
            internet("google", ordenUsuario)

        elif ("música" in ordenUsuario):
            musica()

        elif ("hora" in ordenUsuario):
            horaActual()

        elif ("reiniciate" in ordenUsuario):
            reiniciar()

        elif ("editor" in ordenUsuario):
            editor()

        elif ("dónde queda" in ordenUsuario) or ("dónde está" in ordenUsuario):
            internet("maps", ordenUsuario)

        elif ("correo" in ordenUsuario):
            enviarCorreo()
        
        elif ("quién es" in ordenUsuario) or ("qué es" in ordenUsuario) or ("qué fue" in ordenUsuario):
            respuestaDesconocida(wiki, ordenUsuario)

        elif ("cuánto es" in ordenUsuario):
            respuestaDesconocida(wolfram, ordenUsuario)