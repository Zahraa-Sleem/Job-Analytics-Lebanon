import sys
import pandas as pd
import os
import json
from getcategory import *
from plotting import *
import plotly.express as px
from PyQt5.QtWidgets import QPushButton,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox,QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore
from filtering import *

Graph_Department=None
Graph_Title=None
Graph_Location=None
Graph_Time=None
widgets_added = False
webview1 = None
webview2 = None
webview3 = None
 

def filter():
    global widgets_added
    global webview1
    global webview2
    global webview3
    if not widgets_added:
        webview1 = QWebEngineView()
        webview2 = QWebEngineView()
        webview3 = QWebEngineView()
        layout.addWidget(webview2)
        layout.addWidget(webview3)
        widgets_added = True
    #Changing dataframe from filtered values
    department_selected_value = department.currentText()
    location_selected_value = location.currentText()
    time_selected_value = time.currentText()
    global Graph_Department
    Graph_Department=None
    global Graph_Title
    Graph_Title=None
    global Graph_Location
    Graph_Location=None
    global Graph_Time
    Graph_Time=None
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
    toberepresented=dataframe
    if(len(attributes)>0):
        toberepresented=filter_dataframe(dataframe, attributes, values)
    draw(attributes,toberepresented)
        # Save the graphs as separate HTML files
    if Graph_Department!=None:
        print("PRINTING GRAPH DEPARTMENT \n",Graph_Department)
        Graph_Department.write_html('department.html')
        # webview = QWebEngineView()
        # webview.load(QtCore.QUrl.fromLocalFile(os.path.abspath('department.html')))
    else:
        print("GRAPH DEPARTMENT IS NONE")
    if Graph_Time!=None: 
        print("PRINTING GRPAH TIME",Graph_Time)
        Graph_Time.write_html('time.html')
        # webview2 = QWebEngineView()
        webview2.load(QtCore.QUrl.fromLocalFile(os.path.abspath('time.html')))
    if Graph_Title!=None:
        print("PRINTING GRAPH TITLE",Graph_Title)
        Graph_Title.write_html('titles.html')
        # webview3 = QWebEngineView()
        webview3.load(QtCore.QUrl.fromLocalFile(os.path.abspath('titles.html')))
def draw(filters,toberepresented):
    if 'department' not in filters:
        print("Department not in filters")
        global Graph_Department
        Graph_Department=plotdepartments(toberepresented)
    # if 'location' not in filters:
    #     Graph_Location=plotlocation(toberepresented)
    if 'time' not in filters:
        print("Time not in filters")
        global Graph_Time
        Graph_Time=plottime(toberepresented)
    global Graph_Title
    Graph_Title=plottags(toberepresented)  
    
    
#Reading the json file
with open('objects.json') as f:
    data = json.load(f)
dataframe= pd.read_json(json.dumps(data))

# Create a new application instance
app = QApplication(sys.argv)

# Create a new window instance
window = QWidget()

# Set the window size and title
window.setWindowTitle('Analysis')
window.setFixedSize(1000, 800)
# Set the background color of the container widget
window.setStyleSheet('background-color: #eff7f6;')

# Create a vertical layout for the window
layout = QVBoxLayout()

# Create a container widget for the drop-downs
container = QWidget()
container.setFixedSize(950, 70)

# Set the background color of the container widget
container.setStyleSheet('background-color: #a1b5d8;')

# Create a horizontal layout for the container
container_layout = QHBoxLayout()

# Create three drop-downs and add them to the container layout
department = QComboBox()
lineedit = QLineEdit()
lineedit.setPlaceholderText('Select a department')
department.setLineEdit(lineedit)
department.setStyleSheet('background-color: #f7d6e0;')
department.setFixedSize(250, 40)
department.addItems(getdepartments(dataframe))
container_layout.addWidget(department)

location = QComboBox()
lineedit = QLineEdit()
lineedit.setPlaceholderText('Select a location')
location.setLineEdit(lineedit)
location.setStyleSheet('background-color: #f7d6e0;')
location.setFixedSize(250, 40)
location.addItems(getlocations(dataframe))
container_layout.addWidget(location)

time = QComboBox()
lineedit = QLineEdit()
lineedit.setPlaceholderText('Select a time')
time.setLineEdit(lineedit)
time.setStyleSheet('background-color: #f7d6e0;')
time.setFixedSize(250, 40)
time.addItems(gettime(dataframe))
container_layout.addWidget(time)

# Set the container layout for the container widget
container.setLayout(container_layout)

#Filter Button
filter_button = QPushButton('Filter')
filter_button.setStyleSheet('background-color: #f7d6e0;')
filter_button.setFixedSize(80, 40)
container_layout.addWidget(filter_button)

# Connect the button's clicked signal to the button_clicked function
filter_button.clicked.connect(filter)

# Add the container to the main layout at the top
layout.insertWidget(0, container)

# Add a stretch to center the container vertically
layout.addStretch(1)

# Set the main layout for the window
window.setLayout(layout)

# Show the window
window.show()

# Run the event loop to keep the window open
sys.exit(app.exec_())

