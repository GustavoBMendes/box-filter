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
cv2.imwrite('escaladecinza.png',imagem)

proporcao = int(arquivos[1])

print("Altura: %d pixels" % (imagem.shape[0]))
print("Largura: %d pixels" % (imagem.shape[1]))


i = 0
j = 0
colunas = []
linhas = []

#Percorrendo a matriz original para cálculo das médias
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
print("Altura: %d pixels" % (reduzida.shape[0]))
print("Largura: %d pixels" % (reduzida.shape[1]))

#downsampling com box filter
cv2.imshow("Imagem reduzida com box filter", reduzida)
cv2.imwrite('reduzida_bf.png',reduzida)

#upsampling do box filter
upBF = np.repeat(reduzida, proporcao, axis=1)
upBF = np.repeat(upBF, proporcao, axis=0)
cv2.imshow('Box filter no tamanho original', upBF)
cv2.imwrite('up_bf.png',upBF)

#redução por downsampling fatiamento
downsampling = imagem[::proporcao, ::proporcao]
cv2.imshow('Reduzida por downsampling simples', downsampling)
cv2.imwrite('reduzida_fatiamento.png',downsampling)

#retorno ao tamanho original através de upsampling
upsampling = np.repeat(downsampling, proporcao, axis=1)
upsampling = np.repeat(upsampling, proporcao, axis=0)
cv2.imshow('Upsampling fatiamento simples', upsampling)
cv2.imwrite('up_fatiamento.png',upsampling)

cv2.waitKey(0)
