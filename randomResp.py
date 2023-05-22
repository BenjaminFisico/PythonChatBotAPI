import random

# Devuelve un string de la lista, selecionado de forma aleatoria.
def random_string():
    random_list = [
        "Lo siento, no puedo entender lo que estas tratando de decir. ¿Podrías reformular tu mensaje de manera mas clara?.",
        "Parece que hay algun tipo de error en tu mensaje. Podrias verificarlo y enviarmelo nuevamente, por favor.",
        "No logro comprender la informacion que me estás proporcionando. ¿Podrias darme mas detalles o explicarlo de otra manera?",
        "Parece que hay un problema de comunicacion aqui. ¿Podrias explicar tu mensaje de forma mas sencilla o utilizar palabras diferentes?.",
        "Lamento la confusion, pero no puedo interpretar completamente tu mensaje. ¿Podrias elaborar un poco mas para que pueda entenderlo mejor?."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]