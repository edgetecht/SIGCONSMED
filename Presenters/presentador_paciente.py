from Models.hospital import Hospital
from Models.paciente import Paciente
from View.Controller.vistaPacientes import VentanaPacientes


class PresentadorPacientes:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__hospital = Hospital(self.__repositorio)

    @property
    def repositorio(self):
        return self.__repositorio

    def iniciar(self):
        self.__vista = VentanaPacientes(self)
        self.__vista.show()
        self.__vista.setWindowTitle('PACIENTES')
        self.__index = -1
        self.cargar_datos_combo_all(self.__vista.combo_medicoRemite, self.repositorio.lista_medicos)
        self.cargar_datos_tabla()

    def cerrar(self):
        self.__vista.close()

    def reiniciar(self):
        self.cerrar()
        self.iniciar()

    def cargar_datos_combo_all(self, combo, lista):
        for item in lista:
            combo.addItem(item.string('_'))

    def cargar_datos_tabla(self):
        self.__vista.vaciar_tabla(self.__vista.tablePacientes)
        for object in self.repositorio.lista_pacientes:
            i = self.__vista.tablePacientes.rowCount()
            self.__vista.tablePacientes.insertRow(i)
            self.__vista.agregar_elemento_tabla(self.__vista.tablePacientes, i, 0, object.ci)
            self.__vista.agregar_elemento_tabla(self.__vista.tablePacientes, i, 1, object.nombre_apellido)
            self.__vista.agregar_elemento_tabla(self.__vista.tablePacientes, i, 2, str(object.edad))
            self.__vista.agregar_elemento_tabla(self.__vista.tablePacientes, i, 3, object.sexo)
            self.__vista.agregar_elemento_tabla(self.__vista.tablePacientes, i, 4, object.direccion)
            self.__vista.agregar_elemento_tabla(self.__vista.tablePacientes, i, 5, object.medico_remite.nombre_apellido
                                                )
        self.__vista.tablePacientes.resizeColumnsToContents()

    def cargar_datos_formulario(self):
        if self.__index != -1:
            paciente = self.repositorio.lista_pacientes[self.__index]
            self.__vista.set_valor(self.__vista.text_ci, paciente.ci, 'text')
            self.__vista.set_valor(self.__vista.text_nombre, paciente.nombre_apellido, 'text')
            self.__vista.set_valor(self.__vista.number_edad, paciente.edad, 'number')
            self.__vista.set_valor(self.__vista.text_direccion, paciente.direccion, 'text')
            self.__vista.set_valor(self.__vista.combo_medicoRemite, paciente.medico_remite.string('_'), 'combo')
            if paciente.sexo == 'M':
                self.__vista.set_valor(self.__vista.radio_M, True, 'radio')
            else:
                self.__vista.set_valor(self.__vista.radio_F, True, 'radio')

    def insertar_o_actualizar(self):
        try:
            self.__vista.validar_controles()

            ci = self.__vista.get_valor(self.__vista.text_ci, 'text')
            nombre_apellido = self.__vista.get_valor(self.__vista.text_nombre, 'text')
            edad = self.__vista.get_valor(self.__vista.number_edad, 'number')
            sexo = self.__vista.get_valor(self.__vista.radio_M, 'radio')
            if not sexo:
                sexo = self.__vista.get_valor(self.__vista.radio_F, 'radio')
            direccion = self.__vista.get_valor(self.__vista.text_direccion, 'text')
            medico_remite = self.repositorio.lista_medicos[self.__vista.get_index(self.__vista.combo_medicoRemite)]

            paciente = Paciente(ci, nombre_apellido, edad, sexo, direccion, medico_remite)

            if self.__index == -1:
                self.__repositorio.insertar(paciente)
            else:
                paciente_old = self.repositorio.lista_pacientes[self.__index]
                self.repositorio.actualizar(paciente_old, paciente)
            self.reiniciar()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar(self):
        try:
            index = self.__vista.tablePacientes.currentRow()
            if index == -1:
                raise Exception('Debe seleccionar una fila para eliminarla.')
            object = self.repositorio.lista_pacientes[index]
            self.repositorio.eliminar(object)
            self.reiniciar()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def habilitar_botones_generales(self):
        index = self.__vista.tablePacientes.currentRow()
        if index != -1:
            self.__index = index
            self.__vista.btn_edit.setEnabled(True)
            self.__vista.btn_delete.setEnabled(True)
            self.__vista.btn_add.setEnabled(False)
            self.cargar_datos_formulario()
