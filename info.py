# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.resize(591, 300)
        self.txt_nome = QtWidgets.QLabel(Info)
        self.txt_nome.setGeometry(QtCore.QRect(30, 20, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy)
        self.txt_nome.setObjectName("txt_nome")
        self.valor_nome = QtWidgets.QLabel(Info)
        self.valor_nome.setGeometry(QtCore.QRect(200, 20, 371, 17))
        self.valor_nome.setWordWrap(False)
        self.valor_nome.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.valor_nome.setObjectName("valor_nome")
        self.txt_usuario = QtWidgets.QLabel(Info)
        self.txt_usuario.setGeometry(QtCore.QRect(30, 40, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy)
        self.txt_usuario.setObjectName("txt_usuario")
        self.valor_usuario = QtWidgets.QLabel(Info)
        self.valor_usuario.setGeometry(QtCore.QRect(200, 40, 371, 17))
        self.valor_usuario.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.valor_usuario.setObjectName("valor_usuario")
        self.txt_sistema = QtWidgets.QLabel(Info)
        self.txt_sistema.setGeometry(QtCore.QRect(30, 60, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_sistema.sizePolicy().hasHeightForWidth())
        self.txt_sistema.setSizePolicy(sizePolicy)
        self.txt_sistema.setObjectName("txt_sistema")
        self.valor_sistema = QtWidgets.QLabel(Info)
        self.valor_sistema.setGeometry(QtCore.QRect(200, 60, 371, 17))
        self.valor_sistema.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.valor_sistema.setObjectName("valor_sistema")
        self.txt_ram = QtWidgets.QLabel(Info)
        self.txt_ram.setGeometry(QtCore.QRect(30, 80, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_ram.sizePolicy().hasHeightForWidth())
        self.txt_ram.setSizePolicy(sizePolicy)
        self.txt_ram.setObjectName("txt_ram")
        self.txt_hd = QtWidgets.QLabel(Info)
        self.txt_hd.setGeometry(QtCore.QRect(30, 100, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_hd.sizePolicy().hasHeightForWidth())
        self.txt_hd.setSizePolicy(sizePolicy)
        self.txt_hd.setObjectName("txt_hd")
        self.valor_ram = QtWidgets.QLabel(Info)
        self.valor_ram.setGeometry(QtCore.QRect(200, 80, 371, 17))
        self.valor_ram.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.valor_ram.setObjectName("valor_ram")
        self.valor_hd = QtWidgets.QLabel(Info)
        self.valor_hd.setGeometry(QtCore.QRect(200, 100, 371, 51))
        self.valor_hd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.valor_hd.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.valor_hd.setObjectName("valor_hd")

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Form"))
        self.txt_nome.setText(_translate("Info", "Nome do computador:"))
        self.valor_nome.setText(_translate("Info", "NOME"))
        self.txt_usuario.setText(_translate("Info", "Nome do usuario:"))
        self.valor_usuario.setText(_translate("Info", "USER"))
        self.txt_sistema.setText(_translate("Info", "Sistema operacional:"))
        self.valor_sistema.setText(_translate("Info", "WINDOWS"))
        self.txt_ram.setText(_translate("Info", "RAM:"))
        self.txt_hd.setText(_translate("Info", "HD:"))
        self.valor_ram.setText(_translate("Info", "RAM"))
        self.valor_hd.setText(_translate("Info", "HD"))
