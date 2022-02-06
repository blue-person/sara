# Sara

[![Project Status: Abandoned – Initial development has started, but there has not yet been a stable, usable release; the project has been abandoned and the author(s) do not intend on continuing development.](http://www.repostatus.org/badges/latest/abandoned.svg)](http://www.repostatus.org/#abandoned)

**Una asistente virtual para escritorio**

Sara es una asistente virtual simple que trabaja por medio de Python. Tiene la capacidad de comunicarse por medio de un motor de voz y reconocer las solicitudes del usuario por medio del micrófono. Puede realizar búsquedas en internet, decir la hora actual, poner música y demás.

## Estado del proyecto

Sara fue desarrollada cuando apenas estaba aprendiendo a programar, siendo siempre un proyecto sencillo que se desarrollaba lentamente según tenia nuevas ideas. Por lo anterior, el código es bastante desorganizado y tiende a fallar bastante.

#### Entonces, si es código defectuoso y problemático, ¿por que no lo eliminas y ya?

## Getting Started

In order to start Jarvis just clone [this repository](https://github.com/sukeesh/Jarvis.git) and run `python installer`.

Run **Jarvis** from anywhere by command `jarvis`

On Mac OS X run `source setup.sh`

On Windows run `setup.bat`

You can start by typing `help` within the Jarvis command line to check what Jarvis can do for you.


## Youtube Video Showing Jarvis

[Click here](https://www.youtube.com/watch?v=PR-nxqmG3V8)

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

### Plugins

[Click here](doc/PLUGINS.md) to learn more about plugins.

### Creating a test

Creating a test is optional but never a bad idea ;).

[Click here](doc/TESTING.md) to learn more about testing.

### How to run tests:

 Run `test.sh`
 ```bash
 ./test.sh
 ```
## Optional Dependencies

- Any pyttsx3 text-to-speech engine (``sapi5, nsss or espeak``) for Jarvis to talk out loud (e.g. Ubuntu do ``sudo apt install espeak``)
- Portaudio + python-devel packages for voice control
- ``notify-send`` on Linux if you want to receive *nice* and desktop-notification instead of *ugly* pop up windows (e.g. Ubuntu do ``sudo apt install libnotify-bin``)
- ``ffmpeg`` if you want ``music`` to download songs as .mp3 instead of .webm

## Docker

Run with docker (docker needs to be installed and running):

```
[sudo] make build_docker
[sudo] make run_docker
```

## Authors

 **Blue Bird**

See also the list of [contributors](https://github.com/sukeesh/Jarvis/graphs/contributors) who have participated in this project.

## Licencia

Este proyecto cuenta con la licencia Apache License 2.0 - vea el archivo [LICENSE](LICENSE) para más detalles
