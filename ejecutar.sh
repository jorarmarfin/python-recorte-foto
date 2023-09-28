find . -type f ! -name "*.py" ! -name "*.bash" -exec python3 recorte.py {} \; > salida.txt
