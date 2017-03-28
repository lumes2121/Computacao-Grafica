from PIL import Image
import math


class Operações():
    def __init__(self):
        self.imagemFinal = None
        self.imagem1 = None
        self.imagem2 = None

    def carregarImagem1(self, imagem):
        self.imagem1 = Image.open(imagem)
        self.imagemFinal = self.imagem1

    def carregarImagem2(self, imagem):
        self.imagem2 = Image.open(imagem)

    def negativo(self):
        largura, altura = self.imagemFinal.size

        if self.imagemFinal.mode != 'L':
            canal = self.imagemFinal.layers
            for i in range(largura):
                for j in range(altura):
                    valor = []
                    for k in range(canal):
                        valor.append(255 - self.imagemFinal.getpixel((i,j))[k])
                    self.imagemFinal.putpixel((i,j),tuple(valor))
        else:
            for i in range(largura):
                for j in range(altura):
                    valor = 255 - self.imagemFinal.getpixel((i,j))
                    self.imagemFinal.putpixel((i,j), valor)

    def limiarização(self, limiar):
        self.imagemFinal = self.limiarização_imagem(limiar, self.imagemFinal)

    def limiarização_imagem(self, limiar, imagem):
        largura, altura = imagem.size

        imagem = imagem.convert("L")

        for i in range(largura):
            for j in range(altura):
                if imagem.getpixel((i,j)) <= limiar:
                    imagem.putpixel((i,j), 0)
                else:
                    imagem.putpixel((i,j), 255)
        return imagem

    def operação_and(self):
        self.operaçãoLógica(lambda valor1, valor2: valor1 and valor2)

    def operação_or(self):
        self.operaçãoLógica(lambda valor1, valor2: valor1 or valor2)

    def operaçãoLógica(self, f):
        imagem1 = self.limiarização_imagem(127, self.imagem1)
        imagem2 = self.limiarização_imagem(127, self.imagem2)

        self.imagemFinal = imagem1

        largura1, altura1 = imagem1.size
        largura2, altura2 = imagem2.size

        for i in range(largura1):
            if i > largura2 - 1:
                break
            for j in range(altura1):
                if j > altura2 - 1:
                    break
                if f(bool(imagem1.getpixel((i, j))), bool(imagem2.getpixel((i, j)))):
                    self.imagemFinal.putpixel((i, j), 255)
                else:
                    self.imagemFinal.putpixel((i, j), 0)

    def soma(self):
        self.imagemFinal = self.operaçãoAritmética(lambda parcela1, parcela2: parcela1 + parcela2, self.imagem1, self.imagem2)

    def subtração(self):
        self.imagemFinal = self.operaçãoAritmética(lambda minuendo, subtraendo: minuendo - subtraendo, self.imagem1, self.imagem2)

    def multiplicação(self):
        self.imagemFinal = self.operaçãoAritmética(lambda multiplacando, multiplicador: multiplacando * multiplicador, self.imagem1, self.imagem2)

    def divisão(self):
        self.imagemFinal = self.operaçãoAritmética(lambda numerador, denominador: numerador / (denominador + 1), self.imagem1, self.imagem2)

    def operaçãoAritmética(self, f, imagem1, imagem2):
        imagemFinal = imagem1

        largura1, altura1 = imagem1.size
        largura2, altura2 = imagem2.size

        intensidades = []

        for i in range(largura1):
            intensidades.append([])
            for j in range(altura1):
                intensidades[-1].append(imagemFinal.getpixel((i, j)))

        canal = imagemFinal.layers
        maiorValor, menorValor = [0] * canal, [255] * canal

        for i in range(largura1):
            if i > largura2 - 1:
                break
            for j in range(altura1):
                if j > altura2 - 1:
                    break

                pixel = []
                for k in range(canal):
                    valor = f(imagem1.getpixel((i, j))[k], imagem2.getpixel((i, j))[k])

                    if valor > maiorValor[k]:
                        maiorValor[k] = valor
                    if valor < menorValor[k]:
                        menorValor[k] = valor

                    pixel.append(valor)
                intensidades[i][j] = tuple(pixel)

        for i in range(largura1):
            if i > largura2 - 1:
                break
            for j in range(altura1):
                if j > altura2 - 1:
                    break

                pixel = []
                for k in range(canal):
                    pixel.append(int(self.escalonamento(255, maiorValor[k], menorValor[k], intensidades[i][j][k])))

                imagemFinal.putpixel((i, j), tuple(pixel))

        return imagemFinal

    def escalonamento(self, M, tmax, tmin, t):
        return (M/(tmax - tmin))*(t - tmin)

    def equalização(self):
        self.imagemFinal = self.imagem1
        intensidades = self.h()
        intensidades_norm = self.h_norm(intensidades)
        intensidades_acum_norm = self.h_acum_norm(intensidades_norm)
        self.equalizar(intensidades_acum_norm)

    def h(self):
        largura, altura = self.imagemFinal.size

        intensidades = []

        if self.imagemFinal.mode != 'L':
            for i in range(self.imagemFinal.layers):
                intensidades.append([])
                for j in range(0, 256):
                    intensidades[-1].append(0)
        else:
            for i in range(1):
                intensidades.append([])
                for j in range(0, 256):
                    intensidades[-1].append(0)

        for x in range(largura):
            for y in range(altura):
                if self.imagemFinal.mode != 'L':
                    for c, canal in enumerate(self.imagemFinal.getpixel((x,y))):
                        intensidades[c][canal] += 1
                else:
                    intensidades[0][self.imagemFinal.getpixel((x,y))] += 1

        print(intensidades)

        return intensidades

    def h_norm(self, intensidades):
        M, N = self.imagemFinal.size

        intensidades_norm = []
        for i in range(len(intensidades[0])):
            intensidades_norm.append([valor / (M * N) for valor in intensidades[0]])

        return intensidades_norm

    def h_acum_norm(self, intensidades_norm):
        intensidades_acum_norm = intensidades_norm

        for i, canal in enumerate(intensidades_acum_norm):
            for j, valor in enumerate(canal):
                if j != 0:
                    intensidades_acum_norm[i][j] += intensidades_acum_norm[i][j - 1]

        return intensidades_acum_norm

    def equalizar(self, intensidades_acum_norm):
        largura, altura = self.imagemFinal.size

        if self.imagemFinal.mode != 'L':
            canal = self.imagemFinal.layers

            for x in range(largura):
                for y in range(altura):
                    pixel = []
                    for z in range(canal):
                        pixel.append(int(intensidades_acum_norm[z][self.imagemFinal.getpixel((x,y))[z]] * 255))
                    self.imagemFinal.putpixel((x,y),tuple(pixel))
        else:
            for x in range(largura):
                for y in range(altura):
                    self.imagemFinal.putpixel((x,y),int(intensidades_acum_norm[self.imagemFinal.getpixel((x,y))] * 255))

    def filtroSuavização(self, valor):
        máscara = []
        for x in range(valor):
            máscara.append([1]*valor)
        print(máscara)

        largura, altura = self.imagemFinal.size

        if self.imagemFinal.mode != 'L':
            canal = self.imagemFinal.layers

            offset = math.floor(valor/2)

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = []
                    for z in range(canal):
                        aux = 0
                        for x2 in range(valor):
                            for y2 in range(valor):
                                aux += máscara[x2][y2] * self.imagemFinal.getpixel(((x - offset) + x2, (y-offset) + y2))[z]
                        pixel.append(int(aux/valor**2))
                    print(x, y, pixel)
                    self.imagemFinal.putpixel((x,y), tuple(pixel))
        else:
            offset = math.floor(valor / 2)

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = 0
                    for x2 in range(valor):
                        for y2 in range(valor):
                            pixel += máscara[x2][y2] * \
                                   self.imagemFinal.getpixel(((x - offset) + x2, (y - offset) + y2))
                    pixel = pixel / valor ** 2
                    print(x, y, pixel)
                    self.imagemFinal.putpixel((x, y), int(pixel))

    def filtroRealce(self):
        print('Realçando com a primeira máscara')
        máscara = [[-1,-1,-1],
                   [0,0,0],
                   [1,1,1]]
        imagem1 = self.realçar(self.imagem1, máscara)
        máscara = [[-1,0,1],
                   [-1,0,1],
                   [-1,0,1]]
        print('Realçando com a segunda máscara')
        imagem2 = self.realçar(self.imagem1, máscara)

        print('Calculando imagem final')
        self.imagemFinal = self.operaçãoAritmética(lambda a, b: math.sqrt(a**2+b**2), imagem1, imagem2)

    def realçar(self, imagem, máscara):
        imagemFinal = imagem
        largura, altura = imagemFinal.size

        matrizImagem = []

        for i in range(largura):
            matrizImagem.append([])
            for j in range(altura):
                matrizImagem[-1].append(imagemFinal.getpixel((i, j)))

        if imagemFinal.mode != 'L':
            canal = imagemFinal.layers
            maiorValor, menorValor = [0] * canal, [255] * canal

            offset = math.floor(len(máscara) / 2)

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = []
                    for z in range(canal):
                        aux = 0
                        for x2 in range(len(máscara)):
                            for y2 in range(len(máscara)):
                                aux += máscara[x2][y2] * imagemFinal.getpixel(((x - offset) + x2, (y - offset) + y2))[z]

                        if aux > maiorValor[z]:
                            maiorValor[z] = aux
                        if aux < menorValor[z]:
                            menorValor[z] = aux

                        pixel.append(aux)
                    matrizImagem[x][y] = tuple(pixel)

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = []
                    for k in range(canal):
                        pixel.append(int(self.escalonamento(255, maiorValor[k], menorValor[k], matrizImagem[x][y][k])))

                    imagemFinal.putpixel((x, y), tuple(pixel))


        else:
            offset = math.floor(len(máscara) / 2)

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = 0
                    for x2 in range(len(máscara)):
                        for y2 in range(len(máscara)):
                            pixel += máscara[x2][y2] * \
                                   self.imagemFinal.getpixel(((x - offset) + x2, (y - offset) + y2))
                    imagemFinal.putpixel((x, y), int(pixel))

        return imagemFinal