from Models.hospital import Hospital
from View.Controller.ventana_IncisoD import VentanaIncisoD

class PresentadorIncisoD:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__hospital = Hospital(self.__repositorio)

    @property
    def repositorio(self):
        return self.__repositorio

    def iniciar(self):
        self.__vista = VentanaIncisoD(self)
        self.__vista.show()
        self.__vista.setWindowTitle('INCISO D')


    def cerrar(self):
        self.__vista.close()

    def show(self):
        try:
            fecha = self.__vista.get_valor(self.__vista.date_fecha, 'date')
            especialidad = self.__vista.get_valor(self.__vista.text_especialidad, 'text')
            result = self.__hospital.paciente_de_mayor_edad(fecha, especialidad)
            if result:
                self.__vista.set_valor(self.__vista.text_result, result.string('\n'), 'text')
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def restart(self):
        self.cerrar()
        self.iniciar()
