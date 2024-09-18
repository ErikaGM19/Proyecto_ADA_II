from math import ceil
from modexFB import moderar, calcular_extremismo, calcular_esfuerzos
     

def obtener_estrategia(red_social, lista_agentes_por_esfuerzo):
    agentes_en_red_social = red_social[0]
    estrategia = [0] * len(agentes_en_red_social)
    
    # Iterar sobre los agentes en red_social
    for i, agente in enumerate(agentes_en_red_social):
        # Si el agente está en lista_agentes_por_esfuerzo, marcar con 1
        if agente in lista_agentes_por_esfuerzo:
            estrategia[i] = 1
    
    return estrategia

def extraccion_basada_en_esfuerzo(red_social):
    # Extraer la lista de agentes del primer elemento de red_social
    agentes = red_social[0]
    esfuerzo_max = red_social[1]
    
    # Ordenar los agentes primero por receptividad (descendente) y luego por opinión (descendente)
    agentes_ordenados = sorted(agentes, key=lambda x: (-x[1], -x[0]))
    
    # Iniciar una lista para almacenar los agentes seleccionados
    lista_agentes_por_esfuerzo = []
    esfuerzo_acumulado = 0
    estrategia_actual = []
    
    # Iterar sobre los rangos de receptividad, de 1.0 a 0.1 en pasos de 0.1
    for agente in agentes_ordenados:
        try:
            # Calculamos el esfuerzo acumulado si agregamos este agente
            estrategia_actual = obtener_estrategia(red_social, lista_agentes_por_esfuerzo + [agente])
            nuevo_esfuerzo = sum(calcular_esfuerzos(red_social, estrategia_actual))

            # Si no excedemos el esfuerzo máximo, añadimos al agente
            if nuevo_esfuerzo <= esfuerzo_max:
                lista_agentes_por_esfuerzo.append(agente)
                esfuerzo_acumulado = nuevo_esfuerzo
            else:
                # Si el esfuerzo excede, dejamos de añadir agentes
                break

        except IndexError as e:
            print(f"Error de índice: {str(e)} al procesar agente {agente}")
            continue

    # Si no se encuentra una combinación válida, devolver los agentes seleccionados hasta ahora
    return lista_agentes_por_esfuerzo

def modexV(red_social):
    try:
        lista_optimizada = extraccion_basada_en_esfuerzo(red_social)
        estrategia = obtener_estrategia(red_social, lista_optimizada)

        #from modexFB import moderar, calcular_extremismo
        esfuerzo=sum(calcular_esfuerzos(red_social,estrategia))
        red_social_moderada = moderar(red_social, estrategia)
        extremismo = calcular_extremismo(red_social_moderada)
 
        return [estrategia, esfuerzo, extremismo]
    except Exception as e:
        print(f"Error al ejecutar modexV: {str(e)}")
        return None 