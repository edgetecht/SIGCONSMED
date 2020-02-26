from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class VentanaIncisoF(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('./View/ui/ventana_IncisoF.ui', self)

        self.btn_show.clicked.connect(self.__presentador.show)
        self.btn_restart.clicked.connect(self.__presentador.restart)
        self.btn_cancel.clicked.connect(self.__presentador.cerrar)
        self.tablaTurnos.setColumnCount(9)
        self.tablaTurnos.setHorizontalHeaderLabels(['Código de la Consulta', 'Fecha', 'Hora', 'Especialidad', 'Datos del Paciente',
                                                    'Datos de Doctor', 'Motivo', 'Es Alta', 'Nro. de Secuencia'])
        self.tablaTurnos.resizeColumnsToContents()

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

    def vaciar_tabla(self, tabla):
        while tabla.rowCount() > 0:
            tabla.removeRow(0)

    def agregar_elemento_tablaTurnos(self, tabla, fila, columna, texto):
        tabla.setItem(fila, columna, QTableWidgetItem(texto))

    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        ci = self.get_valor(self.text_ci, 'text')
        anio_nac = int(ci[:2])
        mes_nac = int(ci[2:4])
        dia_nac = int(ci[4:6])
        if mes_nac > 12 or mes_nac == 0:
            raise Exception('Nro de CI erroneo, el mes debe ser menor o igual a 12')
        elif dia_nac > 31 or dia_nac == 0:
            raise Exception('Nro de CI erroneo, el día debe estar entre 1 y 31')
        elif dia_nac > 29 and mes_nac == 2:
            raise Exception('Nro de CI erroneo, el mes de febrero solo puede tener 29 días')
        elif dia_nac == 29 and mes_nac == 2 and anio_nac % 4 != 0:
            raise Exception('Nro de CI erroneo, el mes de febrero solo puede tener 29 días')
        if len(ci) == 0:
            raise Exception(msg.format('CI'))
        if len(ci) != 11 and len(ci) != 6:
            raise Exception('El CI debe tener 6 u 11 dígitos.')
        if not ci.isdigit():
            raise Exception('El CI sólo puede contener números.')

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)
