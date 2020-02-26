from Models.hospital import Hospital
from View.Controller.ventana_incisoE import VentanaIncisoE


class PresentadorIncisoE:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__hospital = Hospital(self.__repositorio)

    @property
    def repositorio(self):
        return self.__repositorio

    def iniciar(self):
        self.__vista = VentanaIncisoE(self)
        self.__vista.show()
        self.__vista.setWindowTitle('INCISO E')

    def cerrar(self):
        self.__vista.close()

    def show(self):
        try:
            self.__vista.validar_controles()
            especialidad = self.__vista.get_valor(self.__vista.text_especialidad, 'text')
            fecha = self.__vista.get_valor(self.__vista.date_fecha, 'date')
            result = self.__hospital.por_ciento_consultas_tienen_examenes(especialidad, fecha)
            if result:
                self.__vista.set_valor(self.__vista.text_result, 'El ' + str(result) + ' % de las consultas le enviarion análisis a los '
                                                                                       'pacientes.', 'text')
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def restart(self):
        self.cerrar()
        self.iniciar()
