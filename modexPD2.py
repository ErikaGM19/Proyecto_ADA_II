import math

# Función para calcular el extremismo
def calcular_extremismo(opiniones):
    n = len(opiniones)
    if n == 0:
        return 0.0  # Evitar división por cero

    suma_cuadrados = sum(opinion ** 2 for opinion in opiniones)
    extremismo = math.sqrt(suma_cuadrados) / n
    return extremismo

# Función para calcular el esfuerzo para moderar un agente
def calcular_esfuerzo(opinion, receptividad):
    return math.ceil(abs(opinion) * (1 - receptividad))

def modexPD(red_social):
    agentes = red_social[0]
    R_max = int(red_social[1])

    n = len(agentes)
    opiniones = [agente[0] for agente in agentes]
    receptividades = [agente[1] for agente in agentes]

    # Inicializar la tabla dp y la tabla keep
    dp = [0] * (R_max + 1) 
    keep = [[False] * (R_max + 1) for _ in range(n)]

    esfuerzos = [calcular_esfuerzo(opiniones[i], receptividades[i]) for i in range(n)]
    valores = [opiniones[i] ** 2 for i in range(n)]

    # Para cada agente
    for i in range(n):
        effort_i = esfuerzos[i]
        value_i = valores[i]

        for j in range(R_max, effort_i - 1, -1):
            if dp[j - effort_i] + value_i > dp[j]:
                    dp[j] = dp[j - effort_i] + value_i
                    keep[i][j] = True

    # Encontrar el valor máximo dp[n][j] para j <= R_max
    max_value = max(dp)
    esfuerzo_utilizado = dp.index(max_value)
   

    # Reconstruir la estrategia óptima
    estrategia = [0] * n
    j = esfuerzo_utilizado
    for i in range(n - 1, -1, -1):
        if keep[i][j]:
            estrategia[i] = 1
            j -= esfuerzos[i]
            if j < 0:
                break  # Evitar índices negativos
        else:
            estrategia[i] = 0  # No moderar este agente

   # Calcular el esfuerzo total utilizado
    esfuerzo_total = sum(esfuerzos[i] for i in range(n) if estrategia[i] == 1)

    # Aplicar la estrategia para obtener las opiniones moderadas
    opiniones_moderadas = [0 if estrategia[i] == 1 else opiniones[i] for i in range(n)]

    # Calcular el extremismo final
    extremismo_final = calcular_extremismo(opiniones_moderadas)

    return [estrategia, esfuerzo_total, extremismo_final]