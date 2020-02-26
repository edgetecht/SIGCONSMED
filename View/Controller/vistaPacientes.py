from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class VentanaPacientes(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('./View/ui/vistaPacientes.ui', self)

        self.btn_add.clicked.connect(self.__presentador.insertar_o_actualizar)
        self.btn_edit.clicked.connect(self.__presentador.insertar_o_actualizar)
        self.btn_delete.clicked.connect(self.__presentador.eliminar)
        self.btn_reset.clicked.connect(self.__presentador.reiniciar)
        self.btn_cancel.clicked.connect(self.close)
        self.tablePacientes.itemClicked.connect(self.__presentador.habilitar_botones_generales)

        self.tablePacientes.setColumnCount(6)
        self.tablePacientes.setHorizontalHeaderLabels(['Carnet de identidiad', 'Nombre y Apellidos', 'Edad', 'Sexo',
                                                       'Dirección Particular', 'Medico Remitente'])
        self.tablePacientes.resizeColumnsToContents()

        self.setModal(True)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self, tabla):
        while tabla.rowCount() > 0:
            tabla.removeRow(0)

    def agregar_elemento_tabla(self, tabla, fila, columna, texto):
        tabla.setItem(fila, columna, QTableWidgetItem(texto))

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

    def set_index(self, combo, index):
        combo.setCurrentIndex(index)

    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        nombre = self.get_valor(self.text_nombre, 'text')
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
        if len(nombre) == 0:
            raise Exception(msg.format('nombre'))
        if len(ci) == 0:
            raise Exception(msg.format('CI'))
        if len(ci) != 11 and len(ci) != 6:
            raise Exception('El CI debe tener 6 u 11 dígitos.')
        if not ci.isdigit():
            raise Exception('El CI sólo puede contener números.')
        self.validar_solo_letras(nombre, 'nombre')

    def validar_solo_letras(self, nombre, atributo):
        lista = nombre.split(' ')
        for substr in lista:
            if not substr.isalpha():
                raise Exception('El atributo ' + atributo + ' sólo puede contener letras y espacios')

    def validar_letras_numeros(self, nombre, atributo):
        lista = nombre.split(' ')
        for substr in lista:
            if not substr.isalnum():
                raise Exception('El atributo ' + atributo + ' sólo puede contener letras y/o números')
