from PyQt5.QtWidgets import QDialog
from View.Controller.ventana_logOut import Ventana_logOut


class PresentadorLogOut(QDialog):
    def iniciar(self):
        dialogo = Ventana_logOut()
        ejecLogout = dialogo.exec_()

        if ejecLogout == QDialog.Accepted:
            self.close()
