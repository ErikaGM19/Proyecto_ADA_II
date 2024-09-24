import customtkinter as ctk # libreria encargada de la interfaz gráfica
import os 
import importlib.util
from tkinter import filedialog # Importación del módulo para abrir el diálogo de archivos
from PIL import Image, ImageTk  # Importar las clases Image y ImageTk de la librería Pillow
import time

# Inicializamos la aplicación y configuramos el tema
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue") 

# Crear la ventana principal
root = ctk.CTk() 
root.geometry("1000x600") # Tamaño inicial de la ventana
root.title("Proyecto I - ADA II - Grupo 4") 

# Variable global para almacenar las pruebas disponibles y los algoritmos
pruebas_disponibles = []
algoritmos_disponibles = []
prueba_seleccionada = None
algoritmo_seleccionado = None

# Función para cargar el archivo de prueba seleccionado
def cargar_archivo(prueba):
    try:
        carpeta_pruebas = "Pruebas"
        ruta_prueba = os.path.join(carpeta_pruebas, prueba)
        with open(ruta_prueba, "r") as archivo:
            datos_prueba = archivo.readlines()  # Leer todas las líneas del archivo
            datos_prueba = [line.strip() for line in datos_prueba]  # Limpiar espacios en blanco
            
            # Procesar los datos de la prueba
            num_agentes = int(datos_prueba[0])  # Primer número: cantidad de agentes
            agentes = []  # Lista para almacenar los agentes (opinión, receptividad)
            
            # Extraer las opiniones y receptividades de las siguientes líneas
            for i in range(1, num_agentes + 1):
                opinion, receptividad = map(float, datos_prueba[i].split(','))  # Separar por coma y convertir a float
                agentes.append((opinion, receptividad))
            
            r_max = float(datos_prueba[num_agentes + 1])  # Último número: valor de R_max

            # Crear la estructura esperada por el algoritmo
            red_social = (agentes, r_max)
            
            resultado_area.insert(ctk.END, f"Prueba cargada: {red_social}\n")  # Mostrar el contenido para depuración
            return red_social
    except Exception as e:
        resultado_area.insert(ctk.END, f"Error al cargar la prueba: {str(e)}\n")
        return None

# Definir las funciones de los algoritmos
def ejecutar_algoritmo(algoritmo):
    if not algoritmo_seleccionado:
        resultado_area.insert(ctk.END, "No se ha seleccionado un algoritmo.\n")
        return

    resultado_area.delete("1.0", ctk.END)  # Limpiar el área de resultados

    # Cargar los datos de la prueba seleccionada
    if prueba_seleccionada is None:
        resultado_area.insert(ctk.END, "No se ha seleccionado una prueba.\n")
        return

    red_social = cargar_archivo(prueba_seleccionada)
    if red_social is None:
        resultado_area.insert(ctk.END, "Error al cargar los datos de la prueba.\n")
        return

    if algoritmo == "Fuerza Bruta":
        try:
            # Verificar si modexFB.py existe y cargarlo dinámicamente
            if os.path.exists("modexFB.py"):
                spec = importlib.util.spec_from_file_location("modexFB", "./modexFB.py")
                modexFB = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(modexFB)

                # Ejecutar la función modexFB del archivo modexFB.py
                start_time = time.time()
                resultado = modexFB.modexFB(red_social)
                end_time = time.time()
                execution_time = end_time - start_time

                estrategia, esfuerzo_total, extremismo = resultado
                extremismo_inicial = modexFB.calcular_extremismo(red_social)
                agentes_moderados = sum(estrategia)
                agentes_totales = len(estrategia)

                resultado_area.insert(ctk.END, f"Resultado del algoritmo Fuerza Bruta:\n")
                resultado_area.insert(ctk.END, f"Estrategia aplicada: {estrategia}\n")
                resultado_area.insert(ctk.END, f"Esfuerzo total: {esfuerzo_total}\n")
                resultado_area.insert(ctk.END, f"Extremismo inicial: {extremismo_inicial}\n")
                resultado_area.insert(ctk.END, f"Extremismo final: {extremismo}\n")
                resultado_area.insert(ctk.END, f"Agentes moderados: {agentes_moderados}/{agentes_totales}\n")
                resultado_area.insert(ctk.END, f"Tiempo total de ejecución: {execution_time:.4f} segundos\n")

            else:
                resultado_area.insert(ctk.END, "El archivo modexFB.py no se encontró.\n")
        except Exception as e:
            resultado_area.insert(ctk.END, f"Error al ejecutar Fuerza Bruta: {str(e)}\n")
    
    elif algoritmo == "Voraz":
        try:
            # Verificar si modexV.py existe y cargarlo dinámicamente
            if os.path.exists("modexV.py"):
                spec = importlib.util.spec_from_file_location("modexV", "./modexV.py")
                modexV = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(modexV)

                # Ejecutar la función modexV del archivo modexV.py
                start_time = time.time()
                resultado = modexV.modexV(red_social)
                end_time = time.time() 
                execution_time = end_time - start_time

                estrategia, esfuerzo_total, extremismo = resultado
                extremismo_inicial = modexV.calcular_extremismo(red_social)
                agentes_moderados = sum(estrategia)
                agentes_totales = len(estrategia)

                resultado_area.insert(ctk.END, f"Resultado del algoritmo Voraz:\n")
                resultado_area.insert(ctk.END, f"Estrategia aplicada: {estrategia}\n")
                resultado_area.insert(ctk.END, f"Esfuerzo total: {esfuerzo_total}\n")
                resultado_area.insert(ctk.END, f"Extremismo inicial: {extremismo_inicial}\n")
                resultado_area.insert(ctk.END, f"Extremismo final: {extremismo}\n")
                resultado_area.insert(ctk.END, f"Agentes moderados: {agentes_moderados}/{agentes_totales}\n")
                resultado_area.insert(ctk.END, f"Tiempo total de ejecución: {execution_time:.4f} segundos\n")
                

            else:
                resultado_area.insert(ctk.END, "El archivo modexV.py no se encontró.\n")
        except Exception as e:
            resultado_area.insert(ctk.END, f"Error al ejecutar Voraz: {str(e)}\n")

    elif algoritmo == algoritmo == "Programación Dinámica":
        try:
            # Verificar si modexPD2.py existe y cargarlo dinámicamente
            if os.path.exists("modexPD2.py"):
                spec = importlib.util.spec_from_file_location("modexPD2", "./modexPD2.py")
                modexPD2 = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(modexPD2)

                # Ejecutar la función modexPD del archivo modexPD2.py
                start_time = time.time()
                resultado = modexPD2.modexPD(red_social)
                end_time = time.time()
                execution_time = end_time - start_time

                estrategia, esfuerzo_total, extremismo = resultado
                extremismo_inicial = modexPD2.calcular_extremismo([agente[0] for agente in red_social[0]])
                agentes_moderados = sum(estrategia)
                agentes_totales = len(estrategia)

                resultado_area.insert(ctk.END, f"Resultado del algoritmo Programación Dinámica:\n")
                resultado_area.insert(ctk.END, f"Estrategia aplicada: {estrategia}\n")
                resultado_area.insert(ctk.END, f"Esfuerzo total: {esfuerzo_total}\n")
                resultado_area.insert(ctk.END, f"Extremismo inicial: {extremismo_inicial}\n")
                resultado_area.insert(ctk.END, f"Extremismo final: {extremismo}\n")
                resultado_area.insert(ctk.END, f"Agentes moderados: {agentes_moderados}/{agentes_totales}\n")
                resultado_area.insert(ctk.END, f"Tiempo total de ejecución: {execution_time:.4f} segundos\n")

            else:
                resultado_area.insert(ctk.END, "El archivo modexPD2.py no se encontró.\n")
        except Exception as e:
            resultado_area.insert(ctk.END, f"Error al ejecutar Programación Dinámica: {str(e)}\n")

def seleccionar_algoritmo(algoritmo):
    global algoritmo_seleccionado
    algoritmo_seleccionado = algoritmo
    resultado_area.insert(ctk.END, f"Algoritmo seleccionado: {algoritmo}\n")

# Función para obtener todas las pruebas disponibles en la carpeta "Pruebas"
def obtener_pruebas():
    global pruebas_disponibles
    carpeta_pruebas = "Pruebas"
    try:
        # Listar los archivos .txt en la carpeta de pruebas
        pruebas_disponibles = [f for f in os.listdir(carpeta_pruebas) if f.endswith(".txt")]
        if pruebas_disponibles:
            pruebas_disponibles = sorted(pruebas_disponibles, key=lambda x: int(''.join(filter(str.isdigit, x))))
        else:
            pruebas_disponibles = ["No hay pruebas disponibles"]
    except FileNotFoundError:
        pruebas_disponibles = ["Carpeta 'Pruebas' no encontrada"]

# Función para actualizar las pruebas en el menú desplegable
def actualizar_pruebas_menu():
    obtener_pruebas()  # Obtener la lista de pruebas desde la carpeta
    opciones_pruebas.configure(values=pruebas_disponibles)  # Actualizar el menú desplegable con las pruebas disponibles

# Función para obtener los algoritmos disponibles en la carpeta "Algoritmos"
def obtener_algoritmos():
    global algoritmos_disponibles
    # Verificar si modexFB.py existe en la raíz
    if os.path.exists("modexFB.py"):
        algoritmos_disponibles.append("Fuerza Bruta")
    if os.path.exists("modexV.py"):
        algoritmos_disponibles.append("Voraz")
    if os.path.exists("modexPD2.py"):
        algoritmos_disponibles.append("Programación Dinámica")
    if not algoritmos_disponibles:
        algoritmos_disponibles = ["No hay algoritmos disponibles"]

# Función para actualizar el menú de algoritmos
def actualizar_algoritmos_menu():
    obtener_algoritmos()  # Obtener la lista de algoritmos desde la carpeta
    opciones_algoritmos.configure(values=algoritmos_disponibles)  # Actualizar el menú desplegable con los algoritmos disponibles

# Función para seleccionar una prueba
def seleccionar_prueba(prueba):
    global prueba_seleccionada
    prueba_seleccionada = prueba
    resultado_area.insert(ctk.END, f"Prueba seleccionada: {prueba}\n")

# Crear la barra superior roja con el título
barra_superior = ctk.CTkFrame(root, height=105, corner_radius=0, fg_color="darkred")  
barra_superior.grid(row=0, column=0, columnspan=3, sticky="ew")


# Título
titulo_label = ctk.CTkLabel(barra_superior, text="Moderando el extremismo de opiniones en una red social", font=("Montserrat", 24), text_color="white")
titulo_label.place(relx=0.5, rely=0.5, anchor="center") # Centrar el título

# Cargar la imagen del logo 
logo_image = Image.open("logoUV_gris.jpg")
logo_image = logo_image.resize((95, 105))
logo_image_tk = ImageTk.PhotoImage(logo_image)

# Mostrar la imagen del logo
logo_label = ctk.CTkLabel(barra_superior, image=logo_image_tk, text="")
logo_label.grid(row=0, column=0, padx=0, pady=0) 

# Crear el área izquierda
frame_resultados = ctk.CTkFrame(root, width=450, height=35, corner_radius=0, fg_color="gray30")  
frame_resultados.grid(row=1, column=0, rowspan=2, sticky="nswe")

resultado_label = ctk.CTkLabel(frame_resultados, text="Resultado\npruebas realizadas", font=("Montserrat", 10), text_color="white", justify="center")
resultado_label.grid(row=0, column=0, pady=10)

# Crear el área principal de contenido 
frame_contenido = ctk.CTkFrame(root, fg_color="gray25", width=150, height=100)  
frame_contenido.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

# Título dentro del contenido
label_seleccion = ctk.CTkLabel(frame_contenido, text="Seleccione el algoritmo y la prueba a ejecutar", font=("Montserrat", 20))
label_seleccion.grid(row=0, column=0, pady=10, sticky="ew")

# Crear un marco para alinear los menús desplegables de forma horizontal
frame_menus_botones = ctk.CTkFrame(frame_contenido, fg_color="gray25")
frame_menus_botones.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

# Alinear centrado el contenido dentro del frame
frame_menus_botones.grid_columnconfigure(0, weight=1)
frame_menus_botones.grid_columnconfigure((0, 1, 2, 3), weight=1)

# Menú desplegable para Pruebas
opciones_pruebas = ctk.CTkOptionMenu(
    frame_menus_botones,
    values=["Cargando pruebas..."],
    command=seleccionar_prueba,  # Llama a seleccionar_prueba cuando se selecciona una prueba
    fg_color="darkred", 
    button_color="darkred", 
    button_hover_color="#c71818"  
)
opciones_pruebas.grid(row=0, column=0, padx=10)

# Menú desplegable para Algoritmos
opciones_algoritmos = ctk.CTkOptionMenu(
    frame_menus_botones,
    values=["Fuerza Bruta", "Voraz", "Programación Dinámica"],
    command=seleccionar_algoritmo,
    fg_color="darkred", 
    button_color="darkred",  
    button_hover_color="#c71818",  
)
opciones_algoritmos.grid(row=0, column=1, padx=10)

# Botón de "Ejecutar prueba"
btn_ejecutar_prueba = ctk.CTkButton(
    frame_menus_botones,
    text="Ejecutar prueba", 
    fg_color="darkred", 
    hover_color="darkred",
    command=lambda: ejecutar_algoritmo(opciones_algoritmos.get())
)
btn_ejecutar_prueba.grid(row=0, column=2, padx=10)

# Botón de "Detener prueba"
btn_detener_prueba = ctk.CTkButton(
    frame_menus_botones,
    text="Detener prueba", 
    fg_color="darkred", 
    hover_color="darkred",
    command=lambda: resultado_area.insert(ctk.END, "Prueba detenida\n")
)
btn_detener_prueba.grid(row=0, column=3, padx=10)

# Crear el área para mostrar el resultado de la ejecución
frame_resultado = ctk.CTkFrame(root, fg_color="gray25", width=150, height=400) 
frame_resultado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

label_resultado = ctk.CTkLabel(frame_resultado, text="Resultado de la ejecución", font=("Montserrat", 30))
label_resultado.grid(row=0, column=0, pady=10)

# Crear el área de texto para mostrar resultados
resultado_area = ctk.CTkTextbox(frame_resultado, height=150, width=870)
resultado_area.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Ajustar el peso de las columnas y filas para que la interfaz sea más responsive 
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)  
frame_resultado.grid_rowconfigure(1, weight=1)

# Actualizar el menú de pruebas al iniciar la aplicación
actualizar_pruebas_menu()
actualizar_algoritmos_menu()

# Ejecutar la aplicación
root.mainloop()

