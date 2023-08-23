import sys
import socket
import os
import requests
import json
import platform
import time
from ping3 import ping, verbose_ping
import netifaces as ni
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *

# GLOBAL Nomes

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
        resposta = requests.get("https://api.ipify.org?format=json")
        data = resposta.json()
        ip_externo = data["ip"]
        self.resposta_ip_externo.emit(ip_externo)

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

def criaLinha(prefixo, valor, self):

    layout = QHBoxLayout()
    prefixo = QLabel(prefixo, self)
    valor = QLabel(valor, self)

    # font -> negrito
    font_negrito = QFont()
    font_negrito.setBold(True)

    valor.setFont(font_negrito)

    layout.addWidget(prefixo)
    layout.addWidget(valor)


    return layout
    pass

class mioloRede(QWidget):
    def __init__(self):
        super().__init__()

        self.layout_principal = QVBoxLayout()

        # ip da rede

        if (pegar_ip_local() != None):
            layout_rede_local = criaLinha("Rede local: ", "Ok", self)
            layout_rede_local.addStretch()
            layout_rede_local.addLayout(criaLinha("IP local: ", pegar_ip_local(), self))
        else:
            layout_rede_local = criaLinha("Rede local: ", "Sem conexão", self)

        # ip da internet

        self.progresso_externo = QProgressBar()
        self.progresso_externo.setMinimum(0)
        self.progresso_externo.setMaximum(2)

        self.layout_rede_externa = QHBoxLayout()

        prefixo = QLabel("Internet:    ", self)

        self.layout_rede_externa.addWidget(prefixo)
        self.layout_rede_externa.addStretch()
        self.layout_rede_externa.addWidget(self.progresso_externo)

        espaco = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_principal.addLayout(layout_rede_local)
        self.layout_principal.addLayout(self.layout_rede_externa)
        self.layout_principal.addItem(espaco)

        self.pegar_ip_externo()

        self.setLayout(self.layout_principal)
    def pegar_ip_externo(self):
        self.progresso_externo.setValue(1)
        self.thread = pegar_ip_externo()
        self.thread.resposta_ip_externo.connect(self.mostrar_ip_externo)
        self.thread.start()
        
    def remover_widgets_do_layout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if isinstance(item, QWidgetItem):
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
            elif isinstance(item, QLayoutItem):
                sub_layout = item.layout()
                if sub_layout is not None:
                    self.remover_widgets_do_layout(sub_layout)
            layout.removeItem(item)
    def mostrar_ip_externo(self, ip):
        # remover os layouts anteriores e substituir os valores
        self.remover_widgets_do_layout(self.layout_rede_externa)
        self.layout_rede_externa.addLayout(criaLinha("Internet: ", "Ok", self))
        self.layout_rede_externa.addStretch()
        self.layout_rede_externa.addLayout(criaLinha("IP externo:", ip, self))

class mioloInfo(QWidget):
    def __init__(self):
        super().__init__()
        
        # cria layout principal
        layout_principal = QVBoxLayout()

        # nome pc
        layout_pc = criaLinha("Nome do computador: ", NOME_PC, self)

        # nome usuario
        layout_usuario = criaLinha("Nome do usuario: ", NOME_USUARIO, self)

        # nome windows
        nome_completo = NOME_SO + " - " + NOME_SO_VERSAO + " - " + NOME_SO_ARQUITETURA
        layout_so = criaLinha("Versao do SO: ", nome_completo, self)
        
        # espaçamento
        espaco = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # junta tudo no layout principal
        layout_principal.addLayout(layout_pc)
        layout_principal.addLayout(layout_usuario)
        layout_principal.addLayout(layout_so)
        layout_principal.addItem(espaco)

        self.setLayout(layout_principal)


class Janela(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # mioloInfo

        self.miolo_info = mioloInfo()
        self.miolo_rede = mioloRede()
        self.setCentralWidget(self.miolo_info)

        # funções de ação

        def mostrar_info():
            self.setCentralWidget(self.miolo_info)
            self.miolo_info = mioloInfo()
            self.miolo_rede = mioloRede()

        def mostrar_rede():
            self.setCentralWidget(self.miolo_rede)
            self.miolo_info = mioloInfo()
            self.miolo_rede = mioloRede()


        # Ações

        acao_info = QAction(QIcon(), 'Informações', self)
        acao_info.setShortcut('Ctrl+I')
        acao_info.setStatusTip('Informações do computador')
        acao_info.triggered.connect(mostrar_info)

        acao_rede = QAction(QIcon(), 'Rede', self)
        acao_rede.setShortcut('Ctrl+R')
        acao_rede.setStatusTip('Testes de rede')
        acao_rede.triggered.connect(mostrar_rede)

        acao_fazer_backup = QAction(QIcon(), 'Fazer Backup', self)
        acao_fazer_backup.setShortcut('Ctrl+B')
        acao_fazer_backup.setStatusTip('Fazer Backup')
        acao_fazer_backup.triggered.connect(self.close)

        acao_voltar_backup = QAction(QIcon(), 'Voltar Backup', self)
        acao_voltar_backup.setShortcut('Ctrl+K')
        acao_voltar_backup.setStatusTip('Voltar Backup')
        acao_voltar_backup.triggered.connect(self.close)

        acao_solucoes = QAction(QIcon(), 'Soluções', self)
        acao_solucoes.setShortcut('Ctrl+O')
        acao_solucoes.setStatusTip('Lista de Soluções')
        acao_solucoes.triggered.connect(self.close)

        acao_fechar = QAction(QIcon(), 'Fechar', self)
        acao_fechar.setShortcut('Ctrl+F')
        acao_fechar.setStatusTip('Fechar programa')
        acao_fechar.triggered.connect(self.close)


        # statusbar

        self.statusBar()

        # menubar

        menubar = self.menuBar()
        menu_arquivo = menubar.addMenu('&Arquivo')
        menu_arquivo.addAction(acao_info)
        menu_arquivo.addAction(acao_rede)
        menu_arquivo.addAction(acao_fazer_backup)
        menu_arquivo.addAction(acao_voltar_backup)
        menu_arquivo.addAction(acao_solucoes)
        menu_arquivo.addAction(acao_fechar)

        # toolbar

        toolbar_info = self.addToolBar('Informações')
        toolbar_info.addAction(acao_info)
        toolbar_rede = self.addToolBar('Rede')
        toolbar_rede.addAction(acao_rede)
        toolbar_fazer_backup = self.addToolBar('Fazer Backup')
        toolbar_fazer_backup.addAction(acao_fazer_backup)
        toolbar_voltar_backup = self.addToolBar('Voltar Backup')
        toolbar_voltar_backup.addAction(acao_voltar_backup)
        toolbar_solucoes = self.addToolBar('Soluções')
        toolbar_solucoes.addAction(acao_solucoes)
        toolbar_fechar = self.addToolBar('Fechar')
        toolbar_fechar.addAction(acao_fechar)

        # montagem da janela

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Janela()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()