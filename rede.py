# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rede.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rede(object):
    def setupUi(self, Rede):
        Rede.setObjectName("Rede")
        Rede.resize(608, 359)
        self.valor_local = QtWidgets.QLabel(Rede)
        self.valor_local.setGeometry(QtCore.QRect(200, 20, 61, 17))
        self.valor_local.setWordWrap(False)
        self.valor_local.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.valor_local.setObjectName("valor_local")
        self.txt_local = QtWidgets.QLabel(Rede)
        self.txt_local.setGeometry(QtCore.QRect(30, 20, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_local.sizePolicy().hasHeightForWidth())
        self.txt_local.setSizePolicy(sizePolicy)
        self.txt_local.setObjectName("txt_local")
        self.valor_internet = QtWidgets.QLabel(Rede)
        self.valor_internet.setGeometry(QtCore.QRect(200, 40, 61, 17))
        self.valor_internet.setWordWrap(False)
        self.valor_internet.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.valor_internet.setObjectName("valor_internet")
        self.txt_internet = QtWidgets.QLabel(Rede)
        self.txt_internet.setGeometry(QtCore.QRect(30, 40, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_internet.sizePolicy().hasHeightForWidth())
        self.txt_internet.setSizePolicy(sizePolicy)
        self.txt_internet.setObjectName("txt_internet")
        self.txt_ip_local = QtWidgets.QLabel(Rede)
        self.txt_ip_local.setGeometry(QtCore.QRect(250, 20, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_ip_local.sizePolicy().hasHeightForWidth())
        self.txt_ip_local.setSizePolicy(sizePolicy)
        self.txt_ip_local.setObjectName("txt_ip_local")
        self.txt_ip_externo = QtWidgets.QLabel(Rede)
        self.txt_ip_externo.setGeometry(QtCore.QRect(250, 40, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_ip_externo.sizePolicy().hasHeightForWidth())
        self.txt_ip_externo.setSizePolicy(sizePolicy)
        self.txt_ip_externo.setObjectName("txt_ip_externo")
        self.valor_ip_local = QtWidgets.QLabel(Rede)
        self.valor_ip_local.setGeometry(QtCore.QRect(350, 20, 231, 17))
        self.valor_ip_local.setWordWrap(False)
        self.valor_ip_local.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.valor_ip_local.setObjectName("valor_ip_local")
        self.valor_ip_externo = QtWidgets.QLabel(Rede)
        self.valor_ip_externo.setGeometry(QtCore.QRect(350, 40, 231, 17))
        self.valor_ip_externo.setWordWrap(False)
        self.valor_ip_externo.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.valor_ip_externo.setObjectName("valor_ip_externo")
        self.valor_endereco = QtWidgets.QLineEdit(Rede)
        self.valor_endereco.setGeometry(QtCore.QRect(10, 120, 581, 25))
        self.valor_endereco.setObjectName("valor_endereco")
        self.check_ping = QtWidgets.QRadioButton(Rede)
        self.check_ping.setGeometry(QtCore.QRect(10, 150, 112, 23))
        self.check_ping.setChecked(True)
        self.check_ping.setObjectName("check_ping")
        self.check_traceroute = QtWidgets.QRadioButton(Rede)
        self.check_traceroute.setGeometry(QtCore.QRect(100, 150, 112, 23))
        self.check_traceroute.setChecked(False)
        self.check_traceroute.setObjectName("check_traceroute")
        self.btn_testar = QtWidgets.QPushButton(Rede)
        self.btn_testar.setGeometry(QtCore.QRect(230, 150, 89, 25))
        self.btn_testar.setObjectName("btn_testar")
        self.valor_resposta = QtWidgets.QTextEdit(Rede)
        self.valor_resposta.setGeometry(QtCore.QRect(10, 180, 581, 161))
        self.valor_resposta.setReadOnly(True)
        self.valor_resposta.setObjectName("valor_resposta")

        self.retranslateUi(Rede)
        QtCore.QMetaObject.connectSlotsByName(Rede)

    def retranslateUi(self, Rede):
        _translate = QtCore.QCoreApplication.translate
        Rede.setWindowTitle(_translate("Rede", "Form"))
        self.valor_local.setText(_translate("Rede", "X"))
        self.txt_local.setText(_translate("Rede", "Rede Local:"))
        self.valor_internet.setText(_translate("Rede", "X"))
        self.txt_internet.setText(_translate("Rede", "Internet:"))
        self.txt_ip_local.setText(_translate("Rede", "IP Local:"))
        self.txt_ip_externo.setText(_translate("Rede", "IP Local:"))
        self.valor_ip_local.setText(_translate("Rede", "X"))
        self.valor_ip_externo.setText(_translate("Rede", "buscando..."))
        self.valor_endereco.setText(_translate("Rede", "www.google.com.br"))
        self.check_ping.setText(_translate("Rede", "Ping"))
        self.check_traceroute.setText(_translate("Rede", "Tracerout"))
        self.btn_testar.setText(_translate("Rede", "Testar"))
