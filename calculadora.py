# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(442, 570)
        MainWindow.setStyleSheet("background-color: rgb(24, 24, 24);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 401, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("7"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("QPushButton{\n"
"    background-color: rgb(111,111,111);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 4, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("4"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(111,111,111);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 3, 0, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("3"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(111,111,111);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("6"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton{\n"
"    background-color: rgb(111,111,111);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 3, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("8"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("QPushButton{\n"
"    background-color: rgb(111,111,111);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 4, 1, 1, 1)
        self.btn_subtracao = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("-"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_subtracao.sizePolicy().hasHeightForWidth())
        self.btn_subtracao.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_subtracao.setFont(font)
        self.btn_subtracao.setStyleSheet("QPushButton{\n"
"    background-color: rgb(69,69,69);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_subtracao.setObjectName("btn_subtracao")
        self.gridLayout.addWidget(self.btn_subtracao, 2, 3, 1, 1)
        self.btn_divisao = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("/"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_divisao.sizePolicy().hasHeightForWidth())
        self.btn_divisao.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_divisao.setFont(font)
        self.btn_divisao.setStyleSheet("QPushButton{\n"
"    background-color: rgb(69,69,69);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_divisao.setObjectName("btn_divisao")
        self.gridLayout.addWidget(self.btn_divisao, 4, 3, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("2"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(111,111,111);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("1"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("QPushButton{\n"
"    background-color: rgb(111,111,111);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)
        self.btn_multiplicacao = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("*"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_multiplicacao.sizePolicy().hasHeightForWidth())
        self.btn_multiplicacao.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_multiplicacao.setFont(font)
        self.btn_multiplicacao.setStyleSheet("QPushButton{\n"
"    background-color: rgb(69,69,69);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_multiplicacao.setObjectName("btn_multiplicacao")
        self.gridLayout.addWidget(self.btn_multiplicacao, 3, 3, 1, 1)
        self.btn_resultado = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.calcular())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_resultado.sizePolicy().hasHeightForWidth())
        self.btn_resultado.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_resultado.setFont(font)
        self.btn_resultado.setStyleSheet("QPushButton{\n"
"    background-color: rgb(69,69,69);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_resultado.setObjectName("btn_resultado")
        self.gridLayout.addWidget(self.btn_resultado, 5, 3, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("5"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton{\n"
"    background-color: rgb(111,111,111);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 3, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("9"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("QPushButton{\n"
"    background-color: rgb(111,111,111);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 4, 2, 1, 1)
        self.btn_ponto = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.decimal())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_ponto.sizePolicy().hasHeightForWidth())
        self.btn_ponto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_ponto.setFont(font)
        self.btn_ponto.setStyleSheet("QPushButton{\n"
"    background-color: rgb(69,69,69);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_ponto.setObjectName("btn_ponto")
        self.gridLayout.addWidget(self.btn_ponto, 5, 2, 1, 1)
        self.btn_apagar = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.apagar())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_apagar.sizePolicy().hasHeightForWidth())
        self.btn_apagar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_apagar.setFont(font)
        self.btn_apagar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(69,69,69);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_apagar.setObjectName("btn_apagar")
        self.gridLayout.addWidget(self.btn_apagar, 1, 2, 1, 1)
        self.btn_somar = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("+"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_somar.sizePolicy().hasHeightForWidth())
        self.btn_somar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_somar.setFont(font)
        self.btn_somar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(69,69,69);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_somar.setObjectName("btn_somar")
        self.gridLayout.addWidget(self.btn_somar, 1, 3, 1, 1)
        self.btn_limpar = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("C"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_limpar.sizePolicy().hasHeightForWidth())
        self.btn_limpar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_limpar.setFont(font)
        self.btn_limpar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(69,69,69);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_limpar.setObjectName("btn_limpar")
        self.gridLayout.addWidget(self.btn_limpar, 1, 0, 1, 2)
        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.pressionar("0"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("QPushButton{\n"
"    background-color: rgb(111,111,111);\n"
"    border-radius: 30px;\n"
"    color:rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(61,61,61);\n"
"    border-radius: 30px;\n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(21)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calcular(self):
        #Pega o que est?? na tela
        tela = self.label.text()
        try:
                # Faz o calculo
                resposta = eval(tela)
                # Sa??da do calculo
                self.label.setText(str(resposta))
        except:
                # Sa??da do erro
                self.label.setText("ERRO 404")

    def apagar(self):
        # Pega o que est?? na tela
        tela = self.label.text()
        # Apaga ??ltima linha do que est?? na tela
        tela = tela[:-1]
        self.label.setText(tela)
        # Ao apagar a ??ltima linha retorna um 0
        if self.label.text() == "":
                self.label.setText("0")

    def decimal(self):
        # Pega o que est?? na tela
        tela = self.label.text()
        # Verifica o ??ltimo d??gito
        tela[-1]
        # Se o ??ltimo d??gito tiver um .
        if tela[-1] == ".":
            # N??o faz nada
                pass
        # Se n??o tiver
        else:
            # Insere um ponto
                self.label.setText(f'{tela}.')

    def pressionar(self, pressionado):
        # Se Limpar for pressionado
        if pressionado == "C":
            # A tela ?? resetada
                self.label.setText("0")
        # Se n??o for digitado
        else:
            # Mas se o texto estiver zerado
                if self.label.text() == "0":
                    # Apenas limpa o texto para inserir outro zero
                        self.label.setText("")
                # Caso contr??rio, insere o valor solicitado pelo bot??o
                self.label.setText(f'{self.label.text()}{pressionado}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_subtracao.setText(_translate("MainWindow", "-"))
        self.btn_divisao.setText(_translate("MainWindow", "/"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_multiplicacao.setText(_translate("MainWindow", "X"))
        self.btn_resultado.setText(_translate("MainWindow", "="))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_ponto.setText(_translate("MainWindow", "."))
        self.btn_apagar.setText(_translate("MainWindow", "Apagar"))
        self.btn_somar.setText(_translate("MainWindow", "+"))
        self.btn_limpar.setText(_translate("MainWindow", "Limpar"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
