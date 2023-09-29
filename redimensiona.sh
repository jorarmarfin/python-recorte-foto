#!/bin/bash

# Lista todos los archivos JPEG en el directorio actual
for f in *.jpeg; do
  # Verifica si el archivo tiene problemas SOS
  if identify -verbose "$f" | grep -q "Invalid SOS parameters"; then
    # Convierte el archivo
    convert "$f" -strip "$f"
  fi
done


# Lista todas las imágenes con las extensiones jpg, jpeg o png
for f in *.jpg *.jpeg *.png; do
  width=$(identify -format "%w" "$f")
  if [ $width -lt 1000 ]; then
    echo "Redimensionando $f a 1024 píxeles"
    convert "$f" -resize 2048x "$f"
  fi
done

