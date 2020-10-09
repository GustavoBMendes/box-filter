import cv2


imagem = cv2.imread('teste.png', 0)
cv2.imshow('Teste', imagem)

print("Altura: %d pixels" % (imagem.shape[0]))
print("Largura: %d pixels" % (imagem.shape[1]))

print("Matriz com niveis de cinza:\n", imagem)

cv2.waitKey(0)
