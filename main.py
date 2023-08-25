import sys
import socket
import os
import requests
import json
import platform
import time
import psutil
from ping3 import ping, verbose_ping
import netifaces as ni
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
from janela import Ui_Janela
from info import Ui_Info
from rede import Ui_Rede

# GLOBAL Nomes

HD_PARTICAO = os.statvfs("/")
HD_TOTAL = (HD_PARTICAO.f_frsize * HD_PARTICAO.f_blocks) / 1e9
HD_LIVRE = (HD_PARTICAO.f_frsize * HD_PARTICAO.f_bfree) / 1e9
MEMORIA = psutil.virtual_memory()
MEMORIA = (MEMORIA.total / 1e9)


NOME_PC = socket.gethostname()
NOME_USUARIO = os.getlogin()
NOME_SO = platform.system()
NOME_SO_VERSAO = platform.release()
NOME_SO_ARQUITETURA = platform.architecture()
NOME_SO_ARQUITETURA = NOME_SO_ARQUITETURA[0]


# GLOBAL Funções

# class pegar_ip_externo(QThread):
#    resposta_ip_externo = pyqtSignal(str)

def pegar_ip_externo():
    # time.sleep(0.5) # draminha
    resposta = requests.get("https://api.ipify.org?format=json")
    data = resposta.json()
    ip_externo = data["ip"]
    # self.resposta_ip_externo.emit(ip_externo)
    if ip_externo == None:
        ip_exerno = "0.0.0.0"
    return ip_externo

def pegar_ip_local():

    try:
        interfaces = ni.interfaces()
        for iface in interfaces:
            if iface != 'lo':  # Ignorar interface loopback
                addresses = ni.ifaddresses(iface)
                if ni.AF_INET in addresses:
                    return addresses[ni.AF_INET][0]['addr']
    except:
        pass
    return None


class Janela(QMainWindow, Ui_Janela):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ui
        self.setupUi(self)

        # Ações
        self.actionFechar.triggered.connect(self.close)
        self.actionInformacoes.triggered.connect(self.mostrarInfo)
        self.actionRede.triggered.connect(self.mostrarRede)
        self.widget_atual = None

        # info ui
        """
        self.info_widget = QWidget()
        self.info_ui = Ui_Info()
        self.info_ui.setupUi(self.info_widget)
        """
        # rede ui
        """
        self.rede_widget = QWidget()
        self.rede_ui = Ui_Rede()
        self.rede_ui.setupUi(self.rede_widget)
        """

        # index -> info ui
        self.mostrarInfo()
        self.widget_atual = self.info_widget

    def mostrarInfo(self):
        self.info_widget = QWidget()
        self.info_ui = Ui_Info()
        self.info_ui.setupUi(self.info_widget)
        # apagando a widget anterior
        if self.widget_atual != self.info_widget and self.widget_atual != None:
            self.layoutMiolo.removeWidget(self.widget_atual)
            self.widget_atual.deleteLater()

        # Alimentando as labels do info
        tudo_info = self.info_ui
        tudo_info.valor_nome.setText(NOME_PC)
        tudo_info.valor_sistema.setText(NOME_SO + " " + NOME_SO_VERSAO + " - " + NOME_SO_ARQUITETURA)
        tudo_info.valor_usuario.setText(NOME_USUARIO)
        tudo_info.valor_ram.setText(str(round(MEMORIA, 2)) + " Gb")
        tudo_info.valor_hd.setText(str(round(HD_TOTAL, 2)) + " Gb \ Livre: " + str(round(HD_LIVRE, 2)) + " Gb")
        # self.layoutMiolo.removeWidget(self)
        self.layoutMiolo.addWidget(self.info_widget)
        self.widget_atual = self.info_widget

    def mostrarRede(self):
        self.rede_widget = QWidget()
        self.rede_ui = Ui_Rede()
        self.rede_ui.setupUi(self.rede_widget)
        # apagando a widget anterior
        if self.widget_atual != self.rede_widget and self.widget_atual != None:
            self.layoutMiolo.removeWidget(self.widget_atual)
            self.widget_atual.deleteLater()

        # Alimentando as labels do rede

        # pegar_ip_externo()
        #def pegar_ip_externo(self):
            # self.progresso_externo.setValue(1)
         #   self.thread = pegar_ip_externo()
         #   self.thread.resposta_ip_externo.connect(self.mostrar_ip_externo)
         #   self.thread.start()

        tudo_rede = self.rede_ui
        ip_local = pegar_ip_local()
        if ip_local == None:
            ip_local = "0.0.0.0"
        tudo_rede.valor_local.setText("ok")
        tudo_rede.valor_internet.setText("ok")
        tudo_rede.valor_ip_externo.setText(pegar_ip_externo())
        tudo_rede.valor_ip_local.setText(ip_local)
        self.layoutMiolo.addWidget(self.rede_widget)
        self.widget_atual = self.rede_widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Janela()
    window.show()
    sys.exit(app.exec_())

