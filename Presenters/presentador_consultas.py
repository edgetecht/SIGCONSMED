from PyQt5.QtCore import QDate, QTime

from Models.consulta import Consulta
from Models.hospital import Hospital
from View.Controller.vistaConsultas import VentanaConsultas


class PresentadorConsultas:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__hospital = Hospital(self.__repositorio)

    @property
    def repositorio(self):
        return self.__repositorio

    def iniciar(self):
        self.__vista = VentanaConsultas(self)
        self.__vista.show()
        self.__vista.setWindowTitle('CONSULTAS')
        self.__index = -1
        self.cargar_datos_tablaTurnos()
        self.cargar_datos_combo_all(self.__vista.combo_paciente, self.repositorio.lista_pacientes)
        self.cargar_datos_combo_all(self.__vista.combo_medico, self.repositorio.lista_medicos)
        if len(self.repositorio.lista_pacientes) == 0 or len(self.repositorio.lista_medicos) == 0:
            self.__vista.btn_add.setEnabled(False)

    def cerrar(self):
        self.__vista.close()

    def reiniciar(self):
        self.cerrar()
        self.iniciar()

    def cargar_datos_combo_all(self, combo, lista):
        for item in lista:
            combo.addItem(item.string('_'))

    def cargar_datos_tablaTurnos(self):
        self.__vista.vaciar_tabla(self.__vista.tablaTurnos)
        for object in self.repositorio.lista_consultas:
            es_alta = 'NO'
            tiene_examenes = 'NO'
            es_urgente = 'NO'
            sangre = 'NO'
            orina = 'NO'
            rayos_x = 'NO'
            ultrasonido = 'NO'
            tac = 'NO'
            if object.es_alta:
                es_alta = 'SI'
            if object.tiene_examenes:
                tiene_examenes = 'SI'
            if object.es_urgente:
                es_urgente = 'SI'
            if object.sangre:
                sangre = 'SI'
            if object.orina:
                orina = 'SI'
            if object.rayos_x:
                rayos_x = 'SI'
            if object.ultrasonido:
                ultrasonido = 'SI'
            if object.tac:
                tac = 'SI'
            i = self.__vista.tablaTurnos.rowCount()
            self.__vista.tablaTurnos.insertRow(i)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 0, str(object.codigoDconsulta))
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 1,
                                                      QDate.toString(object.fecha, 'dd-MM-yyyy'))
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 2,
                                                      QTime.toString(object.hora, "hh:mm:ss A "))
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 3, object.especialidad)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 4, "CI: "+object.paciente.ci+"  Nombre y apellidos: " +
                                                      object.paciente.nombre_apellido)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 5, "CI: "+object.medico.ci + "  Nombre y apellidos: " +
                                                      object.medico.nombre_apellido)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 6, object.motivoDconsulta)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 7, es_alta)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 8, str(object.nro_secuencia))
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 9, tiene_examenes)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 10, es_urgente)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 11, sangre)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 12, orina)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 13, rayos_x)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 14, ultrasonido)
            self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 15, tac)
        self.__vista.tablaTurnos.resizeColumnsToContents()

    def insertar_o_actualizar(self):
        try:
            self.__vista.validar_controles()
            codigoDconsulta = self.__vista.get_valor(self.__vista.number_codigo, 'number')
            fecha = self.__vista.get_valor(self.__vista.date_fecha, 'date')
            hora = self.__vista.get_valor(self.__vista.timeEdit, 'time')
            especialidad = self.__vista.get_valor(self.__vista.text_especialidadC, 'text')
            paciente = self.repositorio.lista_pacientes[self.__vista.get_index(self.__vista.combo_paciente)]
            medico = self.repositorio.lista_medicos[self.__vista.get_index(self.__vista.combo_medico)]
            motivoDconsulta = self.__vista.get_valor(self.__vista.text_motivo, 'text')
            es_alta = self.__vista.get_valor(self.__vista.checkBox_alta, 'check')
            nro_secuencia = self.__vista.get_valor(self.__vista.number_secuencia, 'number')
            tiene_examenes = self.__vista.get_valor(self.__vista.checkBox_examenes, 'check')
            es_urgente = self.__vista.get_valor(self.__vista.checkBox_urgente, 'check')
            sangre = self.__vista.get_valor(self.__vista.checkBox_sangre, 'check')
            orina = self.__vista.get_valor(self.__vista.checkBox_orina, 'check')
            rayos_x = self.__vista.get_valor(self.__vista.checkBox_rayos, 'check')
            ultrasonido = self.__vista.get_valor(self.__vista.checkBox_ultrasonido, 'check')
            tac = self.__vista.get_valor(self.__vista.checkBox_tac, 'check')

            consulta = Consulta(codigoDconsulta, fecha, hora, especialidad, paciente, medico,
                                motivoDconsulta, es_alta, nro_secuencia, tiene_examenes, es_urgente,
                                sangre, orina, rayos_x, ultrasonido, tac)
            if self.__index == -1:
                self.__repositorio.insertar(consulta)
            else:
                consulta_old = self.repositorio.lista_consultas[self.__index]
                self.__repositorio.actualizar(consulta_old, consulta)
            self.reiniciar()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def cargar_datos_formulario(self):
        if self.__index != -1:
            consulta = self.repositorio.lista_consultas[self.__index]

            self.__vista.set_valor(self.__vista.number_codigo, consulta.codigoDconsulta, 'number')
            self.__vista.set_valor(self.__vista.date_fecha, consulta.fecha, 'date')
            self.__vista.set_valor(self.__vista.timeEdit, consulta.hora, 'time')
            self.__vista.set_valor(self.__vista.text_especialidadC, consulta.especialidad, 'text')
            self.__vista.set_valor(self.__vista.combo_paciente, consulta.paciente.string('_'), 'combo')
            self.__vista.set_valor(self.__vista.combo_medico, consulta.medico.string('_'), 'combo')
            self.__vista.set_valor(self.__vista.text_motivo, consulta.motivoDconsulta, 'text')
            self.__vista.set_valor(self.__vista.checkBox_alta, consulta.es_alta, 'check')
            self.__vista.set_valor(self.__vista.number_secuencia, consulta.nro_secuencia, 'number')
            self.__vista.set_valor(self.__vista.checkBox_examenes, consulta.tiene_examenes, 'check')
            self.__vista.set_valor(self.__vista.checkBox_urgente, consulta.es_urgente, 'check')
            self.__vista.set_valor(self.__vista.checkBox_sangre, consulta.sangre, 'check')
            self.__vista.set_valor(self.__vista.checkBox_orina, consulta.orina, 'check')
            self.__vista.set_valor(self.__vista.checkBox_rayos, consulta.rayos_x, 'check')
            self.__vista.set_valor(self.__vista.checkBox_ultrasonido, consulta.ultrasonido, 'check')
            self.__vista.set_valor(self.__vista.checkBox_tac, consulta.tac, 'check')

    def eliminar(self):
        try:
            index = self.__vista.tablaTurnos.currentRow()
            if index == -1:
                raise Exception('Debe seleccionar una fila para eliminarla.')
            object = self.repositorio.lista_consultas[index]
            self.repositorio.eliminar(object)
            self.reiniciar()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def habilitar_botones_generales(self):
        index = self.__vista.tablaTurnos.currentRow()
        if index != -1:
            self.__index = index
            self.__vista.btn_edit.setEnabled(True)
            self.__vista.btn_delete.setEnabled(True)
            self.__vista.btn_add.setEnabled(False)
            self.cargar_datos_formulario()
