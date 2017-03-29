# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import PIL.ImageQt as ImageQt

from operações import Operações
from imageWidget import ImageWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.operações = Operações()

    def setupUi(self, MainWindow):
        MainWindow.showMaximized()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        # MainWindow.resize(894, 587)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame_imagem1 = QtGui.QFrame(self.centralwidget)
        self.frame_imagem1.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_imagem1.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_imagem1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_imagem1.setObjectName(_fromUtf8("frame_imagem1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_imagem1)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea_imagem1 = QtGui.QScrollArea(self.frame_imagem1)
        self.scrollArea_imagem1.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_imagem1.setWidgetResizable(True)
        self.scrollArea_imagem1.setObjectName(_fromUtf8("scrollArea_imagem1"))
        self.scrollAreaWidgetContents_1 = QtGui.QWidget()
        self.scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 300, 261))
        self.scrollAreaWidgetContents_1.setObjectName(_fromUtf8("scrollAreaWidgetContents_1"))
        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents_1)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.imagem1 = ImageWidget(self.scrollAreaWidgetContents_1)
        self.imagem1.setObjectName(_fromUtf8("imagem1"))
        self.gridLayout_5.addWidget(self.imagem1, 0, 0, 1, 1)
        self.scrollArea_imagem1.setWidget(self.scrollAreaWidgetContents_1)
        self.gridLayout_2.addWidget(self.scrollArea_imagem1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_imagem1, 0, 0, 1, 1)
        self.frame_imagem2 = QtGui.QFrame(self.centralwidget)
        self.frame_imagem2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_imagem2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_imagem2.setObjectName(_fromUtf8("frame_imagem2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_imagem2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.scrollArea_imagem2 = QtGui.QScrollArea(self.frame_imagem2)
        self.scrollArea_imagem2.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_imagem2.setWidgetResizable(True)
        self.scrollArea_imagem2.setObjectName(_fromUtf8("scrollArea_imagem2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 300, 261))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.imagem2 = ImageWidget(self.scrollAreaWidgetContents_2)
        self.imagem2.setObjectName(_fromUtf8("imagem2"))
        self.gridLayout_6.addWidget(self.imagem2, 0, 0, 1, 1)
        self.scrollArea_imagem2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea_imagem2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_imagem2, 1, 0, 1, 1)
        self.frame_imagem3 = QtGui.QFrame(self.centralwidget)
        self.frame_imagem3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_imagem3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_imagem3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_imagem3.setObjectName(_fromUtf8("frame_imagem3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_imagem3)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea_imagem3 = QtGui.QScrollArea(self.frame_imagem3)
        self.scrollArea_imagem3.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_imagem3.setWidgetResizable(True)
        self.scrollArea_imagem3.setObjectName(_fromUtf8("scrollArea_imagem3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 568, 526))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.gridLayout_9 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_9.setMargin(0)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.imagem3 = ImageWidget(self.scrollAreaWidgetContents_3)
        self.imagem3.setObjectName(_fromUtf8("imagem3"))
        self.gridLayout_9.addWidget(self.imagem3, 0, 0, 1, 1)
        self.scrollArea_imagem3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.addWidget(self.scrollArea_imagem3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_imagem3, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuOperações = QtGui.QMenu(self.menubar)
        self.menuOperações.setObjectName(_fromUtf8("menuOperações"))
        self.menuOperaçõesLógicas = QtGui.QMenu(self.menuOperações)
        self.menuOperaçõesLógicas.setObjectName(_fromUtf8("menuOperaçõesLógicas"))
        self.menuOperaçõesAritméticas = QtGui.QMenu(self.menuOperações)
        self.menuOperaçõesAritméticas.setObjectName(_fromUtf8("menuOperaçõesAritméticas"))
        self.menuFiltros = QtGui.QMenu(self.menubar)
        self.menuFiltros.setObjectName(_fromUtf8("menuFiltros"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionAbrir_Imagem_1 = QtGui.QAction(MainWindow)
        self.actionAbrir_Imagem_1.setObjectName(_fromUtf8("actionAbrir_Imagem_1"))
        self.actionAbrir_Imagem_1.triggered.connect(self.abrirArquivo1)

        self.actionAbrir_Imagem_2 = QtGui.QAction(MainWindow)
        self.actionAbrir_Imagem_2.setObjectName(_fromUtf8("actionAbrir_Imagem_2"))
        self.actionAbrir_Imagem_2.triggered.connect(self.abrirArquivo2)

        self.actionNegativo = QtGui.QAction(MainWindow)
        self.actionNegativo.setObjectName(_fromUtf8("actionNegativo"))
        self.actionNegativo.triggered.connect(self.negativo)

        self.actionLimiarização = QtGui.QAction(MainWindow)
        self.actionLimiarização.setObjectName(_fromUtf8("actionLimiarização"))
        self.actionLimiarização.triggered.connect(self.limiarizacao)

        self.actionOperaçãoAnd = QtGui.QAction(MainWindow)
        self.actionOperaçãoAnd.setObjectName(_fromUtf8("actionOperaçãoAnd"))
        self.actionOperaçãoAnd.triggered.connect(self.operacao_and)

        self.actionOperaçãoOr= QtGui.QAction(MainWindow)
        self.actionOperaçãoOr.setObjectName(_fromUtf8("actionOperaçãoOr"))
        self.actionOperaçãoOr.triggered.connect(self.operacao_or)

        self.actionSoma = QtGui.QAction(MainWindow)
        self.actionSoma.setObjectName(_fromUtf8("actionSoma"))
        self.actionSoma.triggered.connect(self.soma)

        self.actionSubtração = QtGui.QAction(MainWindow)
        self.actionSubtração.setObjectName(_fromUtf8("actionSubtração"))
        self.actionSubtração.triggered.connect(self.subtracao)

        self.actionMultiplicação = QtGui.QAction(MainWindow)
        self.actionMultiplicação.setObjectName(_fromUtf8("actionMultiplicação"))
        self.actionMultiplicação.triggered.connect(self.multiplicacao)

        self.actionDivisão = QtGui.QAction(MainWindow)
        self.actionDivisão.setObjectName(_fromUtf8("actionDivisão"))
        self.actionDivisão.triggered.connect(self.divisao)

        self.actionEqualização = QtGui.QAction(MainWindow)
        self.actionEqualização.setObjectName(_fromUtf8("actionEqualização"))
        self.actionEqualização.triggered.connect(self.equalizacao)

        self.actionFiltroSuavização = QtGui.QAction(MainWindow)
        self.actionFiltroSuavização.setObjectName(_fromUtf8("actionFiltroSuavização"))
        self.actionFiltroSuavização.triggered.connect(self.filtroSuavizacao)

        self.actionFiltroRealce = QtGui.QAction(MainWindow)
        self.actionFiltroRealce.setObjectName(_fromUtf8("actionFiltroRealce"))
        self.actionFiltroRealce.triggered.connect(self.filtroRealce)

        self.menuArquivo.addAction(self.actionAbrir_Imagem_1)
        self.menuArquivo.addAction(self.actionAbrir_Imagem_2)
        self.menuOperaçõesLógicas.addAction(self.actionOperaçãoAnd)
        self.menuOperaçõesLógicas.addAction(self.actionOperaçãoOr)
        self.menuOperaçõesAritméticas.addAction(self.actionSoma)
        self.menuOperaçõesAritméticas.addAction(self.actionSubtração)
        self.menuOperaçõesAritméticas.addAction(self.actionMultiplicação)
        self.menuOperaçõesAritméticas.addAction(self.actionDivisão)

        self.menuOperações.addAction(self.actionNegativo)
        self.menuOperações.addAction(self.actionLimiarização)
        self.menuOperações.addAction(self.menuOperaçõesLógicas.menuAction())
        self.menuOperações.addAction(self.menuOperaçõesAritméticas.menuAction())
        self.menuOperações.addAction(self.actionEqualização)

        self.menuFiltros.addAction(self.actionFiltroSuavização)
        self.menuFiltros.addAction(self.actionFiltroRealce)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuOperações.menuAction())
        self.menubar.addAction(self.menuFiltros.menuAction())


        self.menuOperações.setEnabled(False)
        self.menuFiltros.setEnabled(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Computação Gráfica", None))

        self.menuArquivo.setToolTip(_translate("MainWindow", "Arquivo", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.actionAbrir_Imagem_1.setText(_translate("MainWindow", "Abrir Imagem 1", None))
        self.actionAbrir_Imagem_2.setText(_translate("MainWindow", "Abrir Imagem 2", None))

        self.menuOperações.setTitle(_translate("MainWindow", "Operações", None))
        self.actionNegativo.setText(_translate("MainWindow", "Negativo", None))
        self.actionLimiarização.setText(_translate("MainWindow", "Limiarização", None))
        self.menuOperaçõesLógicas.setTitle(_translate("MainWindow", "Operações Lógicas", None))
        self.actionOperaçãoAnd.setText(_translate("MainWindow", "Operação AND", None))
        self.actionOperaçãoOr.setText(_translate("MainWindow", "Operação OR", None))
        self.menuOperaçõesAritméticas.setTitle(_translate("MainWindow", "Operações Aritméticas", None))
        self.actionSoma.setText(_translate("MainWindow", "Soma", None))
        self.actionSubtração.setText(_translate("MainWindow", "Subtração", None))
        self.actionMultiplicação.setText(_translate("MainWindow", "Multiplicação", None))
        self.actionDivisão.setText(_translate("MainWindow", "Divisão", None))
        self.actionEqualização.setText(_translate("MainWindow", "Equalização de Histograma", None))

        self.menuFiltros.setTitle(_translate("MainWindow", "Filtro", None))
        self.actionFiltroSuavização.setText(_translate("MainWindow", "Filtro de Suavização", None))
        self.actionFiltroRealce.setText(_translate("MainWindow", "Filtro de Realce", None))

    def abrirArquivo1(self):
        caminho_imagem = QtGui.QFileDialog.getOpenFileName(
            self, 'Abrir Arquivo', '', 'Todos os arquivos (*.*);;jpeg (*.jpeg);;jpg (*.jpg);;png (*.png)')

        if caminho_imagem:
            self.operações.carregar_imagem_1(str(caminho_imagem))
            self.imagem1.Qimg = ImageQt.ImageQt(
                self.operações.imagem_1.convert('RGB') if self.operações.imagem_1.mode == 'L' else self.operações.imagem_1)
            self.imagem1.repaint()
            self.atualizar()
            self.menuOperações.setEnabled(True)
            self.menuFiltros.setEnabled(True)

    def abrirArquivo2(self):
        caminho_imagem = QtGui.QFileDialog.getOpenFileName(
            self, 'Abrir Arquivo', '', 'Todos os arquivos (*.*);;jpeg (*.jpeg);;jpg (*.jpg);;png (*.png)')

        if caminho_imagem:
            self.operações.carregar_imagem_2(str(caminho_imagem))
            self.imagem2.Qimg = ImageQt.ImageQt(
                self.operações.imagem_2.convert('RGB') if self.operações.imagem_2.mode == 'L' else self.operações.imagem_2)
            self.imagem2.repaint()

    def atualizar(self):
        self.imagem3.Qimg = ImageQt.ImageQt(self.operações.imagem_final)
        self.imagem3.repaint()

    def negativo(self):
        print('Iniciando negativo')
        self.operações.negativo()
        self.atualizar()
        print('Negativo finalizado')

    def limiarizacao(self):
        num, ok = QtGui.QInputDialog.getInt(self, '', 'Entre com o limiar (0 a 255)')

        if ok:
            print('Iniciando limiarização')
            self.operações.limiarização(num)
            self.atualizar()
            print('Limiarização finalizada')

    def operacao_and(self):
        if self.operações.imagem_2 != None:
            print('Iniciando operação AND')
            self.operações.operação_and()
            self.atualizar()
            print('Operação AND finalizada')

    def operacao_or(self):
        if self.operações.imagem_2 != None:
            print('Iniciando operação OR')
            self.operações.operação_or()
            self.atualizar()
            print('Operação OR finalizada')

    def soma(self):
        if self.operações.imagem_2 != None:
            print('Iniciando soma')
            self.operações.soma()
            self.atualizar()
            print('Soma finalizada')

    def subtracao(self):
        if self.operações.imagem_2 != None:
            print('Inciando subtração')
            self.operações.subtração()
            self.atualizar()
            print('Subtração finalizada')

    def multiplicacao(self):
        if self.operações.imagem_2 != None:
            print('Inciando multiplicação')
            self.operações.multiplicação()
            self.atualizar()
            print('Multiplicação finalizada')

    def divisao(self):
        if self.operações.imagem_2 != None:
            print('Inciando divisão')
            self.operações.divisão()
            self.atualizar()
            print('Divisão finalizada')

    def equalizacao(self):
        print('Inciando equalização')
        self.operações.equalização()
        self.atualizar()
        print('Equalização finalizada')

    def filtroSuavizacao(self):
        num, ok = QtGui.QInputDialog.getInt(self, '', 'Entre com o tamanho da máscara (número ímpar maior do que 2)')

        if ok and num > 2 and num % 2 != 0:
            print('Iniciando suavização')
            self.operações.filtro_suavização(num)
            self.atualizar()
            print('Suavização finalizada')

    def filtroRealce(self):
        print('Iniciando realce')
        self.operações.filtro_realce()
        self.atualizar()
        print('Realce finalizado')


