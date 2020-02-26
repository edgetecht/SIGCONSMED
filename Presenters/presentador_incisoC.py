from PyQt5.QtCore import QDate, QTime

from Models.hospital import Hospital
from View.Controller.ventana_incisoC import VentanaIncisoC


class PresentadorIncisoC:
    def __init__(self, repo):
        self.__repositorio = repo
        self.__hospital = Hospital(self.__repositorio)

    @property
    def repositorio(self):
        return self.__repositorio

    def iniciar(self):
        self.__vista = VentanaIncisoC(self)
        self.__vista.show()
        self.__vista.setWindowTitle('INCISO C')

    def cerrar(self):
        self.__vista.close()

    def show(self):
        self.__vista.tablaTurnos.setRowCount(0)
        try:
            ci = self.__vista.get_valor(self.__vista.text_ci, 'text')
            lista = self.__hospital.tipo_examen_paciente(ci)
            if lista:
                for object in lista:
                    sangre = 'NO'
                    orina = 'NO'
                    rayos_x = 'NO'
                    ultrasonido = 'NO'
                    tac = 'NO'
                    if object[0]:
                        sangre = 'SI'
                    if object[1]:
                        orina = 'SI'
                    if object[2]:
                        rayos_x = 'SI'
                    if object[3]:
                        ultrasonido = 'SI'
                    if object[4]:
                        tac = 'SI'
                    i = self.__vista.tablaTurnos.rowCount()
                    self.__vista.tablaTurnos.insertRow(i)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 0, sangre)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 1, orina)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 2, rayos_x)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 3, ultrasonido)
                    self.__vista.agregar_elemento_tablaTurnos(self.__vista.tablaTurnos, i, 4, tac)
                self.__vista.tablaTurnos.resizeColumnsToContents()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def restart(self):
        self.cerrar()
        self.iniciar()
