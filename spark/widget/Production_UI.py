from spark.widget.import_module import *
from spark.widget.sample_widget import SAMPLE_WIDGET
from spark.widget.widget_template import WIDGET_TEMPLATE
from spark.widget.color_variable import COLOR_VARIABLE
import os, getpass

class PRODUCTION_UI(SAMPLE_WIDGET):


    def __init__(self, title='Production UI', width=419, height=435):
        super().__init__(title=title, width=width, height=height)

        # EXTERNAL CLASS
        self.widget_template_class = WIDGET_TEMPLATE()
        self.color_variable_class = COLOR_VARIABLE()

        self.update_ui()

    def update_ui(self):
        layout_name = self.get_layout()
        self.production_setup_gridLayout = QGridLayout()
        self.production_setup_gridLayout.setSpacing(2)
        self.production_setup_gridLayout.setObjectName("production_setup_gridLayout")

        #USER PUSHBUTTON
        pushbutton_styleSheet = self.widget_template_class.styleSheet_def(obj_name='QPushButton',
                                                                          color='qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.357955         rgba(27, 166, 208, 255), stop:1 rgba(0, 59, 111, 0));',
                                                                          border_radius=50)
        pushbutton_toolTip = self.widget_template_class.styleSheet_def(obj_name='QToolTip',
                                                                       background_color=[22, 124, 152],
                                                                       color=[80, 231, 186])

        style_sheet = pushbutton_styleSheet + '\n' + pushbutton_toolTip
        print(style_sheet)

        self.user_pushButton = self.widget_template_class.pushButton_def(MinSize=[100, 100],
                                                                         toolTip=getpass.getuser(),
                                                                         icon_size=[100, 100],
                                                                         StyleSheet=style_sheet)
        self.production_setup_gridLayout.addWidget(self.user_pushButton, 1, 1, 1, 1)




        #USER NAME
        #MAYA SETUP
        #NODE EDITOR




        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.production_setup_gridLayout.addItem(spacerItem2, 7, 0, 1, 3)

        self.verticalLayout.addLayout(self.production_setup_gridLayout)












if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PRODUCTION_UI()
    sys.exit(app.exec_())