# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log-sign.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 50, 681, 431))
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.log_password_label = QLabel(self.tab)
        self.log_password_label.setObjectName(u"log_password_label")
        self.log_password_label.setGeometry(QRect(80, 180, 141, 21))
        font1 = QFont()
        font1.setPointSize(14)
        self.log_password_label.setFont(font1)
        self.login_pushButton = QPushButton(self.tab)
        self.login_pushButton.setObjectName(u"login_pushButton")
        self.login_pushButton.setGeometry(QRect(420, 330, 101, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.login_pushButton.setFont(font2)
        self.log_email_lineEdit = QLineEdit(self.tab)
        self.log_email_lineEdit.setObjectName(u"log_email_lineEdit")
        self.log_email_lineEdit.setGeometry(QRect(290, 50, 241, 41))
#if QT_CONFIG(statustip)
        self.log_email_lineEdit.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.log_email_label = QLabel(self.tab)
        self.log_email_label.setObjectName(u"log_email_label")
        self.log_email_label.setGeometry(QRect(80, 60, 131, 21))
        self.log_email_label.setFont(font1)
        self.log_password_lineEdit = QLineEdit(self.tab)
        self.log_password_lineEdit.setObjectName(u"log_password_lineEdit")
        self.log_password_lineEdit.setGeometry(QRect(290, 160, 241, 41))
        self.log_password_lineEdit.setToolTipDuration(-1)
        self.log_password_lineEdit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.log_password_lineEdit.setMaxLength(8)
        self.log_password_lineEdit.setEchoMode(QLineEdit.Password)
        self.log_result_label = QLabel(self.tab)
        self.log_result_label.setObjectName(u"log_result_label")
        self.log_result_label.setGeometry(QRect(80, 260, 451, 21))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.sign_password_label = QLabel(self.tab_2)
        self.sign_password_label.setObjectName(u"sign_password_label")
        self.sign_password_label.setGeometry(QRect(80, 240, 141, 21))
        self.sign_password_label.setFont(font1)
        self.signup_pushButton = QPushButton(self.tab_2)
        self.signup_pushButton.setObjectName(u"signup_pushButton")
        self.signup_pushButton.setGeometry(QRect(450, 340, 111, 41))
        self.signup_pushButton.setFont(font2)
        self.sign_name_lineEdit = QLineEdit(self.tab_2)
        self.sign_name_lineEdit.setObjectName(u"sign_name_lineEdit")
        self.sign_name_lineEdit.setGeometry(QRect(330, 20, 231, 41))
        self.sign_name_label = QLabel(self.tab_2)
        self.sign_name_label.setObjectName(u"sign_name_label")
        self.sign_name_label.setGeometry(QRect(80, 40, 121, 21))
        self.sign_name_label.setFont(font1)
        self.sign_password_lineEdit = QLineEdit(self.tab_2)
        self.sign_password_lineEdit.setObjectName(u"sign_password_lineEdit")
        self.sign_password_lineEdit.setGeometry(QRect(330, 230, 231, 41))
        self.sign_surname_label = QLabel(self.tab_2)
        self.sign_surname_label.setObjectName(u"sign_surname_label")
        self.sign_surname_label.setGeometry(QRect(80, 110, 121, 21))
        self.sign_surname_label.setFont(font1)
        self.sign_email_label = QLabel(self.tab_2)
        self.sign_email_label.setObjectName(u"sign_email_label")
        self.sign_email_label.setGeometry(QRect(80, 180, 121, 21))
        self.sign_email_label.setFont(font1)
        self.sign_email_lineEdit = QLineEdit(self.tab_2)
        self.sign_email_lineEdit.setObjectName(u"sign_email_lineEdit")
        self.sign_email_lineEdit.setGeometry(QRect(330, 160, 231, 41))
        self.sign_surname_lineEdit = QLineEdit(self.tab_2)
        self.sign_surname_lineEdit.setObjectName(u"sign_surname_lineEdit")
        self.sign_surname_lineEdit.setGeometry(QRect(330, 90, 231, 41))
        self.sign_result_label = QLabel(self.tab_2)
        self.sign_result_label.setObjectName(u"sign_result_label")
        self.sign_result_label.setGeometry(QRect(80, 300, 481, 31))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(statustip)
        self.tabWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.log_password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_pushButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.log_email_label.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.log_result_label.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Log In", None))
        self.sign_password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.signup_pushButton.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.sign_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.sign_surname_label.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.sign_email_label.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.sign_result_label.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Sign Up", None))
    # retranslateUi

