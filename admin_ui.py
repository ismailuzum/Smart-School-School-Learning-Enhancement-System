# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1143, 803)
        self.menu11 = QAction(MainWindow)
        self.menu11.setObjectName(u"menu11")
        self.menu12 = QAction(MainWindow)
        self.menu12.setObjectName(u"menu12")
        self.menu21 = QAction(MainWindow)
        self.menu21.setObjectName(u"menu21")
        self.menu22 = QAction(MainWindow)
        self.menu22.setObjectName(u"menu22")
        self.menu31 = QAction(MainWindow)
        self.menu31.setObjectName(u"menu31")
        self.menu41 = QAction(MainWindow)
        self.menu41.setObjectName(u"menu41")
        self.menu42 = QAction(MainWindow)
        self.menu42.setObjectName(u"menu42")
        self.menu32 = QAction(MainWindow)
        self.menu32.setObjectName(u"menu32")
        self.menu33 = QAction(MainWindow)
        self.menu33.setObjectName(u"menu33")
        self.menu51 = QAction(MainWindow)
        self.menu51.setObjectName(u"menu51")
        self.menu61_a = QAction(MainWindow)
        self.menu61_a.setObjectName(u"menu61_a")
        self.menu71 = QAction(MainWindow)
        self.menu71.setObjectName(u"menu71")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 1101, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(253, 189, 16);\n"
"background-color: rgb(40, 41, 44);")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 50, 1141, 741))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"background-color: rgb(40, 41, 44);")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(460, 290, 231, 20))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setUnderline(True)
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: rgb(255, 191, 16);")
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(140, 170, 981, 41))
        font3 = QFont()
        font3.setPointSize(26)
        font3.setBold(True)
        font3.setStrikeOut(False)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: rgb(253, 189, 16);\n"
"background-color: rgb(40, 41, 44);")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 10, 251, 21))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(255, 191, 16);")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 40, 161, 20))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 191, 16);")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 80, 111, 20))
        font5 = QFont()
        font5.setPointSize(11)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tb11 = QLineEdit(self.tab)
        self.tb11.setObjectName(u"tb11")
        self.tb11.setGeometry(QRect(140, 70, 271, 31))
        self.tb11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 130, 111, 20))
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tb12 = QLineEdit(self.tab)
        self.tb12.setObjectName(u"tb12")
        self.tb12.setGeometry(QRect(140, 120, 271, 31))
        self.tb12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 180, 111, 20))
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tb13 = QLineEdit(self.tab)
        self.tb13.setObjectName(u"tb13")
        self.tb13.setGeometry(QRect(140, 170, 271, 31))
        self.tb13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 230, 111, 20))
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tb14 = QLineEdit(self.tab)
        self.tb14.setObjectName(u"tb14")
        self.tb14.setGeometry(QRect(140, 220, 271, 31))
        self.tb14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 280, 111, 20))
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 330, 111, 20))
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tb15 = QLineEdit(self.tab)
        self.tb15.setObjectName(u"tb15")
        self.tb15.setGeometry(QRect(140, 320, 271, 31))
        self.tb15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cb11 = QComboBox(self.tab)
        self.cb11.addItem("")
        self.cb11.addItem("")
        self.cb11.setObjectName(u"cb11")
        self.cb11.setGeometry(QRect(140, 270, 271, 31))
        self.cb11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.cb11.setMaxVisibleItems(8)
        self.cb11.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.tb16 = QLineEdit(self.tab)
        self.tb16.setObjectName(u"tb16")
        self.tb16.setGeometry(QRect(140, 370, 271, 31))
        self.tb16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 380, 111, 20))
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.b5 = QPushButton(self.tab)
        self.b5.setObjectName(u"b5")
        self.b5.setGeometry(QRect(140, 420, 271, 41))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.b5.setFont(font6)
        self.b5.setStyleSheet(u"background-color: rgb(255, 191, 16);")
        self.tb17 = QLineEdit(self.tab)
        self.tb17.setObjectName(u"tb17")
        self.tb17.setGeometry(QRect(430, 370, 211, 31))
        font7 = QFont()
        font7.setPointSize(10)
        self.tb17.setFont(font7)
        self.tb17.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tb17.setEchoMode(QLineEdit.Password)
        self.tb17.setClearButtonEnabled(True)
        self.label_15 = QLabel(self.tab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(490, 340, 111, 20))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"color: rgb(255, 191, 16);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 30, 291, 21))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(255, 191, 16);")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 100, 201, 20))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(255, 191, 16);")
        self.label_24 = QLabel(self.tab_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 380, 111, 20))
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25 = QLabel(self.tab_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 140, 111, 20))
        self.label_25.setFont(font5)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_26 = QLabel(self.tab_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 220, 111, 20))
        self.label_26.setFont(font5)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_27 = QLabel(self.tab_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 300, 111, 20))
        self.label_27.setFont(font5)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tb22 = QLineEdit(self.tab_2)
        self.tb22.setObjectName(u"tb22")
        self.tb22.setGeometry(QRect(140, 170, 271, 31))
        self.tb22.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_28 = QLabel(self.tab_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 260, 111, 20))
        self.label_28.setFont(font5)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tb24 = QLineEdit(self.tab_2)
        self.tb24.setObjectName(u"tb24")
        self.tb24.setGeometry(QRect(140, 250, 271, 31))
        self.tb24.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cb22 = QComboBox(self.tab_2)
        self.cb22.addItem("")
        self.cb22.addItem("")
        self.cb22.setObjectName(u"cb22")
        self.cb22.setGeometry(QRect(140, 290, 271, 31))
        self.cb22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.cb22.setMaxVisibleItems(8)
        self.cb22.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.tb25 = QLineEdit(self.tab_2)
        self.tb25.setObjectName(u"tb25")
        self.tb25.setGeometry(QRect(140, 330, 271, 31))
        self.tb25.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_29 = QLabel(self.tab_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 340, 111, 20))
        self.label_29.setFont(font5)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tb26 = QLineEdit(self.tab_2)
        self.tb26.setObjectName(u"tb26")
        self.tb26.setGeometry(QRect(140, 370, 271, 31))
        self.tb26.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_30 = QLabel(self.tab_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(20, 180, 111, 20))
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.b6 = QPushButton(self.tab_2)
        self.b6.setObjectName(u"b6")
        self.b6.setGeometry(QRect(20, 420, 211, 41))
        self.b6.setFont(font6)
        self.b6.setStyleSheet(u"background-color: rgb(255, 191, 16);")
        self.tb23 = QLineEdit(self.tab_2)
        self.tb23.setObjectName(u"tb23")
        self.tb23.setGeometry(QRect(140, 210, 271, 31))
        self.tb23.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cb21 = QComboBox(self.tab_2)
        self.cb21.setObjectName(u"cb21")
        self.cb21.setGeometry(QRect(140, 90, 271, 31))
        self.cb21.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.b7 = QPushButton(self.tab_2)
        self.b7.setObjectName(u"b7")
        self.b7.setGeometry(QRect(240, 420, 221, 41))
        self.b7.setFont(font6)
        self.b7.setStyleSheet(u"background-color: rgb(255, 85, 0);")
        self.tb27 = QLineEdit(self.tab_2)
        self.tb27.setObjectName(u"tb27")
        self.tb27.setGeometry(QRect(430, 370, 211, 31))
        self.tb27.setFont(font7)
        self.tb27.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tb27.setEchoMode(QLineEdit.Password)
        self.tb27.setClearButtonEnabled(True)
        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(490, 340, 161, 20))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color: rgb(255, 191, 16);")
        self.tb21 = QLineEdit(self.tab_2)
        self.tb21.setObjectName(u"tb21")
        self.tb21.setGeometry(QRect(140, 130, 271, 31))
        self.tb21.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.sendButton1 = QPushButton(self.tab_4)
        self.sendButton1.setObjectName(u"sendButton1")
        self.sendButton1.setGeometry(QRect(800, 610, 201, 51))
        self.sendButton1.setFont(font6)
        self.sendButton1.setStyleSheet(u"background-color: rgb(255, 191, 16);")
        self.listView_4_a = QListView(self.tab_4)
        self.listView_4_a.setObjectName(u"listView_4_a")
        self.listView_4_a.setGeometry(QRect(70, 160, 371, 421))
        self.listView_4_a.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.list_view_3_a = QListView(self.tab_4)
        self.list_view_3_a.setObjectName(u"list_view_3_a")
        self.list_view_3_a.setGeometry(QRect(540, 90, 461, 411))
        self.list_view_3_a.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.LineEdit_3_a = QLineEdit(self.tab_4)
        self.LineEdit_3_a.setObjectName(u"LineEdit_3_a")
        self.LineEdit_3_a.setGeometry(QRect(540, 510, 461, 71))
        font8 = QFont()
        font8.setBold(True)
        font8.setItalic(True)
        self.LineEdit_3_a.setFont(font8)
        self.LineEdit_3_a.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_105 = QLabel(self.tab_4)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(140, 100, 281, 21))
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        self.label_105.setFont(font9)
        self.label_105.setStyleSheet(u"color: rgb(255, 191, 16);")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1143, 30))
        self.menubar.setStyleSheet(u"background-color: rgb(16, 16, 16);\n"
"color: rgb(255, 191, 16);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.menuTeacher = QMenu(self.menubar)
        self.menuTeacher.setObjectName(u"menuTeacher")
        self.menuMessage_Box = QMenu(self.menubar)
        self.menuMessage_Box.setObjectName(u"menuMessage_Box")
        self.menuExit = QMenu(self.menubar)
        self.menuExit.setObjectName(u"menuExit")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuTeacher.menuAction())
        self.menubar.addAction(self.menuMessage_Box.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menuTeacher.addAction(self.menu11)
        self.menuTeacher.addAction(self.menu12)
        self.menuMessage_Box.addAction(self.menu61_a)
        self.menuExit.addAction(self.menu71)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)
        self.cb11.setCurrentIndex(-1)
        self.cb22.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu11.setText(QCoreApplication.translate("MainWindow", u"Add Teacher", None))
        self.menu12.setText(QCoreApplication.translate("MainWindow", u"Edit Teacher", None))
        self.menu21.setText(QCoreApplication.translate("MainWindow", u"Add student", None))
        self.menu22.setText(QCoreApplication.translate("MainWindow", u"Edit student", None))
        self.menu31.setText(QCoreApplication.translate("MainWindow", u"Add/Edit Courses", None))
        self.menu41.setText(QCoreApplication.translate("MainWindow", u"Add/Edit Meeting", None))
        self.menu42.setText(QCoreApplication.translate("MainWindow", u"Add/Edit Meeting Attandance", None))
        self.menu32.setText(QCoreApplication.translate("MainWindow", u"Add/Edit Course Schedule", None))
        self.menu33.setText(QCoreApplication.translate("MainWindow", u"Add/Edit Course Attandance", None))
        self.menu51.setText(QCoreApplication.translate("MainWindow", u"Add/Edit To Do List", None))
        self.menu61_a.setText(QCoreApplication.translate("MainWindow", u"Add/Edit Message", None))
        self.menu71.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"   \ue736 SMART SCHOOL > School-Learning-Enhancement-System \ue736", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"You login as admin !!!", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"   \ue736 WELCOME TO SMART SCHOOL \ue736", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add New Teacher", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enter Teacher Details", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Teacher ID", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.cb11.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.cb11.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.cb11.setProperty("placeholderText", QCoreApplication.translate("MainWindow", u"Add/Select Teacher", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.b5.setText(QCoreApplication.translate("MainWindow", u"Save Teacher Details", None))
        self.tb17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set password for new teacher", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Set Password", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Add Teacher", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Edit or Delete Teacher", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Select Teacher", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Teacher ID", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.cb22.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.cb22.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.cb22.setProperty("placeholderText", QCoreApplication.translate("MainWindow", u"Add/Select Teacher", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.b6.setText(QCoreApplication.translate("MainWindow", u"Save Teacher Details", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"Delete Teacher Details", None))
        self.tb27.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set password", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Set Password", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Edit Teacher", None))
        self.sendButton1.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.LineEdit_3_a.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please Type Here", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Select  Person", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Message_box", None))
        self.menuTeacher.setTitle(QCoreApplication.translate("MainWindow", u"Teachers", None))
        self.menuMessage_Box.setTitle(QCoreApplication.translate("MainWindow", u"Message Box", None))
        self.menuExit.setTitle(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

