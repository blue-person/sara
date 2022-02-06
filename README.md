# Sara

[![Project Status: Abandoned – Initial development has started, but there has not yet been a stable, usable release; the project has been abandoned and the author(s) do not intend on continuing development.](http://www.repostatus.org/badges/latest/abandoned.svg)](http://www.repostatus.org/#abandoned)

**Una asistente virtual para escritorio**

Sara es una asistente virtual simple que trabaja por medio de Python. Tiene la capacidad de comunicarse por medio de un motor de voz y reconocer las solicitudes del usuario por medio del micrófono. Puede realizar búsquedas en internet, decir la hora actual, poner música y demás.

## Estado del proyecto

Sara fue desarrollada cuando apenas estaba aprendiendo a programar, siendo siempre un proyecto sencillo que se desarrollaba lentamente según tenia nuevas ideas. Por lo anterior, el código es bastante desorganizado y tiende a fallar bastante.

### Entonces, si es código defectuoso y problemático, ¿por que no lo eliminas y ya?

Bueno, porque fue el primer programa que realmente me enorgulleció. Quiero conservarlo de alguna manera por mas que ya no vaya a trabajar en él, y considero que tener el código en GitHub es más útil que dejarlo en un .rar perdido en mis carpetas. Al menos aquí, si alguien lo encuentra, puede que le sea de utilidad para crear su propio proyecto.

### ¿Y por que no sigues trabajando en el código, así haces que sea más claro de entender y funcione mejor en general?

Es buena idea, tan buena que ya lo hice. Decidí expandir la idea y usar diversas ideas de Sara para crear un nuevo proyecto, la Familia Sara. Es un proyecto que busca crear diferentes asistentes virtuales y cada una que funcione para un caso específico, por ejemplo un bot para WhatsApp, otro que funcione en computadoras de escritorio y pueda recibir ordenes por micrófono, o incluso uno que sea una plantilla para crear cualquier tipo de bot pero solo sea necesario cambiar pocas partes del código.

Con el tiempo iré publicando estos bots, pero por ahora solo Sara estará disponible.

### Vale, ¿entonces cuando subirás los demás bots?

Esa **si** es una buena pregunta. Solo el tiempo lo dirá. 

## Getting Started

Para utilizar Sara lo primero que debe hacerse es clonar [este repositorio](https://github.com/BlueBird-BH/Sara.git) e instalar las dependencias a continuación. Se recomienda utilizar la última versión de Python 3.

### Dependencias
- ``unidecode``
- ``SpeechRecognition``
- ``pyttsx3``
- ``wikipedia``
- ``wolframalpha``
- ``PyAudio``*

#### Instalar PyAudio

Instalar PyAudio puede ser un poco más difícil que cualquier otra de las anteriores dependencias, pues se debe instalar un archivo en específico, pues debe ser descargado el archivo e instalado manualmente. 

#### Windows
En el casos de sistemas Windows, este archivo (para dispositivos de 64 bits) puede encontrarse en la carpeta [otros](https://github.com/BlueBird-BH/Sara/blob/main/otros/PyAudio-0.2.11-cp310-cp310-win_amd64.whl) del repositorio, sin embargo, de ser necesario se puede descargar manualmente desde la [siguiente pagina](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

Una vez descargado el archivo, debemos abrir una terminal donde tenemos el archivo y ejecutar el comando (la version de PyAudio puede variar) ``pip install PyAudio-x.x.x-cp3x-cp3x-winx.whl``

## Contributing

Check out our [CONTRIBUTING.md](CONTRIBUTING.md) to learn how you can contribute!

### QuickStart: Create a new feature (plugin)

Create new file custom/hello_world.py

```
from plugin import plugin


@plugin("helloworld")
def helloworld(jarvis, s):
    """Repeats what you type"""
    jarvis.say(s)
```

Check it out!
```
./jarvis
Jarvis' sound is by default disabled.
In order to let Jarvis talk out loud type: enable sound
Type 'help' for a list of available actions.

~> Hi, what can I do for you?
helloworld Jarvis is cool!
jarvis is cool
```

## Optional Dependencies

- Any pyttsx3 text-to-speech engine (``sapi5, nsss or espeak``) for Jarvis to talk out loud (e.g. Ubuntu do ``sudo apt install espeak``)
- Portaudio + python-devel packages for voice control
- ``notify-send`` on Linux if you want to receive *nice* and desktop-notification instead of *ugly* pop up windows (e.g. Ubuntu do ``sudo apt install libnotify-bin``)
- ``ffmpeg`` if you want ``music`` to download songs as .mp3 instead of .webm

## Autor

 **Blue Bird**
 
 Correo: bluebird.pbq@gmail.com

## Licencia

Este proyecto cuenta con la licencia Apache License 2.0 - vea el archivo [LICENSE](LICENSE) para más detalles
