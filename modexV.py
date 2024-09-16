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
    estrategia_actual = []
    
    # Iterar sobre los rangos de receptividad, de 1.0 a 0.1 en pasos de 0.1
    for i in range(10):
        rango_max = 1.0 - (i * 0.1)
        rango_min = 0.0 - (i * 0.1)

        # Filtrar los agentes que caen dentro del rango actual
        agentes_en_rango = [agente for agente in agentes_ordenados if rango_min <= agente[1] <= rango_max]

        # Si hay agentes en este rango, añadirlos a lista_agentes_por_esfuerzo
        if agentes_en_rango:
            lista_agentes_por_esfuerzo += agentes_en_rango
            
            # Calcular la estrategia para los agentes seleccionados
            estrategia_actual = obtener_estrategia(red_social, lista_agentes_por_esfuerzo)
            
            # Calcular el esfuerzo basado en la estrategia actual
            esfuerzo = sum(calcular_esfuerzos(red_social,estrategia_actual))
            
            # Si el esfuerzo es menor o igual al máximo permitido, detener el ciclo y devolver los agentes
            if esfuerzo <= esfuerzo_max:
                return lista_agentes_por_esfuerzo
            else:
                # Si el esfuerzo es mayor al permitido, eliminar el agente con la receptividad más baja y recalcular
                while esfuerzo > esfuerzo_max and lista_agentes_por_esfuerzo:
                    # Eliminar el agente con la receptividad más baja (último agente de la lista, ya que está ordenada)
                    lista_agentes_por_esfuerzo.pop(-1)
                    
                    # Recalcular la estrategia y el esfuerzo
                    estrategia_actual = obtener_estrategia(red_social, lista_agentes_por_esfuerzo)
                    esfuerzo = sum(calcular_esfuerzos(red_social, estrategia_actual))

    # Si no se encuentra una combinación válida, devolver los agentes seleccionados hasta ahora
    return lista_agentes_por_esfuerzo

def modexV(red_social):
 lista_optimizada = extraccion_basada_en_esfuerzo(red_social)
 
 estrategia = obtener_estrategia(red_social, lista_optimizada)

 #from modexFB import moderar, calcular_extremismo
 esfuerzo=sum(calcular_esfuerzos(red_social,estrategia))
 red_social_moderada = moderar(red_social, estrategia)
 extremismo = calcular_extremismo(red_social_moderada)
 return [estrategia, esfuerzo, extremismo]