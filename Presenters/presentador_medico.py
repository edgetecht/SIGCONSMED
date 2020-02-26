from Models.medico import Medico
from Models.hospital import Hospital
from View.Controller.vistaMedicos import VentanaMedicos


class PresentadorMedicos:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__hospital = Hospital(self.__repositorio)

    @property
    def repositorio(self):
        return self.__repositorio

    def iniciar(self):
        self.__vista = VentanaMedicos(self)
        self.__vista.show()
        self.__vista.setWindowTitle('MÉDICOS')
        self.__index = -1
        self.cargar_datos_tabla()

    def cerrar(self):
        self.__vista.close()

    def reiniciar(self):
        self.cerrar()
        self.iniciar()

    # ['# Registro', 'Nombre', 'Edad', 'Sexo', 'Especialidad', 'Año Graduado']
    def cargar_datos_tabla(self):
        self.__vista.vaciar_tabla(self.__vista.tableMedicos)
        for object in self.repositorio.lista_medicos:
            i = self.__vista.tableMedicos.rowCount()
            self.__vista.tableMedicos.insertRow(i)
            self.__vista.agregar_elemento_tabla(self.__vista.tableMedicos, i, 0, object.ci)
            self.__vista.agregar_elemento_tabla(self.__vista.tableMedicos, i, 1, object.nombre_apellido)
            self.__vista.agregar_elemento_tabla(self.__vista.tableMedicos, i, 2, object.sexo)
            self.__vista.agregar_elemento_tabla(self.__vista.tableMedicos, i, 3, object.especialidad)
            self.__vista.agregar_elemento_tabla(self.__vista.tableMedicos, i, 4, str(object.anio_graduado))
            self.__vista.agregar_elemento_tabla(self.__vista.tableMedicos, i, 5, str(object.anio_experiencia))
            self.__vista.agregar_elemento_tabla(self.__vista.tableMedicos, i, 6, object.centro_que_pertenece)
            self.__vista.agregar_elemento_tabla(self.__vista.tableMedicos, i, 7, object.nivel_centro)
        self.__vista.tableMedicos.resizeColumnsToContents()

    def cargar_datos_formulario(self):
        if self.__index != -1:
            medico = self.repositorio.lista_medicos[self.__index]
            self.__vista.set_valor(self.__vista.text_ci, medico.ci, 'text')
            self.__vista.set_valor(self.__vista.text_nombre, medico.nombre_apellido, 'text')
            self.__vista.set_valor(self.__vista.text_especialidad, medico.especialidad, 'text')
            self.__vista.set_valor(self.__vista.number_anio_graduado, medico.anio_graduado, 'number')
            self.__vista.set_valor(self.__vista.number_exp, medico.anio_experiencia, 'number')
            self.__vista.set_valor(self.__vista.text_centro, medico.centro_que_pertenece, 'text')
            self.__vista.set_valor(self.__vista.combo_nivel, medico.nivel_centro, 'combo')
            if medico.sexo == 'M':
                self.__vista.set_valor(self.__vista.radio_M, True, 'radio')
            else:
                self.__vista.set_valor(self.__vista.radio_F, True, 'radio')

    def insertar_o_actualizar(self):
        try:
            self.__vista.validar_controles()

            ci = self.__vista.get_valor(self.__vista.text_ci, 'text')
            nombre_apellido = self.__vista.get_valor(self.__vista.text_nombre, 'text')
            especialidad = self.__vista.get_valor(self.__vista.text_especialidad, 'text')
            anio_graduado = self.__vista.get_valor(self.__vista.number_anio_graduado, 'number')
            anios_experiencia = self.__vista.get_valor(self.__vista.number_exp, 'number')
            centro_que_pertenece = self.__vista.get_valor(self.__vista.text_centro, 'text')
            nivel_centro = self.__vista.get_valor(self.__vista.combo_nivel, 'combo')
            sexo = self.__vista.get_valor(self.__vista.radio_M, 'radio')
            if not sexo:
                sexo = self.__vista.get_valor(self.__vista.radio_F, 'radio')

            medico = Medico(ci, nombre_apellido, sexo, especialidad, anio_graduado, anios_experiencia,
                            centro_que_pertenece, nivel_centro)
            if self.__index == -1:
                self.__repositorio.insertar(medico)
            else:
                medico_old = self.repositorio.lista_medicos[self.__index]
                self.repositorio.actualizar(medico_old, medico)
            self.reiniciar()

        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def eliminar(self):
        try:
            index = self.__vista.tableMedicos.currentRow()
            if index == -1:
                raise Exception('Debe seleccionar una fila para eliminarla.')
            object = self.repositorio.lista_medicos[index]
            self.repositorio.eliminar(object)
            self.reiniciar()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def habilitar_botones_generales(self):
        index = self.__vista.tableMedicos.currentRow()
        if index != -1:
            self.__index = index
            self.__vista.btn_edit.setEnabled(True)
            self.__vista.btn_delete.setEnabled(True)
            self.__vista.btn_add.setEnabled(False)
            self.cargar_datos_formulario()
