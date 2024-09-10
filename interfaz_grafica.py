import tkinter as tk
from tkinter import Menu, filedialog, messagebox, scrolledtext

# Función para cargar el archivo de texto
red_social_inicial = []

def cargar_archivo():
    archivo = filedialog.askopenfilename(
        title="Cargar red", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    
    if archivo:
        try:
            with open(archivo, 'r') as f:
                contenido = f.read()
                validar_contenido(contenido)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

# Función para validar y procesar el contenido del archivo
def validar_contenido(contenido):
    lineas = contenido.splitlines()
    
    try:
        # Validar que la primera línea sea n (cantidad de agentes)
        n = int(lineas[0])
        if n <= 0:
            raise ValueError("El valor de n debe ser mayor que 0.")
        
        # Validar que haya n líneas de agentes + 1 para r_max
        if len(lineas) != n + 2:  # n agentes, 1 línea de r_max, 1 línea para n
            raise ValueError("La cantidad de agentes no coincide con el valor de n.")
        
        # Validar y extraer elementos A, B
        elementos = []
        for i in range(1, n + 1):  # Desde la segunda línea hasta la (n+1)-ésima línea
            A, B = map(float, lineas[i].split(','))
            if not (-100 <= A <= 100) or not (0 <= B <= 1):
                raise ValueError("Los valores de A y B están fuera de los límites permitidos.")
            elementos.append([A, B])
        
        # Validar r_max en la última línea
        r_max = int(lineas[-1])
        if r_max < 0:
            raise ValueError("El valor de r_max debe ser un entero no negativo.")
        
        # Estructurar la red_social
        red_social = [elementos, r_max]
        red_social_inicial.append(red_social)

        # Mostrar el archivo cargado y red_social en las cajas de texto
        caja_archivo.delete(1.0, tk.END)
        caja_archivo.insert(tk.END, contenido)
        
        caja_respuesta.delete(1.0, tk.END)
        caja_respuesta.insert(tk.END, f"Archivo cargado correctamente:\nRed Social: {red_social}")
        
    except Exception as e:
        messagebox.showerror("Error", f"El archivo cargado no cumple con el estándar: {e}")
        caja_archivo.delete(1.0, tk.END)
        caja_respuesta.delete(1.0, tk.END)

# Funciones de los botones
def fuerza_bruta():
    from modexFB import modexFB
    lista_aplanada_red_social = sum(red_social_inicial, start=[])
    respuesta = modexFB(lista_aplanada_red_social)
    caja_respuesta.insert(tk.END, f"\nEjecutando Fuerza Bruta...\n {respuesta}")
    red_social_inicial.clear() 
def voraz():
    caja_respuesta.insert(tk.END, "\nEjecutando Voraz...\n")

def dinamica():
    caja_respuesta.insert(tk.END, "\nEjecutando Programación Dinámica...\n")

# Función para limpiar la interfaz y la caché
def limpiar():
    red_social_inicial.clear()  # Limpiar la caché
    caja_archivo.delete(1.0, tk.END)
    caja_respuesta.delete(1.0, tk.END)

# Función para salir
def salir():
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Proyecto ADA II")
root.geometry("800x600")

# Configurar cierre de la ventana con "Salir" o con la X
root.protocol("WM_DELETE_WINDOW", salir)

# Crear la barra de menú
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Menú "Archivo"
archivo_menu = Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Cargar red", command=cargar_archivo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Limpiar", command=limpiar)  # Opción "Limpiar" en el menú
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

# Crear el marco para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botones
btn_fuerza_bruta = tk.Button(frame_botones, text="Fuerza Bruta", command=fuerza_bruta, width=20)
btn_fuerza_bruta.grid(row=0, column=0, padx=10)

btn_voraz = tk.Button(frame_botones, text="Voraz", command=voraz, width=20)
btn_voraz.grid(row=0, column=1, padx=10)

btn_dinamica = tk.Button(frame_botones, text="Dinámica", command=dinamica, width=20)
btn_dinamica.grid(row=0, column=2, padx=10)

# Caja de texto para visualizar el archivo cargado
caja_archivo = scrolledtext.ScrolledText(root, height=10, width=100)
caja_archivo.pack(pady=10)

# Caja de texto para visualizar la respuesta
caja_respuesta = scrolledtext.ScrolledText(root, height=10, width=100)
caja_respuesta.pack(pady=10)

# Botón "Limpiar" en la parte inferior de la interfaz
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar, width=20)
btn_limpiar.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
