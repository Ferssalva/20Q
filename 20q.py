import json

def jugar():
    print("Bienvenido a 20Q. Piensa en algo y yo adivinaré\nResponde con si(s) o no(n):")
    with open('dataset.json', 'r', encoding='utf-8') as data:
        dataset = json.load(data)
    
    nodo=dataset
    while isinstance(nodo,dict):
        respuesta=input(f"{nodo['pregunta']}: Sí(s) o No(n): ").lower()

        if respuesta == 's':
            nodo = nodo['si']
        elif respuesta == 'n':
            nodo = nodo['no']
        else:
            print("Por favor responde con solo \'s\' o \'n\'")
            continue
    
    respuesta = nodo

    print(f"La respuesta es {respuesta}")

jugar()