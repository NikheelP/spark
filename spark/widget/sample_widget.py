from spark.widget.import_module import *


class SAMPLE_WIDGET(QMainWindow):

    def __init__(self, title='Sample Title', width = 640, height=480):
        super().__init__()
        
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
        def moveWindow(event):
            #IF LEFT MOUSE CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()


        #CENTRAL WIDGET
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet("background-color: rgb(4, 39, 48);")
        self.central_widget.setObjectName("central_widget")

        #VERTICAL LAYOUT
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.mouseMoveEvent = moveWindow
        
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
        self.label.setText('UI Name')
        self.GridLayout.addWidget(self.label, 0, 0, 1, 1)

        #MINIMIZE
        self.minimize_pushButton = QPushButton(self.central_widget)
        self.minimize_pushButton.setMinimumSize(QSize(20, 20))
        self.minimize_pushButton.setMaximumSize(QSize(20, 20))
        self.minimize_pushButton.setStyleSheet("background-color: rgb(0, 255, 0); border-radius: 10px;")
        self.minimize_pushButton.setText("")
        self.minimize_pushButton.setObjectName("minimize_pushButton")
        self.minimize_pushButton.clicked.connect(self.showMinimized)
        self.GridLayout.addWidget(self.minimize_pushButton, 0, 1, 1, 1)

        #MAXIMIZE
        self.maximize_pushButton = QPushButton(self.central_widget)
        self.maximize_pushButton.setMinimumSize(QSize(20, 20))
        self.maximize_pushButton.setMaximumSize(QSize(20, 20))
        self.maximize_pushButton.setStyleSheet("background-color: rgb(255, 255, 0); border-radius: 10px;")
        self.maximize_pushButton.setText("")
        self.maximize_pushButton.setObjectName("maximize_pushButton")
        self.maximize_pushButton.clicked.connect(self.maximize_pushButton_def)
        self.GridLayout.addWidget(self.maximize_pushButton, 0, 2, 1, 1)

        #CLOSE
        self.close_pushButton = QPushButton(self.central_widget)
        self.close_pushButton.setMinimumSize(QSize(21, 23))
        self.close_pushButton.setMaximumSize(QSize(20, 20))
        self.close_pushButton.setStyleSheet("background-color: rgb(255, 0, 0); border-radius: 10px;")
        self.close_pushButton.setText("")
        self.close_pushButton.setObjectName("close_pushButton")
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
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


class production_ui(SAMPLE_WIDGET):
    def __init__(self, title='Another Sample', width=640, height=480):
        super().__init__(title=title, width=width, height=height)

        self.update_ui()


    def update_ui(self):
        layout_name = self.get_layout()
        self.production_setup_gridLayout = QGridLayout()
        self.production_setup_gridLayout.setSpacing(2)
        self.production_setup_gridLayout.setObjectName("production_setup_gridLayout")



        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.production_setup_gridLayout.addItem(spacerItem2, 7, 0, 1, 3)

        self.verticalLayout.addLayout(self.production_setup_gridLayout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = production_ui()
    sys.exit(app.exec_())

