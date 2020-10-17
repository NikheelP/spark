


import sys
#IMPORT MODULE ACCORDING TO REQUIREMENT
try:
    #import pyqt5 moduler
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

except:
    try:
        #import PyQt4 moduler
        from PyQt4.QtGui import *
        from PyQt4.QtCore import *
    except:
        try:
            #import pyside moduler
            from PySide.QtGui import *
            from PySide.QtCore import *
        except:
            raise Exception('Python Version does not have PyQt5 or PyQt4 or Pyside \n' 
                            'please install any of this and run command again')