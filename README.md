# Proyecto ADA II - Moderación del Extremismo de Opiniones en Redes Sociales

<p align='center'>
  <img width='200' heigth='225' src='https://user-images.githubusercontent.com/62605744/171186764-43f7aae0-81a9-4b6e-b4ce-af963564eafb.png'>
</p>



  Este repositorio contiene la implementación y análisis de varios algoritmos para la moderación del extremismo de opiniones en una red social. 
  El proyecto fue desarrollado como parte del curso **Análisis y Diseño de Algoritmos II (ADA II)**, de la **Universidad del Valle**. 
  Se han implementado tres enfoques principales: **Fuerza Bruta**, **Algoritmo Voraz**, y **Programación Dinámica**. 

## Estructura del Proyecto

### Algoritmos Implementados

- **Fuerza Bruta (`modexFB.py`)**:
    - Se prueban todas las posibles combinaciones de agentes y se selecciona la combinación que minimiza el extremismo en la red social.
    - Este algoritmo garantiza encontrar la solución óptima, pero es computacionalmente inviable para redes grandes debido a su alta complejidad temporal.

- **Algoritmo Voraz (`modexV.py`)**:
    - Selecciona los agentes a moderar basándose en un enfoque heurístico, eligiendo aquellos con la mayor receptividad en primer lugar.
    - Este enfoque es eficiente en tiempo, pero puede no encontrar siempre la solución óptima.

- **Programación Dinámica (`modexPD2.py`)**:
    - Utiliza un enfoque basado en subproblemas para encontrar una solución óptima de manera más eficiente que la Fuerza Bruta, en términos de tiempo.
    - Sin embargo, su implementación consume una cantidad significativa de memoria, lo que puede ser un inconveniente en redes muy grandes.

### Interfaz Gráfica

- **Interfaz (`interfaz_grafica.py`)**:
    - Implementa una aplicación gráfica en Python utilizando `Tkinter` para seleccionar pruebas y algoritmos.
    - Permite visualizar los resultados de las pruebas y la ejecución de los algoritmos en tiempo real.

### Pruebas

En la carpeta `Pruebas`, se incluyen más de 40 pruebas con diferentes configuraciones de agentes y valores de `Rmax`, que permiten evaluar el desempeño de los tres algoritmos implementados. Las pruebas se dividen en tres categorías:
- **Pruebas Pequeñas**: Redes con pocos agentes y valores bajos de `Rmax`.
- **Pruebas Medianas**: Redes de tamaño intermedio.
- **Pruebas Grandes**: Redes con un gran número de agentes y altos valores de `Rmax`.

### Resultados

Los resultados de las pruebas se encuentran documentados en el informe del proyecto, disponible en este repositorio bajo el archivo `Informe_proyecto1_ADAII.pdf`. Se han realizado análisis comparativos de los tres algoritmos en términos de:
- **Tiempo de ejecución**.
- **Optimalidad de la solución (extremismo final)**.
- **Eficiencia en memoria (en el caso de Programación Dinámica)**.

## Requisitos

Para ejecutar este proyecto localmente, necesitarás:
- **Python 3.x**
- Librerías adicionales que pueden instalarse usando pip:
    - `customtkinter`
    - `PIL` (librería Pillow)

Puedes instalar las dependencias necesarias ejecutando:
```bash
pip install -r requirements.txt
```

## Uso

### Interfaz Gráfica
1. Ejecuta el archivo `interfaz_grafica.py` para iniciar la aplicación gráfica:
   ```bash
   python interfaz_grafica.py
   ```

2. Selecciona la prueba que deseas cargar y el algoritmo a ejecutar.

3. El resultado de la prueba será mostrado en la interfaz, incluyendo la estrategia aplicada, el extremismo final, el esfuerzo total y el tiempo de ejecución.


## Equipo

Este proyecto fue desarrollado por el **Grupo 4** como parte del curso de ADA II.
**Integrantes:**
- Erika García Muñoz - 202259395
- Marcela Mazo Castro - 201843612
- Andres Mauricio Ortiz Bermudez -202110330
- Yissy Katherine Posso Perea - 202181910

## Profesores evaluadores

- Dr. Jesús Alexander Aranda
- Dr. Juan Francisco Díaz Frias

