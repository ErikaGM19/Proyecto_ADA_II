import customtkinter as ctk # Importación de la librería personalizada
from tkinter import filedialog # Importación del módulo para abrir el diálogo de archivos
from PIL import Image, ImageTk  # Importar las clases Image y ImageTk de la librería Pillow

# Inicializamos la aplicación y configuramos el tema
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue") 

# Crear la ventana principal
root = ctk.CTk() 
root.geometry("1000x600") # Tamaño inicial de la ventana
root.title("Proyecto I - ADA II - Grupo 4") 

# Función para cargar el archivo
def cargar_archivo():
    archivo = filedialog.askopenfilename(title="Cargar red", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        print(f"Archivo cargado: {archivo}")

# Definir las funciones de los algoritmos
def ejecutar_fuerza_bruta():
    print("Ejecutando Fuerza Bruta")

def ejecutar_programacion_dinamica():
    print("Ejecutando Programación Dinámica")

def ejecutar_voraz():
    print("Ejecutando Voraz")

# Función que maneja la selección del algoritmo
def ejecutar_algoritmo(algoritmo):
    if algoritmo == "Fuerza Bruta":
        ejecutar_fuerza_bruta()
    elif algoritmo == "Programación Dinámica":
        ejecutar_programacion_dinamica()
    elif algoritmo == "Voraz":
        ejecutar_voraz()

# Crear la barra superior roja con el título
barra_superior = ctk.CTkFrame(root, height=105, corner_radius=0, fg_color="darkred")  
barra_superior.grid(row=0, column=0, columnspan=3, sticky="ew")
barra_superior.pack_propagate(False)  

# Título
titulo_label = ctk.CTkLabel(barra_superior, text="Moderando el extremismo de opiniones en una red social", font=("Montserrat", 24), text_color="white")
titulo_label.place(relx=0.5, rely=0.5, anchor="center") # Centrar el título

# Cargar la imagen del logo 
logo_image = Image.open("logoUV_gris.jpg")
logo_image = logo_image.resize((95, 105))
logo_image_tk = ImageTk.PhotoImage(logo_image)

# Mostrar la imagen del logo
logo_label = ctk.CTkLabel(barra_superior, image=logo_image_tk, text="")
logo_label.pack(side="left", anchor="nw", padx=0, pady=0) 

# Crear el área izquierda
frame_resultados = ctk.CTkFrame(root, width=450, height=35, corner_radius=0, fg_color="gray30")  
frame_resultados.grid(row=1, column=0, rowspan=2, sticky="nswe")

resultado_label = ctk.CTkLabel(frame_resultados, text="Resultado\npruebas realizadas", font=("Montserrat", 10), text_color="white", justify="center")
resultado_label.pack(pady=10)

# Crear el área principal de contenido 
frame_contenido = ctk.CTkFrame(root, fg_color="gray25", width=150, height=100)  
frame_contenido.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

# Título dentro del contenido
label_seleccion = ctk.CTkLabel(frame_contenido, text="Seleccione el algoritmo y la prueba a ejecutar", font=("Montserrat", 20))
label_seleccion.pack(pady=10)

# Crear un marco para alinear los menús desplegables de forma horizontal
frame_menus = ctk.CTkFrame(frame_contenido, fg_color="gray25")
frame_menus.pack(pady=10)

# Menú desplegable para Algoritmos
opciones_algoritmos = ctk.CTkOptionMenu(
    frame_menus,
    values=["Fuerza Bruta", "Programación Dinámica", "Voraz"],
    command=lambda seleccion: ejecutar_algoritmo(seleccion),
    fg_color="darkred", 
    button_color="darkred",  
    button_hover_color="#c71818",  
)
opciones_algoritmos.grid(row=0, column=0, padx=10)

# Menú desplegable para Pruebas
opciones_pruebas = ctk.CTkOptionMenu(
    frame_menus,
    values=["Prueba 1", "Prueba 2", "Prueba 3"],
    fg_color="darkred", 
    button_color="darkred", 
    button_hover_color="#c71818"  
)
opciones_pruebas.grid(row=0, column=1, padx=80)

# Crear el área para mostrar el resultado de la ejecución
frame_resultado = ctk.CTkFrame(root, fg_color="gray25", width=150, height=400) 
frame_resultado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

label_resultado = ctk.CTkLabel(frame_resultado, text="Resultado de la ejecución", font=("Montserrat", 30))
label_resultado.pack(pady=10)

# Ajustar el peso de las columnas y filas para que la interfaz sea más responsive 
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)  

# Ejecutar la aplicación
root.mainloop()
