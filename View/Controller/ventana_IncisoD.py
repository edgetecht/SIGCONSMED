from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class VentanaIncisoD(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('./View/ui/ventana_IncisoD.ui', self)

        self.btn_show.clicked.connect(self.__presentador.show)
        self.btn_restart.clicked.connect(self.__presentador.restart)
        self.btn_cancel.clicked.connect(self.__presentador.cerrar)

        self.setModal(True)

    def get_valor(self, componente, tipo):
        if tipo == 'text':
            return componente.text().strip()
        elif tipo == 'combo':
            return componente.currentText()
        elif tipo == 'date':
            return componente.date()
        elif tipo == 'number':
            return componente.value()
        elif tipo == 'radio':
            if componente.isChecked():
                return componente.text().strip()
        elif tipo == 'check':
            if componente.isChecked():
                return True
            else:
                return False

    def get_index(self, combo):
        return combo.currentIndex()

    def set_valor(self, componente, valor, tipo):
        if tipo == 'text':
            componente.setText(valor)
        elif tipo == 'date':
            componente.setDate(valor)
        elif tipo == 'combo':
            componente.setCurrentText(valor)
        elif tipo == 'number':
            componente.setValue(valor)
        elif tipo == 'radio' or tipo == 'check':
            componente.setChecked(valor)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)