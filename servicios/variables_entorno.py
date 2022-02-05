import dotenv, os


def cargar_variable(nombreVariable):
    archivo = "otros/.env"
    dotenv.load_dotenv(archivo)
    return os.getenv(nombreVariable)


API_WOLFRAM = cargar_variable("API_WOLFRAM")