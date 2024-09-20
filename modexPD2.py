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

def programacion_dinamica(agentes, R_max):
    n = len(agentes)
    opiniones = [agente[0] for agente in agentes]
    receptividades = [agente[1] for agente in agentes]

    # Calcular la suma total de los cuadrados
    total_sum = sum(opinion ** 2 for opinion in opiniones)

    # Inicializar la tabla dp y la tabla keep
    dp = [[0] * (R_max + 1) for _ in range(n + 1)]
    keep = [[False] * (R_max + 1) for _ in range(n + 1)]

    # Para cada agente
    for i in range(1, n + 1):
        o_i = opiniones[i - 1]
        r_i = receptividades[i - 1]
        effort_i = calcular_esfuerzo(o_i, r_i)
        value_i = o_i ** 2

        for j in range(R_max + 1):
            if effort_i <= j:
                if dp[i - 1][j - effort_i] + value_i > dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j - effort_i] + value_i
                    keep[i][j] = True
                else:
                    dp[i][j] = dp[i - 1][j]
                    keep[i][j] = False
            else:
                dp[i][j] = dp[i - 1][j]
                keep[i][j] = False

    # Encontrar el valor máximo dp[n][j] para j <= R_max
    max_value = 0
    best_j = 0
    for j in range(R_max + 1):
        if dp[n][j] > max_value:
            max_value = dp[n][j]
            best_j = j

    # Reconstruir la solución
    j = best_j
    E = [0] * n  # Estrategia, 1 si el agente es moderado, 0 en caso contrario
    for i in range(n, 0, -1):
        if keep[i][j]:
            E[i - 1] = 1
            o_i = opiniones[i - 1]
            r_i = receptividades[i - 1]
            effort_i = calcular_esfuerzo(o_i, r_i)
            j -= effort_i

    # Ahora, calcular el extremismo después de aplicar la estrategia E
    moderated_opinions = []
    total_effort = 0
    for i in range(n):
        if E[i] == 1:
            moderated_opinions.append(0)
            o_i = opiniones[i]
            r_i = receptividades[i]
            effort_i = calcular_esfuerzo(o_i, r_i)
            total_effort += effort_i
        else:
            moderated_opinions.append(opiniones[i])

    extremism = calcular_extremismo(moderated_opinions)

    return E, total_effort, extremism

# Leer entrada desde archivo
with open('Pruebas/Prueba17.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())
agentes = []
for i in range(1, n + 1):
    line = lines[i].strip()
    if line:
        op, recep = line.split(',')
        agentes.append((int(op), float(recep)))

R_max = int(lines[-1].strip())

print("Número de agentes:", n)
print("Agentes:", agentes)
print("R_max:", R_max)

E, total_effort, extremism = programacion_dinamica(agentes, R_max)

print("Estrategia E:", E)
print("Esfuerzo total:", total_effort)
print("Extremismo:", extremism)
