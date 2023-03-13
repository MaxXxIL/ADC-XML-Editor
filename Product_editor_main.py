import os.path
from product_editor import Ui_MainWindow
from PyQt5.QtWidgets import QApplication ,QMainWindow ,QPushButton ,QWidget ,QListWidget ,QLabel ,QListView ,QMessageBox
import sys
import xmltodict




class my_window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_params()
        self.emgime_image_type=('color','color_ref','color_bw','bw','bw_ref','bw2','bw2_ref','ici','ici_ref')
        self.engine_convert=('no_conversion','color_to_bw','bw_to_color')
        self.engine_types = ('simple', 'join_2')
        self.architectures = ('resnet18', 'resnet34', 'resnet50', 'resnet152', 'alex_net', 'vgg16', 'googlenet', 'squeezenet', 'densenet', 'inception', 'shufflenet', 'mobilenet', 'resnext')
        self.comboBox.activated.connect(self.init_product)
        self.Image_type.activated.connect(self.change_image_type)
        self.comboBox_Engine.activated.connect(self.change_engine)
        self.model_trial.activated.connect(self.change_model_trial)
        self.Set_parameters.clicked.connect(self.edit_dict)

    def init_product(self):
        product = self.comboBox.currentText()
        Xml_dict = self.Read_XML_file(os.path.normpath('C:/adc/configurations/' + product + '/config1_' + product +'/ADC_generate_training_Engines_Setup.xml'))
        self.root_element = Xml_dict['root']
        self.Version.setText(('Version: ' + self.root_element['version']['number']))
        self.Date.setText(('Date: ' + self.root_element['version']['date']))
        self.Date.setText(('Date: ' + self.root_element['version']['date']))
        self.plainTextEdit_2.setPlainText(self.root_element['config_folder_name'])
        self.plainTextEdit_3.setPlainText(self.root_element['product'])
        self.listWidget.clear()
        if self.root_element['active_engines'].__class__ == list:
            self.listWidget.addItems(self.root_element['active_engines'])
        else:
            self.listWidget.addItem(self.root_element['active_engines'])
        if self.root_element['generate']['generate_data_in_addition_to_factors'] == '1':
            self.radioButton.setChecked(1)

        image_element = self.root_element['input_image_properties']['image']
        self.im_type_dict={}
        im_type_l=[]
        for im_type in image_element:
            self.im_type_dict[im_type['image_type_name']] = (im_type['image_type_name'], im_type['size_w'], im_type['size_h'], im_type['max_offset_from_center'])
            im_type_l.append(im_type['image_type_name'])
        self.Image_type.clear()
        self.Image_type.addItems(im_type_l)
        self.update_image_type(self.im_type_dict[im_type_l[0]])
        self.debug.setChecked(int(self.root_element['process']['debug']))
        self.training_p.setPlainText(str(float(self.root_element['train']['training_percent'])*100))
        self.validation_p.setPlainText(str(float(self.root_element['train']['validation_percent']) * 100))
        self.max_epochs.setPlainText(self.root_element['train']['n_epochs_with_no_improvment'])
        self.engine_dict={}
        engines_l=[]
        engine_element = self.root_element['engines']['engine']
        for eng in engine_element:
            self.engine_dict[eng['name']] = eng
            engines_l.append(eng['name'])
        self.comboBox_Engine.clear()
        self.comboBox_Engine.addItems(engines_l)
        self.update_engine(engine_element[0])
        x = 1

    def Read_XML_file(self,path):
        with open(path) as fd:
            doc = xmltodict.parse(fd.read())
        return doc

    def init_params(self):
        products_list = self.search_products()
        self.comboBox.addItems(products_list)

    def search_products(self):
        list=[]
        dir_path = os.path.normpath('C:/adc/configurations')
        dirs = os.listdir(dir_path)
        for dir in dirs:
            if os.path.exists(os.path.normpath(dir_path + '/' + dir + '/config1_' + dir)):
                #sub_dir = os.listdir(os.path.normpath(dir_path + '/' + dir + '/config1_' + dir))
                if os.path.exists(os.path.normpath(dir_path + '/' + dir + '/config1_' + dir + '/ADC_generate_training_Engines_Setup.xml')) and os.path.exists(os.path.normpath(dir_path + '/' + dir + '/config1_' + dir + '/ADC_Setup.xml')):
                    list.append(dir)
        return list

    def change_model_trial(self):
        model_trial = self.model_trial.currentText()
        self.update_model_trial(self.trial_dict[model_trial])

    def update_model_trial(self,model_t):

        #model_t = eng['train']['model_trial'][0]
        indx = self.engine_types.index(model_t['engine_type'])
        self.engine_type.setCurrentIndex(indx)
        self.spinBox_3.setValue(int(model_t['batch_size']))
        if model_t['active'] == '1':
            self.active_trial.setChecked(1)
        else:
            self.active_trial.setChecked(0)
        sub_engine_l = []
        sub_engine_dict = {}
        if len(model_t['sub_engines']) == 1:
            sub_engine_l.append(model_t['sub_engines']['sub_engine']['image_type_name'])
            sub_engine_dict[model_t['sub_engines']['sub_engine']['image_type_name']] = model_t['sub_engines']
        else:
            for sub in model_t['sub_engines']:
                sub_engine_l.append(sub['sub_engine']['image_type_name'])
                sub_engine_dict[model_t['sub_engines']['sub_engine']['image_type_name']] = model_t['sub_engines'][
                    'sub_engine']
        self.sub_engine.clear()
        self.sub_engine.addItems(sub_engine_l)
        indx = self.architectures.index(sub_engine_dict[self.sub_engine.currentText()]['sub_engine']['model_type'])
        self.architecture.setCurrentIndex(indx)

        # self.architecture.setCurrentIndex(indx)
        learning_str = sub_engine_dict[self.sub_engine.currentText()]['sub_engine']['learning_rate']
        tmp_str = learning_str.split('lr')
        tmp_str = tmp_str[1].split('_')
        self.spinBox_4.setValue(float(tmp_str[0]))
        tmp_str2 = tmp_str[1].split('factor')
        self.spinBox_5.setValue(float(tmp_str2[1]))
        tmp_str3 = tmp_str[2].split('patience')
        tmp_str3 = tmp_str3[1].split('*')
        self.spinBox_6.setValue(int(tmp_str3[0]))
        self.spinBox_7.setValue(int(tmp_str3[1]))

    def change_engine(self):
        eng = self.comboBox_Engine.currentText()
        self.update_engine(self.engine_dict[eng])

    def update_engine(self,eng):
        self.eng_num.setValue(int(eng['number']))
        type_name = self.Image_type_engine.currentText()
        indx = self.emgime_image_type.index(type_name)
        self.Image_type_engine.setCurrentIndex(indx)
        image_type_l=[]
        if len(eng['images']) == 1:
            image_type_l.append(eng['images']['image']['image_type_name'])
        else:
            for image in eng['images']['image']:
                image_type_l.append(image['image_type_name'])
        self.model_t_image_type.clear()
        self.model_t_image_type.addItems(image_type_l)
        indx = self.engine_convert.index(eng['images']['image']['convert_to'])
        self.Image_convert.setCurrentIndex(indx)
        self.Image_resize.setPlainText(eng['images']['image']['source_image_size_linked_to_minus_one'])
        if eng['images']['image']['roi_resize'] == '-1':
            self.roi_resize.setChecked(1)
        else:
            self.roi_resize.setChecked(0)
        self.roi_size.setPlainText(eng['images']['image']['roi_size'])
        self.translate_shift.setPlainText(eng['images']['image']['translate_shift'])
        if eng['images']['image']['smooth_image'] == '0':
            self.image_smooth.setChecked(1)
        else:
            self.image_smooth.setChecked(0)
        self.spinBox.setValue(int(eng['generate']['max_factor']))
        self.spinBox_2.setValue(int(eng['generate']['max_factor_exceeding_percentage']))
        self.doubleSpinBox_2.setValue(float(eng['generate']['unbalanced_allowed_ratio']))
        self.trial_dict = {}
        trial_l = []
        for model_trial in eng['train']['model_trial']:
            self.trial_dict[model_trial['name']] = model_trial
            trial_l.append(model_trial['name'])
        self.model_trial.clear()
        self.model_trial.addItems(trial_l)
        self.update_model_trial(eng['train']['model_trial'][0])
        x = 1
        #indx = self.architectures.index(model_t['model_type'])
        #self.architecture.setCurrentIndex(indx)
        #indx =
        #self.model_t_image_type.setCurrentIndex(indx)
        #type_engine.setCurrentItem(eng['images']['image_type_name'])
        #self.Image_type_engine.seeng['images']['image_type_name']

    def change_image_type(self):
        product = self.Image_type.currentText()
        self.update_image_type(self.im_type_dict[product])

    def update_image_type(self,image_element):
        self.Image_width.setPlainText(image_element[1])
        self.Image_height.setPlainText(image_element[2])
        self.Image_offset.setPlainText(image_element[3])

    def edit_dict(self):
        indx = self.tabWidget.currentIndex()
        if indx == 0:
            self.update_product_info()
        elif indx == 1:
            self.update_engine_info()
        else:
            self.update_model_info()

    def update_product_info(self):
        x =1
    def update_engine_info(self):
        x =1
    def update_model_info(self):
        x =1

if __name__ == "__main__":
    app=QApplication(sys.argv)
    main_win=my_window()
    main_win.show()
    app.exec_()