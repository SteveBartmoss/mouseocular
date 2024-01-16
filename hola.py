#se importa la libreria de opencv
import cv2

#se crea el objeto de captura, en este caso se indica que sera la camara por defecto de la computadora por que se pasa el indice 0
capture=cv2.VideoCapture(0)

#se debe iniciar un bucle para la instruccion capture.read()
while (capture.isOpened()):

    #se captura imagen cuador por cuadro, por esto requiere un bucle
    #para que sea de forma continua
    ret, frame=capture.read()

    #se muestra en pantalla la captura que se esta opteniendo
    cv2.imshow('webCam',frame)

    #si se pulsa la tecla s, salimos del bucle que se definio anteriormente
    if (cv2.waitKey(1) == ord ('s')):
        break

#despues de salir del bule se borra el objeto que definimos anteriormente
capture.release()

#se borran las ventanas que surgen con el programa
cv2.destroyAllWindows()
#hola
