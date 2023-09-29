#!/bin/bash

# Verifica si se proporciona una fecha como argumento
if [ $# -ne 1 ]; then
    echo "Uso: $0 <fecha en formato 'YYYY-MM-DD'>"
    exit 1
fi

# Obtén la fecha del primer argumento
fecha="$1"

# Ruta del directorio donde se buscarán los archivos
directorio="."

# Ruta de la carpeta de destino
destino="/2023-11-10"

# Verifica si la carpeta de destino existe; si no, créala
if [ ! -d "$destino" ]; then
    mkdir -p "$destino"
fi

# Busca archivos de imagen que cumplen con los criterios y cópialos a la carpeta de destino
find "$directorio" \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) -type f -newermt "$fecha" ! -newermt "$fecha+1" -exec cp {} "$destino" \;
