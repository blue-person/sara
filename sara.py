import speech_recognition as sr
import pyttsx3 as ptt
import os, sys, datetime, webbrowser, random, wikipedia, wolframalpha, unidecode
from servicios import variables_entorno

# Variables
nombre_usuario = "Usuario"
lista_despedidas = ["adios", "hasta luego", "hasta pronto", "hasta mañana"]
lista_saludos = ["hola", "buenos dias", "buenas tardes", "buenas noches"]
lista_agradecimientos = ["gracias"]
lista_youtube = ["youtube", "yutub", "yutube", "yutube.com", "videos"]
lista_google = ["google", "gugol", "gugol.com", "buscar"]
lista_musica = ["pon musica", "musica", "reproduce", "reproduce musica"]
lista_ubicaciones = ["donde esta", "donde queda", "donde esta ubicado"]
lista_wikipedia = ["quien es", "que es", "que fue", "que paso en"]
lista_calculo = ["cuanto da", "cuanto es"]

# Configuracion de la voz
if sys.platform == "win32":
    dialogo_sara = ptt.init(driverName="sapi5")
    lista_voces = dialogo_sara.getProperty("voices")
    voz = lista_voces[0].id
elif sys.platform == "darwin":
    dialogo_sara = ptt.init(driverName="nsss")
    voz = "es-la+f5"
else:
    dialogo_sara = ptt.init(driverName="espeak")
    voz = "es-la+f5"

# Configuracion de servicios
cliente_wolfram = wolframalpha.Client(variables_entorno.API_WOLFRAM)
wikipedia.set_lang("es")


# Funciones principales
def decir_mensaje(mensaje):
    dialogo_sara.say(mensaje)
    dialogo_sara.runAndWait()


def escuchar_microfono():
    reconocimiento_voz = sr.Recognizer()

    with sr.Microphone() as microfono:
        print("Ajustando micrófono...\n")
        reconocimiento_voz.adjust_for_ambient_noise(microfono, duration=0.5)
        print("Micrófono listo. Estoy lista para escucharte\n")
        audio = reconocimiento_voz.listen(microfono)

    try:
        print("Procesando mensaje...\n")
        consulta_usuario = reconocimiento_voz.recognize_google(
            audio, language="es-US")
        return consulta_usuario
    except sr.UnknownValueError:
        decir_mensaje(
            "No he entendido bien lo que me pediste, di eso de nuevo por favor"
        )
        escuchar_microfono()


# Seleccion de frases
def frases_confirmacion():
    lista_frases = ["Con gusto", "Vale", "De inmediato", "Claro", "Ok"]
    frase_seleccionada = random.choice(lista_frases)
    decir_mensaje(frase_seleccionada)


def frases_agradecimiento():
    lista_frases = ["No te preocupes", "De nada", "No hay de qué", "Con gusto"]
    frase_seleccionada = random.choice(lista_frases)
    decir_mensaje(frase_seleccionada)


def frases_saludo():
    lista_frases = [
        f"Hola {nombre_usuario}, soy Sara. ¿Como puedo ayudarte?",
        f"Hola {nombre_usuario}. ¿En qué puedo ayudarte?",
        "¿Qué puedo hacer por ti?", "Bienvenido. ¿En qué te puedo ayudar?"
    ]
    frase_seleccionada = random.choice(lista_frases)
    decir_mensaje(f"{momento_dia()}. {frase_seleccionada}")


# Habilidades
def momento_dia():
    hora = int(datetime.datetime.now().hour)

    if (hora >= 6) and (hora < 12):
        return "¡Buenos días!"
    elif (hora >= 12) and (hora < 19):
        return "¡Buenas tardes!"
    else:
        return "¡Buenas noches!"


def despedirse():
    decir_mensaje(f"Adiós {nombre_usuario}")


def poner_musica():
    webbrowser.open(
        "https://www.youtube.com/watch?v=zisuhZqTeH4&list=PLp22EiLpMLDdvp6C4W2plwhyoAF-pXASA"
    )
    frases_confirmacion()


def buscar_internet(pagina, consulta_usuario):
    direccion = ""
    palabra = ""
    solicitud_busqueda = ""
    solicitud = consulta_usuario.split()[-1]

    if pagina == "google":
        palabra = "Gugol"
        direccion = "https://www.google.com/search?q="
    elif pagina == "youtube":
        palabra = "Yutub"
        direccion = "https://www.youtube.com/results?search_query="
    elif pagina == "maps":
        direccion = "https://www.google.com/maps/place/"
        decir_mensaje(
            "Estoy abriendo Gugol Maps para mostrarte la ubicacion de" +
            solicitud)
    else:
        decir_mensaje(
            f"Perdón {nombre_usuario}. No logre encontrar una respuesta a lo que pediste. Lo buscare en Gugol."
        )
        direccion = "https://www.google.com/search?q="
        busqueda = direccion + consulta_usuario
        webbrowser.open(busqueda)

    if solicitud == pagina:
        decir_mensaje(f"¿Qué te gustaría que buscara en {palabra}?")
        solicitud_busqueda = escuchar_microfono()
    else:
        solicitud_busqueda = solicitud

    busqueda = direccion + solicitud_busqueda
    webbrowser.open(busqueda)
    frases_confirmacion()


def realizar_calculo(orden_usuario):
    orden = orden_usuario.split("cuanto es ")
    solicitud = cliente_wolfram.query(orden)
    resultado = next(solicitud.results).text
    decir_mensaje(f"Lo tengo! Según Wolfram-Alpha {orden} es {resultado}")


def buscar_wikipedia(orden_usuario):
    resultado = wikipedia.summary(orden_usuario, sentences=2)
    decir_mensaje(f"Lo tengo! Según Wikipedia... {resultado}")


def respuesta_desconocida(funcion_alternativa, orden_usuario):
    lista_frases = ["si", "ok", "claro", "de inmediato", "vale"]

    decir_mensaje(
        "Realmente no lo sé. Quieres que intente buscarlo por medios externos?"
    )
    respuesta = escuchar_microfono()

    if respuesta in lista_frases:
        try:
            funcion_alternativa(orden_usuario)
        except:
            buscar_internet("error", orden_usuario)
    else:
        decir_mensaje("Vale")


def decir_hora_actual():
    hora = datetime.datetime.now().strftime("%#I:%M:%p")
    decir_mensaje(f"Son las {hora}")


def reiniciar():
    decir_mensaje("Reiniciandome...")
    despedirse()
    os.execl(sys.executable, sys.executable, *sys.argv)


# Nucleo
if __name__ == "__main__":
    frases_saludo()

    while True:
        orden_usuario = unidecode.unidecode(escuchar_microfono().lower())

        if orden_usuario in lista_despedidas:
            despedirse()
            break

        elif orden_usuario in lista_saludos:
            frases_saludo()

        elif orden_usuario in lista_agradecimientos:
            frases_agradecimiento()

        elif orden_usuario in lista_youtube:
            buscar_internet("youtube", orden_usuario)

        elif orden_usuario in lista_google:
            buscar_internet("google", orden_usuario)

        elif orden_usuario in lista_ubicaciones:
            buscar_internet("maps", orden_usuario)

        elif orden_usuario in lista_calculo:
            respuesta_desconocida(realizar_calculo, orden_usuario)

        elif orden_usuario in lista_wikipedia:
            respuesta_desconocida(buscar_wikipedia, orden_usuario)

        elif orden_usuario in lista_musica:
            poner_musica()

        elif ("hora" in orden_usuario):
            decir_hora_actual()

        elif ("reiniciate" in orden_usuario):
            reiniciar()
