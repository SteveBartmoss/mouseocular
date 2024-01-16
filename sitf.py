#importante, para que el codigo funcione se debe instalar opencv contrib 
#el comando es pip install opencv-contrib-python

import cv2
import numpy as np

#se carga la imagen en la que se van a buscar las caracteriscas
img=cv2.imread("img.png",cv2.IMREAD_GRAYSCALE)

#se crea una instancia de la libreria de SIFT para poder trabajar con ella
sift=cv2.xfeatures2d.SIFT_create()

#no se puede usar surf porque es de pago :( pero obr es la misma version que surft pero de gnu
#surft=cv2.xfeatures2d.SURF_create()

#esta es la version de surt pero de codigo abierto, se crea una instancia para poder trabajar con la libareria
orb=cv2.ORB_create()

#con esto se almacenan los puntos clabes de que se obtienen usando el algorimtmo obr
#las lineas comentadas corresponden a cada implementacion

#keypoints, descriptors=sift.detectAndCompute(img, None)
#keypoints, descriptors=surft.detectAndCompute(img, None)
keypoints, descriptors=orb.detectAndCompute(img, None)

#se dibujan en la imagen los puntos clabe que se obtuvieron
img=cv2.drawKeypoints(img,keypoints,None)

#se muestra en pantalla la imagen con los puntos claves ya dibujados
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

