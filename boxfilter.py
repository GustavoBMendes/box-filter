import cv2
import numpy as np
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-a', 
	'--arquivos', 
	type=str, 
	nargs='+', 
	help='Imagem a ser lida, informe o nome completo do arquivo, em seguida a proporção em que a imagem será reduzida, exemplo: python boxfilter.py -a teste.png 2')
args = parser.parse_args()
arquivos = args.arquivos
print(arquivos)

imagem = cv2.imread(arquivos[0], 0)
cv2.imshow('Imagem original', imagem)

proporcao = int(arquivos[1])

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

cv2.imshow("Imagem reduzida com box filter", reduzida)
upBF = np.repeat(reduzida, proporcao, axis=1)
upBF = np.repeat(upBF, proporcao, axis=0)
cv2.imshow('Box filter no tamanho original', upBF)

#redução por downsampling
downsampling = imagem[::proporcao, ::proporcao]
cv2.imshow('Reduzida por vizinho mais proximo', downsampling)

#retorno ao tamanho original através de upsampling
upsampling = np.repeat(downsampling, proporcao, axis=1)
upsampling = np.repeat(upsampling, proporcao, axis=0)
cv2.imshow('Upsampling vizinho mais proximo', upsampling)

cv2.waitKey(0)
