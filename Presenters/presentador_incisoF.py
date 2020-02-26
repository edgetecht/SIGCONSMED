from PyQt5.QtCore import QDate, QTime
from Models.hospital import Hospital
from View.Controller.ventana_incisoF import VentanaIncisoF


class PresentadorIncisoF:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__hospital = Hospital(self.__repositorio)

    @property
    def repositorio(self):
        return self.__repositorio

    def iniciar(self):
        self.__vista = VentanaIncisoF(self)
        self.__vista.show()
        self.__vista.setWindowTitle('INCISO F')

    def cerrar(self):
        self.__vista.close()

    def show(self):
        self.__vista.tablaTurnos.setRowCount(0)
        try:
            self.__vista.validar_controles()
            ci = self.__vista.get_valor(self.__vista.text_ci, 'text')
            lista = self.__hospital.listado_consultas_sin_analisis(ci)
            if lista:
                for object in lista:
                    es_alta = 'NO'
                    if object.es_alta:
                        es_alta = 'SI'
                    i = self.__vista.tablaTurnos.rowCount()
                    self.__vista.tablaTurnos.insertRow(i)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 0, str(object.codigoDconsulta))
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 1, QDate.toString(object.fecha, 'dd-MM-yyyy'))
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 2, QTime.toString(object.hora, "hh:mm:ss A "))
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 3, object.especialidad)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 4, "CI: "+object.paciente.ci+"  Nombre y apellidos: " + object.paciente.nombre_apellido)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 5, "CI: "+object.medico.ci + "  Nombre y apellidos: " + object.medico.nombre_apellido)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 6, object.motivoDconsulta)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 7, es_alta)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 8, str(object.nro_secuencia))
                    self.__vista.tablaTurnos.resizeColumnsToContents()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def restart(self):
        self.cerrar()
        self.iniciar()
