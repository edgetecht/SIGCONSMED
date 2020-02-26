from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox


class VentanaIncisos(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('./View/ui/vista_incisos.ui', self)

        self.btn_incisoB.clicked.connect(self.__presentador.verIncisoB)
        self.btn_incisoC.clicked.connect(self.__presentador.verIncisoC)
        self.btn_incisoD.clicked.connect(self.__presentador.verIncisoD)
        self.btn_incisoE.clicked.connect(self.__presentador.verIncisoE)
        self.btn_incisoF.clicked.connect(self.__presentador.verIncisoF)

    def iniciar(self):
        self.show()


    def cerrar(self):
        self.close()

    def restart(self):
        self.cerrar()
        self.iniciar()

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    '''def verIncisoB(self):
        self.mdiArea.closeActiveSubWindow()
        dialogo = VentanaIncisoB(self)
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo,
                                  QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()

    def verIncisoC(self):
        self.mdiArea.closeActiveSubWindow()
        dialogo = VentanaIncisoC(self)
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo,
                                  QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()

    def verIncisoD(self):
        self.mdiArea.closeActiveSubWindow()
        dialogo = VentanaIncisoD(self)
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo,
                                  QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()

    def verIncisoE(self):
        self.mdiArea.closeActiveSubWindow()
        dialogo = VentanaIncisoE(self)
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo,
                                  QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()

    def verIncisoF(self):
        self.mdiArea.closeActiveSubWindow()
        dialogo = VentanaIncisoF(self)
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo,
                                  QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()'''
