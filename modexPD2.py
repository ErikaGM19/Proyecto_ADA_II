import math

# Función para calcular el extremismo
def calcular_extremismo(opiniones):
    n = len(opiniones)
    if n == 0:
        return 0.0  # Evitar división por cero si no hay agentes

    suma_cuadrados = sum(opinion ** 2 for opinion in opiniones)
    extremismo = math.sqrt(suma_cuadrados)
    return extremismo/n

#Función para calcular el esfuerzo de aplicar la estrategia
def calcular_esfuerzo(opinion, receptividad):
    return math.ceil(abs(opinion) * (1 - receptividad))

def programacion_dinamica(agentes, R_max):
    n = len(agentes)
    # Inicializar la tabla ex_min
    ex_min = [[float('inf')] * (R_max + 1) for _ in range(n + 1)]
    opiniones = [agente[0] for agente in agentes]
    receptividades = [agente[1] for agente in agentes]

    ex_min[0][0] = calcular_extremismo(opiniones)  # Con 0 agentes y 0 esfuerzo, el extremismo es el original

    # Llenar la tabla ex_min
    for i in range(1, n + 1):
        for j in range(R_max + 1):

            # Caso 1: Moderar al agente i-1
            esfuerzo_moderar = calcular_esfuerzo(opiniones[i-1], receptividades[i-1])
            if j >= esfuerzo_moderar:  # Si hay suficiente esfuerzo para moderar
                # Crear una nueva lista de opiniones moderadas
                nuevas_opiniones = opiniones[:]
                nuevas_opiniones[i-1] = 0  # Moderar la opinión del agente i-1
                nuevo_extremismo = calcular_extremismo(nuevas_opiniones)

                # Actualizar la tabla ex_min para reflejar el nuevo extremismo con la moderación
                ex_min[i][j] = min(ex_min[i-1][j], ex_min[i-1][j - esfuerzo_moderar])

                # Solo actualizar si se ha utilizado el esfuerzo
                if j - esfuerzo_moderar >= 0:
                    ex_min[i][j] = min(ex_min[i][j], nuevo_extremismo)
            else:
                # Caso 2: No moderar al agente i-1
                ex_min[i][j] = ex_min[i-1][j]  # Mantener el extremismo sin cambios

    # El mínimo extremismo alcanzable 
    return ex_min, ex_min[n][R_max]

with open('Pruebas/Prueba1.txt', 'r') as file:
    lines = file.readlines()

num_rs = int(lines[0].strip())
rs = [eval(line.strip()) for line in lines[1:num_rs + 1]] 
r_max = int(lines[-1].strip())
print("Número de agentes:", num_rs)
# print("RS:", rs)
print("R_max:", r_max)

ex_min, solucion = programacion_dinamica(rs, r_max)

for fila in ex_min:
    print(fila)

print("El mínimo extremismo alcanzable es:", solucion)

#De momento solo calcula el mínimo extremismo