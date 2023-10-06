import pandas as pd
import os
import json
from getcategory import *
from plotting import *
import plotly.express as px
from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox,QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore
from filtering import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Graph_Department=None
        self.Graph_Location=None
        self.Graph_Title=None
        self.Graph_Time=None
        self.webview=None
        self.webview1 = None
        self.webview2 = None
        self.webview3 = None
        self.overalllayout=None
        self.upperlayout=None
        self.lowerlayout=None
        self.graphslayout=None
        self.readjsonfile()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Analysis')
        self.setFixedSize(1200, 1500)
        self.setStyleSheet('background-color:#eff7f6')

        # Create a central widget to hold the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the window
        self.overalllayout = QVBoxLayout(central_widget)
        
        # Create a horizontal layout for the graphs
        self.graphslayout = QVBoxLayout()

        # Create a vertical layout for the upper part of graph layout
        self.upperlayout = QHBoxLayout()
        self.graphslayout.addLayout(self.upperlayout)

        # Create a vertical layout for the middle part of graph layout
        self.middlelayout = QHBoxLayout()
        self.graphslayout.addLayout(self.middlelayout)
        
        # Create a vertical layout for the lower part of graph layout
        self.lowerlayout = QHBoxLayout()
        self.graphslayout.addLayout(self.lowerlayout)

        # Add the graphslayout to the overalllayout
        self.overalllayout.addLayout(self.graphslayout)
        
        # Create a container widget for the drop-downs
        container = QWidget()
        container.setFixedSize(1170, 70)
        
        # Set the background color of the container widget
        container.setStyleSheet('background-color: #a1b5d8;')

        # Create a horizontal layout for the container
        container_layout = QHBoxLayout()

        # Create three drop-downs and add them to the container layout
        self.department = QComboBox()
        lineedit = QLineEdit()
        lineedit.setPlaceholderText('Select a department')
        self.department.setLineEdit(lineedit)
        self.department.setStyleSheet('background-color: #f7d6e0;')
        self.department.setFixedSize(250, 40)
        self.department.addItems(getdepartments(self.dataframe))
        container_layout.addWidget(self.department)

        self.location = QComboBox()
        lineedit = QLineEdit()
        lineedit.setPlaceholderText('Select a location')
        self.location.setLineEdit(lineedit)
        self.location.setStyleSheet('background-color: #f7d6e0;')
        self.location.setFixedSize(250, 40)
        self.location.addItems(getlocations(self.dataframe))
        container_layout.addWidget(self.location)

        self.time = QComboBox()
        lineedit = QLineEdit()
        lineedit.setPlaceholderText('Select a time')
        self.time.setLineEdit(lineedit)
        self.time.setStyleSheet('background-color: #f7d6e0;')
        self.time.setFixedSize(250, 40)
        self.time.addItems(gettime(self.dataframe))
        container_layout.addWidget(self.time)

        # Set the container layout for the container widget
        container.setLayout(container_layout)

        #Filter Button
        filter_button = QPushButton('Filter')
        filter_button.setStyleSheet('background-color: #f7d6e0;')
        filter_button.setFixedSize(80, 40)
        container_layout.addWidget(filter_button)

        # Connect the button's clicked signal to the button_clicked function
        filter_button.clicked.connect(self.filter)

        # Add the container to the main layout at the top
        self.overalllayout.insertWidget(0, container)

        #Add a stretch to center the container vertically
        self.overalllayout.addStretch(1)
        self.show()
    
    def readjsonfile(self):
        with open('objects.json') as f:
            data = json.load(f)
        self.dataframe= pd.read_json(json.dumps(data))
    
    def filter(self):
        department_selected_value = self.department.currentText()
        location_selected_value = self.location.currentText()
        time_selected_value = self.time.currentText()
        self.Graph_Department=None
        self.Graph_Title=None
        self.Graph_Location=None
        self.Graph_Time=None
        #setting the filtered
        attributes=[]
        values=[]
        if(department_selected_value!=''):
            attributes.append('department')
            values.append(department_selected_value)
        if(location_selected_value!=''):
            attributes.append('location')
            values.append(location_selected_value)
        if(time_selected_value!=''):
            attributes.append('time')
            values.append(time_selected_value)  
        toberepresented=self.dataframe
        if(len(attributes)>0):
            toberepresented=filter_dataframe(self.dataframe, attributes, values)
        self.draw(attributes,toberepresented)
            
    def draw(self,filters,toberepresented):
        if len(toberepresented):
            if 'department' not in filters:
                self.Graph_Department=plotdepartments(toberepresented)
            if 'location' not in filters:
                self.Graph_Location=plotlocation(toberepresented)   
            if 'time' not in filters:
                self.Graph_Time=plottime(toberepresented)
            self.Graph_Title=plottags(toberepresented)
            self.showGraphs()
        else:
            if self.webview is not None:
                self.upperlayout.removeWidget(self.webview)
                self.webview.deleteLater()
                self.webview = None
            if self.webview1 is not None:    
                self.lowerlayout.removeWidget(self.webview1)
                self.webview1.deleteLater()
                self.webview1 = None
            if self.webview2 is not None:
                self.upperlayout.removeWidget(self.webview2)
                self.webview2.deleteLater()
                self.webview2 = None
            if self.webview3 is not None:    
                self.upperlayout.removeWidget(self.webview3)
                self.webview3.deleteLater()
                self.webview3 = None
            
              
    def showGraphs(self):
        if self.Graph_Department is not None:
            self.Graph_Department.write_html('department.html')
            if self.webview is None:
                self.webview = QWebEngineView()
            self.webview.load(QtCore.QUrl.fromLocalFile(os.path.abspath('department.html')))
            self.upperlayout.addWidget(self.webview)
        elif self.webview is not None:
            self.upperlayout.removeWidget(self.webview)
            self.webview.deleteLater()
            self.webview = None
        
        if self.Graph_Location is not None:
            self.Graph_Location.save('map.html')
            if self.webview1 is None:
                self.webview1 = QWebEngineView()
            self.webview1.load(QtCore.QUrl.fromLocalFile(os.path.abspath('map.html')))
            self.lowerlayout.addWidget(self.webview1)
        elif self.webview1 is not None:
            self.lowerlayout.removeWidget(self.webview1)
            self.webview1.deleteLater()
            self.webview1 = None

        if self.Graph_Time is not None: 
            self.Graph_Time.write_html('time.html')
            if self.webview2 is None:
                self.webview2 = QWebEngineView()
            self.webview2.load(QtCore.QUrl.fromLocalFile(os.path.abspath('time.html')))
            self.upperlayout.addWidget(self.webview2)
        elif self.webview2 is not None:
            self.upperlayout.removeWidget(self.webview2)
            self.webview2.deleteLater()
            self.webview2 = None

        if self.Graph_Title is not None:
            self.Graph_Title.write_html('tags.html')
            if self.webview3 is None:
                self.webview3 = QWebEngineView()
            self.webview3.load(QtCore.QUrl.fromLocalFile(os.path.abspath('tags.html')))
            self.upperlayout.addWidget(self.webview3)
        elif self.webview3 is not None:
            self.upperlayout.removeWidget(self.webview3)
            self.webview3.deleteLater()
            self.webview3 = None
        
        

        
# Create the QApplication and Window instance
app = QApplication([])
window = Window()
app.exec_()

    