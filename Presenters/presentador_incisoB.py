from Models.hospital import Hospital
from View.Controller.ventana_incisoB import VentanaIncisoB

class PresentadorIncisoB:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__hospital = Hospital(self.__repositorio)

    @property
    def repositorio(self):
        return self.__repositorio

    def iniciar(self):
        self.__vista = VentanaIncisoB(self)
        self.__vista.show()
        self.__vista.setWindowTitle('INCISO B')


    def cerrar(self):
        self.__vista.close()

    def show(self):
        try:
            self.__vista.validar_controles()
            codigoDconsulta = self.__vista.get_valor(self.__vista.number_codigo, 'number')
            result = self.__hospital.costo_consulta(codigoDconsulta)
            if result:
                self.__vista.set_valor(self.__vista.text_result, 'El costo de la consulta es de $ ' + str(result), 'text')
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def restart(self):
        self.cerrar()
        self.iniciar()

