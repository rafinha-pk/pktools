import sys
import socket
import os
import requests
import json
import platform
import time
import psutil
import subprocess
import shutil
from ping3 import ping, verbose_ping
import netifaces as ni
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QPushButton, QProgressBar, QFileDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
from janela import Ui_Janela
from info import Ui_Info
from rede import Ui_Rede
from backup import Ui_backup

# GLOBAL Nomes

if platform.system() == "Windows":
    import wmi
    import ctypes
    c = wmi.WMI()
    for d in c.Win32_LogicalDisk():
        HD_PARTICAO = round((((int(d.Size) / 1024) / 1024) / 1024), 2)
        HD_TOTAL = round((((int(d.Size) / 1024) / 1024) / 1024), 2)
        HD_LIVRE = round((((int(d.FreeSpace) / 1024) / 1024) / 1024), 2)
else:
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

class pegar_ip_externo(QThread):
    resposta_ip_externo = pyqtSignal(str)

    def run(self):
        time.sleep(0.5) # draminha
        try:
            resposta = requests.get("https://api.ipify.org?format=json")
            data = resposta.json()
            ip_externo = data["ip"]
        except:
            ip_externo = "0.0.0.0"
        
        self.resposta_ip_externo.emit(ip_externo)

class fazer_traceroute(QThread):

    def __init__(self, arg):
        super().__init__()
        self.endereco = arg

    resposta_fazer_traceroute = pyqtSignal(str)

    def run(self):
        if NOME_SO == "Linux":
            comando = f"traceroute {self.endereco}"
        else:
            comando = f"tracert {self.endereco}"
        try:
            processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            saida, erro = processo.communicate()
            saida = str(saida)

        except:
            saida = "Sem conexão"

        if NOME_SO == "Linux":
            self.resposta_fazer_traceroute.emit(saida.replace("\\n", "\n"))
        else:
            self.resposta_fazer_traceroute.emit(saida.replace("\\r\\n", "\n"))


def pegar_ip_local():
    try:
        interfaces = ni.interfaces()
        for iface in interfaces:
            addresses = ni.ifaddresses(iface)
            if ni.AF_INET in addresses:
                for addr_info in addresses[ni.AF_INET]:
                    if 'addr' in addr_info:
                        ip_local = addr_info['addr']
                        default_gateway = ni.gateways()['default'][ni.AF_INET]
                        ip_gateway = default_gateway[0]
                        try:
                            response = ping(ip_gateway, timeout=2)
                            if response is not None and ip_local != "127.0.0.1":
                                return ip_local
                        except:
                            pass
    except:
        pass
    return None

def eh_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


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
        self.actionBackup.triggered.connect(self.mostrarBackup)
        self.widget_atual = None

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
        if NOME_SO == "Windows":
            tudo_info.valor_hd.setText(str(HD_TOTAL) + " Gb \ Livre: " + str(HD_LIVRE) + " Gb")
        else:
            tudo_info.valor_hd.setText(str(round(HD_TOTAL, 2)) + " Gb \ Livre: " + str(round(HD_LIVRE, 2)) + " Gb")
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

        tudo_rede = self.rede_ui
        ip_local = pegar_ip_local()
        if ip_local == None:
            ip_local = "0.0.0.0"
            tudo_rede.valor_local.setText("sem")
        else:
            tudo_rede.valor_local.setText("ok")
        tudo_rede.valor_internet.setText("...")
        tudo_rede.valor_ip_local.setText(ip_local)
        self.pegar_ip_externo(tudo_rede=tudo_rede)
        tudo_rede.btn_testar.clicked.connect(lambda :self.testarRede(tudo_rede=tudo_rede))

        if NOME_SO == "Windows" and eh_admin() == False:
            tudo_rede.btn_testar.setEnabled(False)

        self.layoutMiolo.addWidget(self.rede_widget)
        self.widget_atual = self.rede_widget
    def testarRede(self, tudo_rede):
        endereco = tudo_rede.valor_endereco.text()
        resposta = "Enviando requisição para " + endereco + "\n"
        if tudo_rede.check_ping.isChecked() and endereco:
            # tudo_rede.valor_resposta.setText("ping!\n")
            contador_ping = 0;
            while contador_ping < 4:
                contador_ping += 1
                try:
                    resultado = ping(endereco)

                    if resultado is not None and resultado > 0:
                        resposta = resposta + '#' + str(contador_ping) + '# Ping para ' + endereco + ' - Tempo de resposta: ' + str(round(resultado, 3)) + ' ms\n'
                    else:
                        resposta = resposta + '#' + str(contador_ping) + '# Ping para ' + endereco + ' - Sem resposta\n'
                    tudo_rede.valor_resposta.setText(str(resposta))

                except Exception as e:
                    resposta = resposta + str(e)
                    tudo_rede.valor_resposta.setText(resposta)
                    # return str(e)

        elif tudo_rede.check_traceroute.isChecked() and endereco:
            tudo_rede.valor_resposta.setText("Enviando traceroute para " + endereco)
            self.thread = fazer_traceroute(endereco)
            self.thread.resposta_fazer_traceroute.connect(lambda resp: tudo_rede.valor_resposta.setPlainText(resp))
            self.thread.start()
            tudo_rede.btn_testar.setEnabled(False)
        else:
            tudo_rede.valor_resposta.setText("Algo esta faltando!")
        # tudo_rede.valor_resposta.setText(resposta)

    def pegar_ip_externo(self, tudo_rede):
        self.thread = pegar_ip_externo()
        self.thread.resposta_ip_externo.connect(lambda ip: self.troca_ip_externo(ip, tudo_rede))
        self.thread.start()

    def troca_ip_externo(self, ip, tudo_rede):
        tudo_rede.valor_ip_externo.setText(ip)
        try:
            response = requests.get("http://www.google.com", timeout=5)
            tudo_rede.valor_internet.setText("ok")
        except:
            tudo_rede.valor_internet.setText("sem")
        # print("IP: " + ip)

    def mostrarBackup(self):
        self.backup_widget = QWidget()
        self.backup_ui = Ui_backup()
        self.backup_ui.setupUi(self.backup_widget)
        # apagando a widget anterior
        if self.widget_atual != self.backup_widget and self.widget_atual != None:
            self.layoutMiolo.removeWidget(self.widget_atual)
            self.widget_atual.deleteLater()
        self.layoutMiolo.addWidget(self.backup_widget)
        self.widget_atual = self.backup_widget

        # Alimentando as labels do backup
        tudo_backup = self.backup_ui
        tudo_backup.tab_bkp_btn_fazer.setEnabled(False)
        tudo_backup.tab_bkp_btn_selecionar.clicked.connect(lambda :self.pegaDestino(tudo_backup=tudo_backup))

    def pegaDestino(self, tudo_backup):
        destino = QFileDialog.getExistingDirectory(self, "Selecione a pasta destino")
        if destino:
            tudo_backup.tab_bkp_destino.setText(destino)
            tudo_backup.tab_bkp_btn_fazer.setEnabled(True)
        else:
            if tudo_backup.tab_bkp_destino.text():
                tudo_backup.tab_bkp_btn_fazer.setEnabled(True)
            else:
                tudo_backup.tab_bkp_btn_fazer.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_icon = QIcon("ico/ico.ico")
    app.setWindowIcon(app_icon)
    window = Janela()
    window.show()
    sys.exit(app.exec_())

