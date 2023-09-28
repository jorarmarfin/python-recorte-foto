import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

# Crear una aplicación PyQt
app = QApplication(sys.argv)

# Crear una ventana principal
window = QMainWindow()
window.setWindowTitle('Hola Mundo con PyQt5')
window.setGeometry(100, 100, 400, 200)  # Establecer la posición y el tamaño de la ventana

# Crear una etiqueta de texto
label = QLabel('Hola Mundo!', window)
label.setGeometry(150, 80, 200, 40)  # Establecer la posición y el tamaño de la etiqueta

# Mostrar la ventana
window.show()

# Iniciar el bucle de eventos de la aplicación
sys.exit(app.exec_())
