import sys
import os.path
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import  QPushButton, QWidget, QAction, QTabWidget
from PyQt5.QtWidgets import  QListWidget, QComboBox, QLabel, QLineEdit
from PyQt5.QtWidgets import  QFileDialog, QCheckBox
from PyQt5.QtWidgets import  QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PDielec:'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
 
        self.show()
 
class MyTableWidget(QWidget):        
 
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.settings = {}
        self.settings["eckart"] = True
        self.settings["born"] = False
        self.settings["program"] = "Castep"
        self.settings["filename"] = ""
        self.layout = QVBoxLayout()
 
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()	
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300,200) 
 
        # Add tabs
        self.tabs.addTab(self.tab1,"Main")
        self.tabs.addTab(self.tab2,"Settings")
        self.tabs.addTab(self.tab3,"Scenario 1")
 
        # Create first tab - MAIN
        self.tab1.vbox = QVBoxLayout(self)
        # The program combobox
        hbox = QHBoxLayout()
        self.program_l  = QLabel("Program:",self)
        self.program_l.setToolTip("Choose QM/MM program")
        self.program_cb = QComboBox(self)
        self.program_cb.setToolTip("Choose QM/MM program")
        self.program_cb.addItem('Abinit')
        self.program_cb.addItem('Castep')
        self.program_cb.addItem('Crystal')
        self.program_cb.addItem('Gulp')
        self.program_cb.addItem('Phonopy')
        self.program_cb.addItem('Quantum Espresso')
        self.program_cb.addItem('Vasp')
        index = self.program_cb.findText(self.settings["program"], Qt.MatchFixedString)
        if index >=0:
            self.program_cb.setCurrentIndex(index)
        self.program_cb.currentIndexChanged.connect(self.on_program_cb_changed)
        hbox.addWidget(self.program_l)
        hbox.addWidget(self.program_cb)
        self.tab1.vbox.addLayout(hbox)
        # The file selector
        hbox = QHBoxLayout()
        self.file_l  = QLabel("Output file:",self)
        self.file_l.setToolTip("Choose output file for analysis (press return for a file chooser)")
        self.file_le = QLineEdit(self)
        self.file_le.setToolTip("Choose output file for analysis (press return for a file chooser)")
        self.file_le.setText("")
        self.file_le.returnPressed.connect(self.on_file_le_return)
        self.file_le.textChanged.connect(self.on_file_le_changed)
        hbox.addWidget(self.file_l)
        hbox.addWidget(self.file_le)
        self.tab1.vbox.addLayout(hbox)
        # The eckart checkbox
        hbox = QHBoxLayout()
        self.eckart_l = QLabel("Eckart conditions?", self)
        self.eckart_l.setToolTip("Applying Eckart conditions ensures three zero translation mode)")
        self.eckart_cb = QCheckBox(self)
        self.eckart_cb.setToolTip("Applying Eckart conditions ensures three zero translation mode)")
        self.eckart_cb.setText("")
        self.eckart_cb.setLayoutDirection(Qt.RightToLeft)
        self.eckart_cb.stateChanged.connect(self.on_eckart_changed)
        if self.settings["eckart"]:
            self.eckart_cb.setCheckState(Qt.Checked)
        else:
            self.eckart_cb.setCheckState(Qt.Unchecked)
        hbox.addWidget(self.eckart_l)
        hbox.addWidget(self.eckart_cb)
        self.tab1.vbox.addLayout(hbox)
        # Add the Born neutral condition
        hbox = QHBoxLayout()
        self.born_l = QLabel("Born neutrality?", self)
        self.born_l.setToolTip("Applying Born charge neutrality ensures the unit cell has zero charge")
        self.born_cb = QCheckBox(self)
        self.born_cb.setToolTip("Applying Born charge neutrality ensures unit cell has zero charge")
        self.born_cb.setText("")
        self.born_cb.setLayoutDirection(Qt.RightToLeft)
        self.born_cb.stateChanged.connect(self.on_born_changed)
        if self.settings["born"]:
            self.born_cb.setCheckState(Qt.Checked)
        else:
            self.born_cb.setCheckState(Qt.Unchecked)
        hbox.addWidget(self.born_l)
        hbox.addWidget(self.born_cb)
        self.tab1.vbox.addLayout(hbox)
        # Final button
        self.pushButton1 = QPushButton("Read Output File")
        self.tab1.vbox.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.vbox)
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def on_born_changed(self):
        print("on born change ", self.born_cb.isChecked())
        self.settings["born"] = self.born_cb.isChecked()
        print("on born change ", self.settings["born"])

    def on_eckart_changed(self):
        print("on eckart change ", self.eckart_cb.isChecked())
        self.settings["eckart"] = self.eckart_cb.isChecked()
        print("on eckart change ", self.settings["eckart"])

    def on_file_le_return(self):
        print("on file return ", self.file_le.text())
        # Does the file exist?
        self.settings["filename"] = self.file_le.text()
        if os.path.isfile(self.settings["filename"]):
            self.settings["filename"] = os.path.relpath(self.settings["filename"])
            return
        # The file doesn't exist so open a file chooser
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.settings["filename"], _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        self.settings["filename"] = os.path.relpath(self.settings["filename"])
        if self.settings["filename"]:
            print(self.settings["filename"])
        self.file_le.setText(self.settings["filename"])
 
    def on_file_le_changed(self, text):
        print("on file changed", self.file_le.text())
        print("on file changed", text)
 
    def on_program_cb_changed(self,index):
        print("on program combobox changed", index)
        print("on program combobox changed", self.program_cb.currentText())
        self.settings["program"] = self.program_cb.currentText()
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
