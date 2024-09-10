import itertools
from math import ceil, sqrt

#red_social = list([((100, 0.5), (100, 0.1), (-10, 0.1)), 55])

def calcular_estrategias(red_social): # Hace todas las posibles combinaciones
    num_agentes = len(red_social[0]) # Tomamos el primer elemento de red_social (la lista de agentes) y contamos cuántos elementos tiene
    estrategias = list(itertools.product([0, 1], repeat=num_agentes)) # Generamos todas las combinaciones posibles de 0 y 1 con tamaño igual al número de agentes
    estrategias = [list(estrategia) for estrategia in estrategias] # Convertimos las tuplas generadas en listas
    return estrategias

def calcular_esfuerzos(red_social, estrategia):
    agentes = red_social[0]  # Lista de agentes (opinión y receptividad)
    esfuerzos = []  # Aquí almacenamos los resultados de esfuerzo

    # Recorremos cada agente y aplicamos la fórmula según la estrategia
    for i in range(len(agentes)):
        opinion_agente = agentes[i][0]
        receptividad_agente = agentes[i][1]
        
        if estrategia[i] == 1: # Si la estrategia indica aplicar el esfuerzo (1), aplicamos la fórmula
            esfuerzo = ceil(abs(opinion_agente) * (1 - receptividad_agente))
        else: # Si la estrategia indica no aplicar el esfuerzo (0), el esfuerzo es 0
            esfuerzo = 0   
                 
        esfuerzos.append(esfuerzo) # Guardamos el esfuerzo calculado
    
    return esfuerzos
        
    
def moderar(red_social, estrategia):
    r_max = red_social[1]  # Obtener el valor de R_max (esfuerzo máximo permitido)
    suma_esfuerzos_red = sum(calcular_esfuerzos(red_social, estrategia))  # Calcular la suma de esfuerzos

    if suma_esfuerzos_red <= r_max: # Validar si la suma de esfuerzos es menor o igual a r_max
        
        agentes = list(red_social[0])  # Los agentes son el primer elemento de la lista red_social
        nueva_red_social = [] # Crear una nueva red social modificada según la estrategia
        
        for i, (opinion, receptividad) in enumerate(agentes):
            if estrategia[i] == 1: # Si la estrategia indica moderar (1), cambiamos la opinión a 0
                nueva_red_social.append((0, receptividad)) 
            else: # Si no, dejamos la opinión original
                nueva_red_social.append((opinion, receptividad))

        return [tuple(nueva_red_social), r_max] # Devolver la nueva red social con las opiniones moderadas, es decir convertidas en 0 
    else: # Si el esfuerzo excede r_max, devolver una lista vacía
        return []
    
    
def extraer_opiniones(red_social):
    opiniones = [agente[0] for agente in red_social[0]] # Extrae los primeros elementos (opiniones) de cada agente en red_social[0]
    return opiniones
    
    
def calcular_extremismo(red_social):
    opiniones = extraer_opiniones(red_social)  # Extraemos las opiniones
    suma_cuadrados = sum([opinion**2 for opinion in opiniones])  # Elevamos al cuadrado cada opinión y sumamos
    extremismo = sqrt(suma_cuadrados) / len(opiniones)  # Calculamos la raíz cuadrada y dividimos por el número de agentes
    return extremismo    
    
    
def modexFB(red_social):
    lista_de_estrategias = calcular_estrategias(red_social) # Paso 1: Generar la lista de todas las estrategias posibles
    respuestas = [] # Inicializamos la lista de respuestas que almacenará [estrategia, esfuerzo, extremismo]
    
    for estrategia in lista_de_estrategias: # Paso 2: Recorremos cada estrategia en la lista
        lista_de_esfuerzos = calcular_esfuerzos(red_social, estrategia) # Calcular los esfuerzos de la estrategia actual
        esfuerzo_total = sum(lista_de_esfuerzos)
        
        if esfuerzo_total <= red_social[-1]: # Verificar si el esfuerzo total no excede el esfuerzo máximo permitido
            red_social_moderada = moderar(red_social, estrategia) # Si es válido, generamos la nueva red social moderada
            
            extremismo = calcular_extremismo(red_social_moderada) # Calcular el extremismo de la nueva red social moderada
            
            respuesta = [estrategia, esfuerzo_total, extremismo] # Almacenamos la estrategia, esfuerzo y extremismo en la lista de respuestas
            respuestas.append(respuesta)
        else:
            continue # Si el esfuerzo total excede, no hacemos nada y continuamos con la siguiente estrategia
    
    if respuestas: # Paso 3: Seleccionar la estrategia con el menor extremismo
        mejor_respuesta = min(respuestas, key=lambda x: x[2])  # Busca la sublista con el menor extremismo
    else:
        mejor_respuesta = []  # Si no hay respuestas válidas, retornamos una lista vacía
    
    return mejor_respuesta

# Ejemplo de uso:
#red_social = [((100, 0.5), (100, 0.1), (-10, 0.1)), 55]
#resultado = modexFB(red_social)
#print(resultado)

