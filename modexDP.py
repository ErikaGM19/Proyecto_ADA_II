import math

def calcular_extremismo(agentes, estrategia):
    """
    Calcula el nivel de extremismo de una red social dada una estrategia de moderación.
    """
    n = len(agentes)
    extremismo = 0
    for i in range(n):
        opinion, _ = agentes[i]
        if estrategia[i] == 0:  # No se modera
            extremismo += opinion ** 2
    return math.sqrt(extremismo / n)

def calcular_esfuerzo(agentes, estrategia):
    """
    Calcula el esfuerzo necesario para aplicar una estrategia de moderación.
    """
    esfuerzo_total = 0
    for i in range(len(agentes)):
        opinion, receptividad = agentes[i]
        if estrategia[i] == 1:  # Se modera
            esfuerzo_total += abs(opinion) * (1 - receptividad)
    return esfuerzo_total

def modexPD(agentes, R_max):
    """
    Resuelve el problema de moderación de extremismo usando programación dinámica.
    """
    n = len(agentes)

    # Inicializamos la matriz DP, donde dp[i][e] representa el extremismo mínimo moderando los primeros i agentes con esfuerzo e
    dp = [[float('inf')] * (R_max + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Si no hay agentes, no hay extremismo.

    # Matriz para reconstruir la solución
    decision = [[0] * (R_max + 1) for _ in range(n + 1)]

    # Programación dinámica
    for i in range(1, n + 1):
        opinion, receptividad = agentes[i - 1]
        esfuerzo_moderar = abs(opinion) * (1 - receptividad)

        for e in range(R_max + 1):
            # Caso 1: No moderar al agente i-ésimo
            dp[i][e] = dp[i - 1][e]  # Copiamos la solución anterior sin moderar

            # Caso 2: Moderar al agente i-ésimo, si el esfuerzo es suficiente
            if e >= esfuerzo_moderar:
                # Calculamos el extremismo restando el efecto del agente actual si lo moderamos
                nuevo_extremismo = dp[i - 1][int(e - esfuerzo_moderar)] - (opinion ** 2 / n)
                if nuevo_extremismo < dp[i][e]:
                    dp[i][e] = nuevo_extremismo
                    decision[i][e] = 1  # Decidimos moderar este agente

    # Buscar el esfuerzo óptimo que minimiza el extremismo
    esfuerzo_optimo = R_max
    for e in range(R_max + 1):
        if dp[n][e] < dp[n][esfuerzo_optimo]:
            esfuerzo_optimo = e

    # Reconstruir la estrategia óptima
    estrategia_optima = [0] * n
    e = esfuerzo_optimo
    for i in range(n, 0, -1):
        if decision[i][e] == 1:
            estrategia_optima[i - 1] = 1
            opinion, receptividad = agentes[i - 1]
            e -= int(abs(opinion) * (1 - receptividad))

    # Calcular el extremismo y esfuerzo final
    extremismo_final = calcular_extremismo(agentes, estrategia_optima)
    esfuerzo_final = calcular_esfuerzo(agentes, estrategia_optima)

    return estrategia_optima, esfuerzo_final, extremismo_final

# Función para leer entradas desde archivo de texto
def leer_entrada(archivo_entrada):
    with open(archivo_entrada, 'r') as f:
        n = int(f.readline().strip())
        agentes = []
        for _ in range(n):
            opinion, receptividad = map(float, f.readline().strip().split(','))
            agentes.append((opinion, receptividad))
        R_max = int(f.readline().strip())
    return agentes, R_max

# Función para escribir la salida en archivo de texto
def escribir_salida(archivo_salida, extremismo, esfuerzo, estrategia):
    with open(archivo_salida, 'w') as f:
        f.write(f"{extremismo:.2f}\n")
        f.write(f"{esfuerzo:.2f}\n")
        for mod in estrategia:
            f.write(f"{mod}\n")

# Ejemplo de uso
if __name__ == "__main__":
    # Leer los datos de entrada desde un archivo
    agentes, R_max = leer_entrada('entrada.txt')

    # Calcular la estrategia óptima usando programación dinámica
    estrategia, esfuerzo, extremismo = modexPD(agentes, R_max)

    # Escribir los resultados en un archivo de salida
    escribir_salida('salida.txt', extremismo, esfuerzo, estrategia)
