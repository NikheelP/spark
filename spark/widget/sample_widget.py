from spark.widget.import_module import *
from spark.widget.widget_template import WIDGET_TEMPLATE
from spark.widget.color_variable import COLOR_VARIABLE


import sys

class SAMPLE_WIDGET(QMainWindow):

    def __init__(self, title='Sample Title', width = 640, height=480):
        super().__init__()

        #EXTERNAL CLASS
        self.widget_template_class = WIDGET_TEMPLATE()
        self.color_variable_class = COLOR_VARIABLE()

        #SET WINDOW TITLE
        self.title = title


        #SET WINDOW WIDTH AND HEIGHT
        self.width = width
        self.height = height

        #MAKE WINDOW MOVE IN FRAMELESS
        self.center()
        
        self.initUI()
        self.show()
                
    def initUI(self):
        '''
        CREATE INITIAL UI
        '''
        self.resize(self.width, self.height)

        #SET WINDOT TITLE
        self.setWindowTitle(self.title)
 
        #IMPORT FUCTIONS
        self.first_layout()
        self.set_window_frameless()
    
    def set_window_frameless(self):
        #CREATE WINDOW FRAMELESS
        self.setWindowFlag(Qt.FramelessWindowHint)


    def first_layout(self):
        '''
        FIRST LAYOUT WHICH HAS LABEL AND CLOSE, MAXIMIZE AND MINIMIZE WINDOW
        '''

        #CENTRAL WIDGET
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet("background-color: rgb(4, 39, 48);")
        self.central_widget.setObjectName("central_widget")

        #VERTICAL LAYOUT
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        #PRODUCTION NAME
        self.GridLayout = QGridLayout()
        self.GridLayout.setHorizontalSpacing(5)
        self.GridLayout.setVerticalSpacing(0)
        self.GridLayout.setObjectName("GridLayout")
        
        #LABEL
        self.label = QLabel()
        self.label.setStyleSheet("color: rgb(0, 255, 0); font-size: 12pt; font-weight: bold;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label.setText(self.title)
        self.GridLayout.addWidget(self.label, 0, 0, 1, 1)

        #MINIMIZE
        val = self.color_variable_class.get_minimize_color().get_color()
        mini_styleSheet = self.widget_template_class.styleSheet_def(obj_name='QPushButton',
                                                                    background_color=val,
                                                                    border_radius=10)
        self.minimize_pushButton = self.widget_template_class.pushButton_def(MinSize = [20, 20],
                                                                             MaxSize=[20, 20],
                                                                             StyleSheet=mini_styleSheet)
        self.minimize_pushButton.clicked.connect(self.showMinimized)
        self.GridLayout.addWidget(self.minimize_pushButton, 0, 1, 1, 1)

        #MAXIMIZE
        val = self.color_variable_class.get_maxmize_color().get_color()
        max_styleSheet = self.widget_template_class.styleSheet_def(obj_name='QPushButton',
                                                                   background_color=val,
                                                                   border_radius=10)
        self.maximize_pushButton = self.widget_template_class.pushButton_def(MinSize=[20, 20], MaxSize=[20, 20],
                                                                             StyleSheet=max_styleSheet)
        self.maximize_pushButton.clicked.connect(self.maximize_pushButton_def)
        self.GridLayout.addWidget(self.maximize_pushButton, 0, 2, 1, 1)

        #CLOSE
        val = self.color_variable_class.get_close_color().get_color()
        close_styleSheet = self.widget_template_class.styleSheet_def(obj_name='QPushButton',
                                                                     background_color=val,
                                                                     border_radius=10)
        self.close_pushButton = self.widget_template_class.pushButton_def(MinSize=[20, 20],
                                                                          MaxSize=[20, 20],
                                                                          StyleSheet=close_styleSheet)
        self.close_pushButton.clicked.connect(self.close)
        self.GridLayout.addWidget(self.close_pushButton, 0, 3, 1, 1)

        self.verticalLayout.addLayout(self.GridLayout)
        self.setCentralWidget(self.central_widget)

    def get_layout(self):
        return self.verticalLayout

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def maximize_pushButton_def(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def center(self):
        if  self.isMaximized():
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()










