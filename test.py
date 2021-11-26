import pytesseract as tess #importando Pytesseract
import cv2
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Corregir el problema de path

#Ruta de imagen

Ruta = cv2.imread('Texto.jpeg')

Texto = tess.image_to_string(Ruta) #conversion para mostrar el texto de la imagen

cv2.imshow("Pruebas",Ruta)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(Texto)
