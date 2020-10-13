import cv2
import numpy as np

def media(ponto):
	print(ponto)
	return ponto

imagem = cv2.imread('teste.png', 0)
cv2.imshow('Teste', imagem)

proporcao = 2

print("Altura: %d pixels" % (imagem.shape[0]))
print("Largura: %d pixels" % (imagem.shape[1]))

print(imagem)

#reduzida = np.array(imagem[0:int(imagem.shape[0]/proporcao), 0:int(imagem.shape[1]/proporcao)], dtype=np.int32)
#aux = np.arange(0, int(imagem.shape[0]), proporcao)

#reduzida[:, ::1] = aux
i = 0
j = 0
colunas = []
linhas = []
while i < imagem.shape[0]:
	while j < imagem.shape[1]:
		media = imagem[i:proporcao+i, j:proporcao+j]
		pixel_novo = int(media.mean())
		j += proporcao
		colunas.append(pixel_novo)
	linhas.append(colunas)
	colunas = []
	i += proporcao
	j = 0

reduzida = np.array(linhas, dtype=np.uint8)
print(reduzida)
print("Altura: %d pixels" % (reduzida.shape[0]))
print("Largura: %d pixels" % (reduzida.shape[1]))

cv2.imshow("Imagem reduzida", reduzida)

cv2.waitKey(0)
