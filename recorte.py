import cv2
import sys
import os

# Verifica si se proporciona el nombre del archivo de imagen como argumento
if len(sys.argv) != 2:
    print("Uso: python3 recorte.py nombre_de_la_foto.jpeg")
    sys.exit(1)

# Obtiene el nombre del archivo de imagen desde los argumentos de línea de comandos
nombre_archivo = sys.argv[1]

# Verifica si el archivo de imagen especificado existe
if not os.path.isfile(nombre_archivo):
    print(f"El archivo '{nombre_archivo}' no existe.")
    sys.exit(1)

# Crea una carpeta llamada "recorte" si no existe
carpeta_recorte = 'recorte'
os.makedirs(carpeta_recorte, exist_ok=True)

# Carga la imagen
imagen = cv2.imread(nombre_archivo)

# Carga el clasificador de detección de rostros preentrenado
clasificador_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Convierte la imagen a escala de grises (la detección de rostros funciona mejor en imágenes en escala de grises)
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detecta rostros en la imagen
rostros = clasificador_rostros.detectMultiScale(imagen_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Si se detectan rostros, recorta la región del primer rostro encontrado
if len(rostros) > 0:
    x, y, w, h = rostros[0]  # Obtiene las coordenadas del primer rostro

    # Calcula las dimensiones del recorte en proporción 3:4
    proporcion_ancho = 3
    proporcion_alto = 4
    ancho_recorte = w

    # Ajusta el alto del recorte para mantener la proporción
    alto_recorte = int(ancho_recorte * proporcion_alto / proporcion_ancho)

    # Realiza el recorte
    rostro_recortado = imagen[y - 150:y + alto_recorte, x:x + ancho_recorte+50]

    # Guarda la región del rostro recortado en un archivo
    cv2.imwrite('rostro_recortado.jpeg', rostro_recortado)

    print("Rostro recortado y guardado como 'rostro_recortado.jpeg'.")
else:
    print("No se detectaron rostros en la imagen.")
