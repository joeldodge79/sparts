#!/usr/bin/python
 
import sys
 
import PySide
from PySide.QtGui import QApplication
from PySide.QtGui import QMessageBox

from sparts.tasks.qt_pyside import QApplicationTask
from sparts.vservice import VService

class Service(VService):
    TASKS=[QApplicationTask]
 
# Create the application object
app = QApplication(sys.argv)
 
# Create a simple dialog box
msgBox = QMessageBox()
msgBox.setText("Hello World - using PySide version " + PySide.__version__)
msgBox.exec_()

