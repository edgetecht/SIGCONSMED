import datetime
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class VentanaConsultas(QDialog):
    def __init__(self, presentador):
        self.__presentador = presentador
        QDialog.__init__(self)
        uic.loadUi('./View/ui/vistaConsultas.ui', self)

        self.btn_add.clicked.connect(self.__presentador.insertar_o_actualizar)
        self.btn_edit.clicked.connect(self.__presentador.insertar_o_actualizar)
        self.btn_delete.clicked.connect(self.__presentador.eliminar)
        self.btn_reset.clicked.connect(self.__presentador.reiniciar)
        self.btn_cancel.clicked.connect(self.close)
        self.tablaTurnos.itemClicked.connect(self.__presentador.habilitar_botones_generales)

        self.tablaTurnos.setColumnCount(16)
        self.tablaTurnos.setHorizontalHeaderLabels(['Código de la Consulta', 'Fecha', 'Hora', 'Especialidad',
                                                    'Datos del Paciente', 'Datos de Doctor', 'Motivo', 'Es Alta',
                                                    'Nro. de Secuencia', 'Tiene Examanes', 'Es Urgencia',
                                                    'Sangre', 'Orina', 'Rayos X', 'Ultrasonido', 'TAC'])
        self.tablaTurnos.resizeColumnsToContents()

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self, tabla):
        while tabla.rowCount() > 0:
            tabla.removeRow(0)

    def agregar_elemento_tablaTurnos(self, tabla, fila, columna, texto):
        tabla.setItem(fila, columna, QTableWidgetItem(texto))

    def get_valor(self, componente, tipo):
        if tipo == 'text':
            return componente.text().strip()
        elif tipo == 'combo':
            return componente.currentText()
        elif tipo == 'date':
            return componente.date()
        elif tipo == 'time':
            return componente.time()
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
        elif tipo == 'time':
            componente.setTime(valor)
        elif tipo == 'combo':
            componente.setCurrentText(valor)
        elif tipo == 'number':
            componente.setValue(valor)
        elif tipo == 'radio' or tipo == 'check':
            componente.setChecked(valor)

    def set_index(self, combo, index):
        combo.setCurrentIndex(index)

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

    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        motivo = self.get_valor(self.text_motivo, 'text')
        especialidad = self.get_valor(self.text_especialidadC, 'text')
        fecha = self.get_valor(self.date_fecha, 'date')
        if len(motivo) == 0:
            raise Exception(msg.format('Motivo de la Consulta'))
        if len(especialidad) == 0:
            raise Exception(msg.format('Especialidad'))
        if fecha >= datetime.date.today():
            raise Exception('La fecha de consulta debe ser mayor a la fecha actual')
        self.validar_letras_numeros(motivo, 'Motivo de la Consulta')
        self.validar_letras_numeros(especialidad, 'Especialidad')

    def nro_secuencia_paciente(self):
        nro = self.get_valor(self.number_secuencia, 'number')
        paciente = self.get_valor(self.combo_paciente, 'combo')
        if paciente == paciente:
            return sum(nro, 1)
