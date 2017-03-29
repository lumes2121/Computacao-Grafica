from PIL import Image
import math


class Operações:
    def __init__(self):
        self.imagem_final = None
        self.imagem_1 = None
        self.imagem_2 = None

    def carregar_imagem_1(self, imagem):
        self.imagem_1 = Image.open(imagem)
        self.imagem_final = self.imagem_1

    def carregar_imagem_2(self, imagem):
        self.imagem_2 = Image.open(imagem)

    def negativo(self):
        largura, altura = self.imagem_final.size

        if self.imagem_final.mode != 'L':
            canal = self.imagem_final.layers
            for i in range(largura):
                for j in range(altura):
                    valor = []
                    for k in range(canal):
                        valor.append(255 - self.imagem_final.getpixel((i, j))[k])
                    self.imagem_final.putpixel((i, j), tuple(valor))
        else:
            for i in range(largura):
                for j in range(altura):
                    valor = 255 - self.imagem_final.getpixel((i, j))
                    self.imagem_final.putpixel((i, j), valor)

    def limiarização(self, limiar):
        self.imagem_final = self.limiarização_imagem(limiar, self.imagem_final)

    @staticmethod
    def limiarização_imagem(limiar, imagem):
        largura, altura = imagem.size

        imagem = imagem.convert("L")

        for x in range(largura):
            for y in range(altura):
                if imagem.getpixel((x, y)) <= limiar:
                    imagem.putpixel((x, y), 0)
                else:
                    imagem.putpixel((x, y), 255)
        return imagem

    def operação_and(self):
        self.imagem_final = self.operação_lógica(lambda valor_1, valor_2: valor_1 and valor_2,
                                                 self.imagem_1, self.imagem_2)

    def operação_or(self):
        self.imagem_final = self.operação_lógica(lambda valor_1, valor_2: valor_1 or valor_2,
                                                 self.imagem_1, self.imagem_2)

    def operação_lógica(self, f, imagem_1, imagem_2):
        imagem_1 = self.limiarização_imagem(127, imagem_1)
        imagem_2 = self.limiarização_imagem(127, imagem_2)

        imagem_final = imagem_1

        largura_1, altura_1 = imagem_1.size
        largura_2, altura_2 = imagem_2.size

        for i in range(largura_1):
            if i > largura_2 - 1:
                break
            for j in range(altura_1):
                if j > altura_2 - 1:
                    break
                if f(bool(imagem_1.getpixel((i, j))), bool(imagem_2.getpixel((i, j)))):
                    imagem_final.putpixel((i, j), 255)
                else:
                    imagem_final.putpixel((i, j), 0)

        return imagem_final

    def soma(self):
        self.imagem_final = self.operação_aritmética(lambda valor_1, valor_2: valor_1 + valor_2,
                                                     self.imagem_1, self.imagem_2)

    def subtração(self):
        self.imagem_final = self.operação_aritmética(lambda valor_1, valor_2: valor_1 - valor_2,
                                                     self.imagem_1, self.imagem_2)

    def multiplicação(self):
        self.imagem_final = self.operação_aritmética(lambda valor_1, valor_2: valor_1 * valor_2,
                                                     self.imagem_1, self.imagem_2)

    def divisão(self):
        self.imagem_final = self.operação_aritmética(lambda valor_1, valor_2: valor_1 / (valor_2 + 1),
                                                     self.imagem_1, self.imagem_2)

    def operação_aritmética(self, f, imagem_1, imagem_2):
        imagem_final = imagem_1

        largura_1, altura_1 = imagem_1.size
        largura_2, altura_2 = imagem_2.size

        matriz_imagem = []

        for x in range(largura_1):
            matriz_imagem.append([])
            for y in range(altura_1):
                matriz_imagem[-1].append(imagem_final.getpixel((x, y)))

        canal = imagem_final.layers
        maior_valor, menor_valor = [0] * canal, [255] * canal

        for x in range(largura_1):
            if x > largura_2 - 1:
                break
            for y in range(altura_1):
                if y > altura_2 - 1:
                    break

                pixel = []
                for k in range(canal):
                    valor = f(imagem_1.getpixel((x, y))[k], imagem_2.getpixel((x, y))[k])

                    if valor > maior_valor[k]:
                        maior_valor[k] = valor
                    if valor < menor_valor[k]:
                        menor_valor[k] = valor

                    pixel.append(valor)
                matriz_imagem[x][y] = tuple(pixel)

        for x in range(largura_1):
            if x > largura_2 - 1:
                break
            for y in range(altura_1):
                if y > altura_2 - 1:
                    break

                pixel = []
                for k in range(canal):
                    pixel.append(int(self.escalonamento(maior_valor[k], menor_valor[k], matriz_imagem[x][y][k])))

                imagem_final.putpixel((x, y), tuple(pixel))

        return imagem_final

    @staticmethod
    def escalonamento(tmax, tmin, t):
        return (255/(tmax - tmin))*(t - tmin)

    def equalização(self):
        # self.imagem_final = self.imagem_1
        intensidades = self.h()
        intensidades_norm = self.h_norm(intensidades)
        intensidades_acum_norm = self.h_acum_norm(intensidades_norm)
        self.equalizar(intensidades_acum_norm)

    def h(self):
        largura, altura = self.imagem_final.size

        intensidades = []

        if self.imagem_final.mode != 'L':
            for x in range(self.imagem_final.layers):
                intensidades.append([])
                for y in range(0, 256):
                    intensidades[-1].append(0)
            for x in range(largura):
                for y in range(altura):
                    for z, canal in enumerate(self.imagem_final.getpixel((x, y))):
                        intensidades[z][canal] += 1
        else:
            for x in range(1):
                intensidades.append([])
                for y in range(0, 256):
                    intensidades[-1].append(0)
            for x in range(largura):
                for y in range(altura):
                    intensidades[0][self.imagem_final.getpixel((x, y))] += 1

        return intensidades

    def h_norm(self, intensidades):
        largura, altura = self.imagem_final.size

        intensidades_norm = []
        for i in range(len(intensidades[0])):
            intensidades_norm.append([valor / (largura * altura) for valor in intensidades[0]])

        return intensidades_norm

    @staticmethod
    def h_acum_norm(intensidades_norm):
        intensidades_acum_norm = intensidades_norm

        for x, canal in enumerate(intensidades_acum_norm):
            for y, valor in enumerate(canal):
                if y != 0:
                    intensidades_acum_norm[x][y] += intensidades_acum_norm[x][y - 1]

        return intensidades_acum_norm

    def equalizar(self, intensidades_acum_norm):
        largura, altura = self.imagem_final.size

        if self.imagem_final.mode != 'L':
            canal = self.imagem_final.layers

            for x in range(largura):
                for y in range(altura):
                    pixel = []
                    for z in range(canal):
                        pixel.append(int(intensidades_acum_norm[z][self.imagem_final.getpixel((x, y))[z]] * 255))
                    self.imagem_final.putpixel((x, y), tuple(pixel))
        else:
            for x in range(largura):
                for y in range(altura):
                    valor = intensidades_acum_norm[0][self.imagem_final.getpixel((x, y))] * 255
                    self.imagem_final.putpixel((x, y), int(valor))

    def filtro_suavização(self, valor):
        máscara = []
        for x in range(valor):
            máscara.append([1]*valor)
        print(máscara)

        largura, altura = self.imagem_final.size

        if self.imagem_final.mode != 'L':
            canal = self.imagem_final.layers

            offset = int(math.floor(valor/2))

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = []
                    for z in range(canal):
                        aux = 0
                        for x2 in range(valor):
                            for y2 in range(valor):
                                aux += máscara[x2][y2] * \
                                       self.imagem_final.getpixel(((x - offset) + x2, (y - offset) + y2))[z]
                        pixel.append(int(aux/valor**2))

                    self.imagem_final.putpixel((x, y), tuple(pixel))
        else:
            offset = int(math.floor(valor / 2))

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = 0
                    for x2 in range(valor):
                        for y2 in range(valor):
                            pixel += máscara[x2][y2] * \
                                   self.imagem_final.getpixel(((x - offset) + x2, (y - offset) + y2))
                    pixel = pixel / valor ** 2

                    self.imagem_final.putpixel((x, y), int(pixel))

    def filtro_realce(self):
        máscara = [[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]]
        self.imagem_final = self.realçar(self.imagem_1, máscara)

    def realçar(self, imagem, máscara):
        imagem_final = imagem
        largura, altura = imagem_final.size

        matriz_imagem = []

        for i in range(largura):
            matriz_imagem.append([])
            for j in range(altura):
                matriz_imagem[-1].append(imagem_final.getpixel((i, j)))

        if imagem_final.mode != 'L':
            canal = imagem_final.layers
            maior_valor, menor_valor = [-25500] * canal, [25500] * canal

            offset = int(math.floor(len(máscara) / 2))

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = []
                    for z in range(canal):
                        aux = 0
                        for x2 in range(len(máscara)):
                            for y2 in range(len(máscara)):
                                aux += máscara[x2][y2] * \
                                       imagem_final.getpixel(((x - offset) + x2, (y - offset) + y2))[z]

                        if aux > maior_valor[z]:
                            maior_valor[z] = aux
                        if aux < menor_valor[z]:
                            menor_valor[z] = aux

                        pixel.append(aux)
                    matriz_imagem[x][y] = tuple(pixel)

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = []
                    for k in range(canal):
                        valor = self.escalonamento(maior_valor[k], menor_valor[k], matriz_imagem[x][y][k])
                        pixel.append(int(valor))

                    imagem_final.putpixel((x, y), tuple(pixel))
        else:
            maior_valor, menor_valor = -25500, 25500

            offset = int(math.floor(len(máscara) / 2))

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = 0
                    for x2 in range(len(máscara)):
                        for y2 in range(len(máscara)):
                            pixel += máscara[x2][y2] * \
                                   imagem_final.getpixel(((x - offset) + x2, (y - offset) + y2))

                    if pixel > maior_valor:
                        maior_valor = pixel
                    if pixel < menor_valor:
                        menor_valor = pixel

                    matriz_imagem[x][y] = pixel

            for x in range(offset, largura - offset):
                for y in range(offset, altura - offset):
                    pixel = self.escalonamento(maior_valor, menor_valor, matriz_imagem[x][y])

                    imagem_final.putpixel((x, y), int(pixel))

        return imagem_final
