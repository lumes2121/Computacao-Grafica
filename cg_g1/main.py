from PyQt4 import QtGui
import sys
from gui import Ui_MainWindow

def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
