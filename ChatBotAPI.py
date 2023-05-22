from flask import Flask, request
from collections import namedtuple

import json
import re
import randomResp

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> PAGINA WEB PRINCIPAL </h1>'

@app.route('/api')
def api():
    user_input = request.args.get('input')
    response = generate_response(user_input)

    json = {
        'input': user_input,
        'response': response.response,
        'accuracy': response.accuracy
    }

    return json

Response = namedtuple('Response', 'response accuracy')

def load_json(file):
    """Leer los datos de un archivo .json

    Args:
        file (string): ruta del archivo
    
    Returns:
        list: Datos del archivo
    """
    with open(file) as botResp:
        print(f"Archivo '{file}' cargado")
        return json.load(botResp)

# Almacena los datos del chatbot 
responses_data = load_json("bot.json")

def generate_response(user_input) -> Response:
    """Calcula la respuesta mas adecuada posible para una entrada determinada, tomando los datos almacenados en responses_data

    Args:
        user_input (string): Cadena a analizar 

    Returns:
        namedtuple: Almacena el retorno en Response
    """

    inp = user_input.lower()
    split_message = re.split(r'\s+|[,;?!.-]\s*', inp)
    accuracy = []

    #Recorre todas las respuestas
    for response in responses_data:
        resp_accuracy = 0
        req_accuracy = 0
        required_words = response["required_words"]

        #Verifica si hay palabras obligatorias
        if required_words:
            #verifica cada coincidencia entre el mensaje del usuario y las palabras obligatorias
            for word in split_message:
                if word in required_words:
                    req_accuracy += 1

        #La cantidad de palabras obligatorias tiene que coincidir con la cantidad de aciertos
        if req_accuracy == len(required_words):
            for word in split_message:
                #Verifica cada palabra ingresada por el usuario y si esta coincide con la lista de user_input
                if word in response["user_input"]:
                    resp_accuracy += 1

        #Agrega la cantidad de coincidencias a una lista para poder comparar la mejor 
        accuracy.append(resp_accuracy)

    bestResp = max(accuracy)
    #Es importante notar que el indice de aciertos coincide con el indice de las respuestas.
    respIndex = accuracy.index(bestResp)

    if bestResp != 0:
        return Response(responses_data[respIndex]["bot_response"], bestResp)

    # Si los aciertos son igual a cero entonces el chatbot no tiene programada la respuesta
    return Response(randomResp.random_string(),0)


if __name__ == '__main__':
    app.run()

