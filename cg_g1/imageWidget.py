from PyQt4 import QtCore, QtGui


class ImageWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(ImageWidget, self).__init__(parent)
        self.Qimg = None

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        if self.Qimg :
            largura = event.rect().height() * (self.Qimg.width()/self.Qimg.height())

            if largura < event.rect().width():
                rect = QtCore.QRect((event.rect().width()-largura)/2, 0, largura, event.rect().height())
            else:
                altura = event.rect().width() * (self.Qimg.height()/self.Qimg.width())
                rect = QtCore.QRect(0, (event.rect().height()-altura)/2, event.rect().width(), altura)

            painter.drawImage(rect, self.Qimg)
        painter.end()