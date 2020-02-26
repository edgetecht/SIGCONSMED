from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, qApp


#from main import MainWindow

class Ventana_logOut(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("View/ui/logOut.ui", self)
        
        #Al hacer click en el boton ejecuta la funcion
        self.botonAceptar.clicked.connect(qApp.quit)
        self.botonCancelar.clicked.connect(self.closeEvent)

    def closeEvent(self, event):
         self.close()
