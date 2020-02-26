from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog

from View.Controller.ventana_logOut import Ventana_logOut


class VentanaPrincipal(QMainWindow):
    def __init__(self, presentador):
        super(QMainWindow, self).__init__()
        uic.loadUi('View/ui/vistaPrincipal.ui', self)
        self.__presentador = presentador

        self.pb_agenda.clicked.connect(self.__presentador.pb_agenda_on_click)
        self.pb_turnos.clicked.connect(self.__presentador.pb_turnos_on_click)
        self.pb_pacientes.clicked.connect(self.__presentador.pb_pacientes_on_click)
        self.pb_medicos.clicked.connect(self.__presentador.pb_medicos_on_click)
        self.pd_logOut.clicked.connect(self.__presentador.pb_logOut_on_click)

    def iniciar(self):
        self.show()

    def cerrar(self):
        dialogo = Ventana_logOut()
        ejecLogout = dialogo.exec_()
        if ejecLogout == QDialog.Accepted:
            self.close()

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)