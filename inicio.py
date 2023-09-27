import cv2
 
#Cargamos los clasificadores requeridos
face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt.xml')
 
#Utilizamos un fichero de imagen del disco duro
img = cv2.imread('foto3.jpeg')
 
while(True):
    #Convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Buscamos las coordenadas de los rostros
    caras = face_cascade.detectMultiScale(gray, 1.3, 5)
    #Dibujamos un rectángulo en las coordenadas de cada rostro
    x_ini = 0
    y_ini = 0
    x_fin = 0
    y_fin = 0
    for (x,y,w,h) in caras:
        x_ini = x-10
        y_ini = y-120
        x_fin = x+w+50
        y_fin = y+h+80
        cv2.rectangle(img,(x_ini,y_ini),(x_fin,y_fin),(0,0,0),2)
    #Recortar una imagen
    imageOut = img[x_ini-150:x_fin+100,y_ini+100:y_fin+50]
    #Mostramos la imagen
    cv2.imshow('imagen original',img)
    cv2.imshow('imagen cortada',imageOut)
    #Pulsando la tecla "q" salimos del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
