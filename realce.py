# Trabalho de processamento de imagens, realçador de bordas

import cv2

url='img.png' 

#importa a imagen destino

imagem=cv2.imread(url) 

#invoka a imagem, cria uma variavel com ela no Open CV

imagemLapcian=cv2.Laplacian(imagem,cv2.CV_8U) 

#aplica o filtro de realce de bordas

cv2.imshow("Bordasrealce",imagemLapcian) 

#apresenta a imagem na tela

cv2.waitKey(0)

 #encerra