# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\doron\Documents\py projects\Image_editor\product_editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(274, 820)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 271, 721))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 241, 161))
        self.groupBox.setObjectName("groupBox")
        self.Version = QtWidgets.QLabel(self.groupBox)
        self.Version.setGeometry(QtCore.QRect(10, 20, 171, 16))
        self.Version.setObjectName("Version")
        self.Date = QtWidgets.QLabel(self.groupBox)
        self.Date.setGeometry(QtCore.QRect(10, 40, 171, 16))
        self.Date.setObjectName("Date")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 120, 111, 17))
        self.radioButton.setObjectName("radioButton")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_7.setObjectName("label_7")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(90, 60, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_8.setObjectName("label_8")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(90, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 241, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_6.setObjectName("label_6")
        self.Image_width = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.Image_width.setGeometry(QtCore.QRect(90, 60, 91, 21))
        self.Image_width.setObjectName("Image_width")
        self.Image_height = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.Image_height.setGeometry(QtCore.QRect(90, 90, 91, 21))
        self.Image_height.setObjectName("Image_height")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_9.setObjectName("label_9")
        self.Image_offset = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.Image_offset.setGeometry(QtCore.QRect(90, 120, 91, 21))
        self.Image_offset.setObjectName("Image_offset")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_10.setObjectName("label_10")
        self.Image_type = QtWidgets.QComboBox(self.groupBox_2)
        self.Image_type.setGeometry(QtCore.QRect(90, 20, 91, 20))
        self.Image_type.setObjectName("Image_type")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 92, 20))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 370, 241, 321))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 280, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(10, 280, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 150, 221, 121))
        self.listWidget.setObjectName("listWidget")
        self.training_p = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.training_p.setGeometry(QtCore.QRect(140, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.training_p.setFont(font)
        self.training_p.setObjectName("training_p")
        self.validation_p = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.validation_p.setGeometry(QtCore.QRect(140, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.validation_p.setFont(font)
        self.validation_p.setObjectName("validation_p")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label_12.setObjectName("label_12")
        self.max_epochs = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.max_epochs.setGeometry(QtCore.QRect(140, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.max_epochs.setFont(font)
        self.max_epochs.setObjectName("max_epochs")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 80, 131, 16))
        self.label_13.setObjectName("label_13")
        self.debug = QtWidgets.QRadioButton(self.groupBox_3)
        self.debug.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.debug.setObjectName("debug")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(13, 13, 191, 22))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 80, 271, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 92, 20))
        self.label_5.setObjectName("label_5")
        self.Image_type_engine = QtWidgets.QComboBox(self.groupBox_4)
        self.Image_type_engine.setGeometry(QtCore.QRect(120, 20, 101, 20))
        self.Image_type_engine.setObjectName("Image_type_engine")
        self.Image_type_engine.addItem("")
        self.Image_type_engine.addItem("")
        self.Image_type_engine.addItem("")
        self.Image_type_engine.addItem("")
        self.Image_type_engine.addItem("")
        self.Image_type_engine.addItem("")
        self.Image_type_engine.addItem("")
        self.Image_type_engine.addItem("")
        self.Image_type_engine.addItem("")
        self.translate_shift = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.translate_shift.setGeometry(QtCore.QRect(120, 170, 101, 20))
        self.translate_shift.setObjectName("translate_shift")
        self.Image_resize = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.Image_resize.setGeometry(QtCore.QRect(120, 80, 101, 21))
        self.Image_resize.setObjectName("Image_resize")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_14.setObjectName("label_14")
        self.roi_size = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.roi_size.setGeometry(QtCore.QRect(120, 140, 101, 21))
        self.roi_size.setObjectName("roi_size")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(10, 170, 71, 15))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(10, 140, 71, 16))
        self.label_16.setObjectName("label_16")
        self.Image_convert = QtWidgets.QComboBox(self.groupBox_4)
        self.Image_convert.setGeometry(QtCore.QRect(120, 50, 101, 20))
        self.Image_convert.setObjectName("Image_convert")
        self.Image_convert.addItem("")
        self.Image_convert.addItem("")
        self.Image_convert.addItem("")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(10, 50, 92, 20))
        self.label_17.setObjectName("label_17")
        self.roi_resize = QtWidgets.QRadioButton(self.groupBox_4)
        self.roi_resize.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.roi_resize.setObjectName("roi_resize")
        self.image_smooth = QtWidgets.QRadioButton(self.groupBox_4)
        self.image_smooth.setGeometry(QtCore.QRect(10, 200, 111, 17))
        self.image_smooth.setObjectName("image_smooth")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(20, 40, 92, 20))
        self.label_21.setObjectName("label_21")
        self.eng_num = QtWidgets.QSpinBox(self.tab_2)
        self.eng_num.setGeometry(QtCore.QRect(140, 40, 61, 22))
        self.eng_num.setObjectName("eng_num")
        self.comboBox_Engine = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_Engine.setGeometry(QtCore.QRect(110, 10, 91, 20))
        self.comboBox_Engine.setObjectName("comboBox_Engine")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(12, 10, 92, 20))
        self.label_3.setObjectName("label_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 310, 271, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        self.label_20.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.label_20.setObjectName("label_20")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox.setGeometry(QtCore.QRect(161, 20, 61, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_2.setGeometry(QtCore.QRect(161, 50, 61, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(160, 80, 62, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.model_trial = QtWidgets.QComboBox(self.tab_3)
        self.model_trial.setGeometry(QtCore.QRect(140, 10, 91, 20))
        self.model_trial.setObjectName("model_trial")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(20, 10, 92, 20))
        self.label_23.setObjectName("label_23")
        self.label_31 = QtWidgets.QLabel(self.tab_3)
        self.label_31.setGeometry(QtCore.QRect(20, 150, 92, 20))
        self.label_31.setObjectName("label_31")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 40, 271, 101))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_22 = QtWidgets.QLabel(self.groupBox_6)
        self.label_22.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_22.setObjectName("label_22")
        self.engine_type = QtWidgets.QComboBox(self.groupBox_6)
        self.engine_type.setGeometry(QtCore.QRect(130, 20, 91, 20))
        self.engine_type.setObjectName("engine_type")
        self.engine_type.addItem("")
        self.engine_type.addItem("")
        self.label_24 = QtWidgets.QLabel(self.groupBox_6)
        self.label_24.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_24.setObjectName("label_24")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_3.setGeometry(QtCore.QRect(161, 50, 61, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.active_trial = QtWidgets.QRadioButton(self.groupBox_6)
        self.active_trial.setGeometry(QtCore.QRect(10, 80, 111, 17))
        self.active_trial.setObjectName("active_trial")
        self.sub_engine = QtWidgets.QComboBox(self.tab_3)
        self.sub_engine.setGeometry(QtCore.QRect(140, 150, 91, 20))
        self.sub_engine.setObjectName("sub_engine")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 190, 271, 201))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_25 = QtWidgets.QLabel(self.groupBox_7)
        self.label_25.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_25.setObjectName("label_25")
        self.architecture = QtWidgets.QComboBox(self.groupBox_7)
        self.architecture.setGeometry(QtCore.QRect(130, 20, 91, 20))
        self.architecture.setObjectName("architecture")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.architecture.addItem("")
        self.label_26 = QtWidgets.QLabel(self.groupBox_7)
        self.label_26.setGeometry(QtCore.QRect(10, 50, 92, 20))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_7)
        self.label_27.setGeometry(QtCore.QRect(9, 80, 71, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_7)
        self.label_28.setGeometry(QtCore.QRect(9, 110, 71, 16))
        self.label_28.setObjectName("label_28")
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_7)
        self.spinBox_6.setGeometry(QtCore.QRect(161, 140, 61, 22))
        self.spinBox_6.setObjectName("spinBox_6")
        self.label_29 = QtWidgets.QLabel(self.groupBox_7)
        self.label_29.setGeometry(QtCore.QRect(10, 140, 71, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_7)
        self.label_30.setGeometry(QtCore.QRect(9, 170, 71, 16))
        self.label_30.setObjectName("label_30")
        self.spinBox_7 = QtWidgets.QSpinBox(self.groupBox_7)
        self.spinBox_7.setGeometry(QtCore.QRect(160, 170, 61, 22))
        self.spinBox_7.setObjectName("spinBox_7")
        self.model_t_image_type = QtWidgets.QComboBox(self.groupBox_7)
        self.model_t_image_type.setGeometry(QtCore.QRect(130, 50, 91, 20))
        self.model_t_image_type.setObjectName("model_t_image_type")
        self.spinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.spinBox_4.setGeometry(QtCore.QRect(160, 80, 62, 22))
        self.spinBox_4.setDecimals(4)
        self.spinBox_4.setSingleStep(0.0001)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.spinBox_5.setGeometry(QtCore.QRect(160, 110, 62, 22))
        self.spinBox_5.setSingleStep(0.01)
        self.spinBox_5.setObjectName("spinBox_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.Set_parameters = QtWidgets.QPushButton(self.centralwidget)
        self.Set_parameters.setGeometry(QtCore.QRect(10, 730, 241, 41))
        self.Set_parameters.setObjectName("Set_parameters")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 274, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "General info"))
        self.Version.setText(_translate("MainWindow", "Version:"))
        self.Date.setText(_translate("MainWindow", "Date"))
        self.radioButton.setText(_translate("MainWindow", "Generate data"))
        self.label_7.setText(_translate("MainWindow", "Config Folder:"))
        self.label_8.setText(_translate("MainWindow", "Product:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Image Property"))
        self.label_6.setText(_translate("MainWindow", "Image width:"))
        self.label_9.setText(_translate("MainWindow", "Image height:"))
        self.label_10.setText(_translate("MainWindow", "Center offset"))
        self.label_2.setText(_translate("MainWindow", "Image type"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Training"))
        self.pushButton_2.setText(_translate("MainWindow", "Add engine"))
        self.label_4.setText(_translate("MainWindow", "Active Engines"))
        self.pushButton.setText(_translate("MainWindow", "Remove engine"))
        self.label_11.setText(_translate("MainWindow", "Training precentage"))
        self.label_12.setText(_translate("MainWindow", "Validation precentage"))
        self.label_13.setText(_translate("MainWindow", "Max epoch no improve"))
        self.debug.setText(_translate("MainWindow", "Debug mode"))
        self.label.setText(_translate("MainWindow", "Product:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Product"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Image properties"))
        self.label_5.setText(_translate("MainWindow", "Image type"))
        self.Image_type_engine.setItemText(0, _translate("MainWindow", "color"))
        self.Image_type_engine.setItemText(1, _translate("MainWindow", "color_ref"))
        self.Image_type_engine.setItemText(2, _translate("MainWindow", "color_bw"))
        self.Image_type_engine.setItemText(3, _translate("MainWindow", "bw"))
        self.Image_type_engine.setItemText(4, _translate("MainWindow", "bw_ref"))
        self.Image_type_engine.setItemText(5, _translate("MainWindow", "bw2"))
        self.Image_type_engine.setItemText(6, _translate("MainWindow", "bw2_ref"))
        self.Image_type_engine.setItemText(7, _translate("MainWindow", "ici"))
        self.Image_type_engine.setItemText(8, _translate("MainWindow", "ici_ref"))
        self.label_14.setText(_translate("MainWindow", "resize image size"))
        self.label_15.setText(_translate("MainWindow", "Translate shift"))
        self.label_16.setText(_translate("MainWindow", "Roi size"))
        self.Image_convert.setItemText(0, _translate("MainWindow", "no_conversion"))
        self.Image_convert.setItemText(1, _translate("MainWindow", "color_to_bw"))
        self.Image_convert.setItemText(2, _translate("MainWindow", "bw_to_color"))
        self.label_17.setText(_translate("MainWindow", "Convert"))
        self.roi_resize.setText(_translate("MainWindow", "Roi Resize"))
        self.image_smooth.setText(_translate("MainWindow", "Smotth image"))
        self.label_21.setText(_translate("MainWindow", "Engine number"))
        self.label_3.setText(_translate("MainWindow", "Engine"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Generate training data"))
        self.label_18.setText(_translate("MainWindow", "Max factor"))
        self.label_19.setText(_translate("MainWindow", "exceeding precentage"))
        self.label_20.setText(_translate("MainWindow", "unbalanced ratio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Engine"))
        self.label_23.setText(_translate("MainWindow", "Model trial name"))
        self.label_31.setText(_translate("MainWindow", "Sub engine name"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Model trial"))
        self.label_22.setText(_translate("MainWindow", "Engine type"))
        self.engine_type.setItemText(0, _translate("MainWindow", "simple"))
        self.engine_type.setItemText(1, _translate("MainWindow", "join_2"))
        self.label_24.setText(_translate("MainWindow", "batch size"))
        self.active_trial.setText(_translate("MainWindow", "Active "))
        self.groupBox_7.setTitle(_translate("MainWindow", "Sub Engine"))
        self.label_25.setText(_translate("MainWindow", "architecture"))
        self.architecture.setItemText(0, _translate("MainWindow", "resnet18"))
        self.architecture.setItemText(1, _translate("MainWindow", "resnet34"))
        self.architecture.setItemText(2, _translate("MainWindow", "resnet50"))
        self.architecture.setItemText(3, _translate("MainWindow", "resnet152"))
        self.architecture.setItemText(4, _translate("MainWindow", "alex_net"))
        self.architecture.setItemText(5, _translate("MainWindow", "vgg16"))
        self.architecture.setItemText(6, _translate("MainWindow", "googlenet"))
        self.architecture.setItemText(7, _translate("MainWindow", "squeezenet"))
        self.architecture.setItemText(8, _translate("MainWindow", "densenet"))
        self.architecture.setItemText(9, _translate("MainWindow", "inception"))
        self.architecture.setItemText(10, _translate("MainWindow", "shufflenet"))
        self.architecture.setItemText(11, _translate("MainWindow", "mobilenet"))
        self.architecture.setItemText(12, _translate("MainWindow", "resnext"))
        self.label_26.setText(_translate("MainWindow", "image type"))
        self.label_27.setText(_translate("MainWindow", "Learning rate"))
        self.label_28.setText(_translate("MainWindow", "factor"))
        self.label_29.setText(_translate("MainWindow", "patiance"))
        self.label_30.setText(_translate("MainWindow", "max epochs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Model trial"))
        self.Set_parameters.setText(_translate("MainWindow", "Set parameters"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
