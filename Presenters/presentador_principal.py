import sys

from PyQt5.QtWidgets import QApplication
from Models.hospital import Hospital
from Models.repositorio import Repositorio
from Presenters.presentador_consultas import PresentadorConsultas
from Presenters.presentador_logOut import PresentadorLogOut
from Presenters.presentador_medico import PresentadorMedicos
from Presenters.presentador_paciente import PresentadorPacientes
from Presenters.presentador_incisos import PresentadorIncisos
from View.Controller.vistaPrincipal import VentanaPrincipal


class PresentadorPrincipal:
    def __init__(self):
        self.__repositorio = Repositorio()
        self.__hospital = Hospital(self.__repositorio)
        self.__app = QApplication(sys.argv)
        self.__window_principal = VentanaPrincipal(self)

    def iniciar(self):
        self.__window_principal.iniciar()
        self.__window_principal.showMaximized()
        self.__app.exec_()

    def cerrar(self):
        self.__window_principal.cerrar()

    def pb_agenda_on_click(self):
        p = PresentadorIncisos(self.__repositorio)
        p.iniciar()

    def pb_turnos_on_click(self):
        p = PresentadorConsultas(self.__repositorio)
        p.iniciar()

    def pb_pacientes_on_click(self):
        p = PresentadorPacientes(self.__repositorio)
        p.iniciar()

    def pb_medicos_on_click(self):
        p = PresentadorMedicos(self.__repositorio)
        p.iniciar()

    def pb_logOut_on_click(self):
        p = PresentadorLogOut()
        p.iniciar()

