from Models.hospital import Hospital
from Presenters.presentador_incisoB import PresentadorIncisoB
from Presenters.presentador_incisoC import PresentadorIncisoC
from Presenters.presentador_incisoD import PresentadorIncisoD
from Presenters.presentador_incisoE import PresentadorIncisoE
from Presenters.presentador_incisoF import PresentadorIncisoF
from View.Controller.vista_Incisos import VentanaIncisos


class PresentadorIncisos:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__hospital = Hospital(self.__repositorio)
        self.__vista = VentanaIncisos(self)
        self.__vista.setWindowTitle('RESPUESTAS A LOS INCISOS')

    def iniciar(self):
        self.__vista.iniciar()

    def cerrar(self):
        self.__vista.cerrar()

    def verIncisoB(self):
        p = PresentadorIncisoB(self.__repositorio)
        p.iniciar()

    def verIncisoC(self):
        p = PresentadorIncisoC(self.__repositorio)
        p.iniciar()

    def verIncisoD(self):
        p = PresentadorIncisoD(self.__repositorio)
        p.iniciar()

    def verIncisoE(self):
        p = PresentadorIncisoE(self.__repositorio)
        p.iniciar()

    def verIncisoF(self):
        p = PresentadorIncisoF(self.__repositorio)
        p.iniciar()
