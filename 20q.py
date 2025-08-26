dataset={'pregunta':'¿Es una idea, emoción, sentimiento',#1
         'si':{'pregunta':'¿?',#2
               'si':'',
               'no':''},
         'no':{'pregunta':'¿Está en el planeta Tierra?',#2
               'si':{'pregunta': '¿Está creado por el hombre?',#3
                     'si': {'pregunta':'¿Es una herramienta?',#4
                            'si':{},
                            'no':{}},
                     'no': ''},
               'no':{'pregunta': ''}}}

def jugar():
    print("Bienvenido a 20Q. Piensa en algo y yo adivinaré\nResponde con si(s) o no(n):")
    
    nodo = dataset
    while isinstance(nodo,dict):
        respuesta=input(f"{nodo['pregunta']}: Sí(s) o No(n)").lower()

        if respuesta == 's':
            nodo = nodo['si']
        elif respuesta == 'no':
            nodo = nodo['no']
        else:
            print("Por favor responde con solo \'s\' o \'n\'")
            continue
    
    respuesta = nodo

    print(f"La respuesta es {respuesta}")

jugar()