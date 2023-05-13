import sys
import statistics_1.py
from PyQt5.QtWidgets import QDesktopWidget,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox,QLineEdit

# Create a new application instance
app = QApplication(sys.argv)

# Create a new window instance
window = QWidget()

# Set the window size and title
window.setWindowTitle('My PyQt5 Window')
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
department.setPlaceholderText('Select a department')
department.setStyleSheet('background-color: #f7d6e0;')
department.setFixedSize(300, 40)
container_layout.addWidget(department)

location = QComboBox()
lineedit = QLineEdit()
lineedit.setPlaceholderText('Select a location')
location.setLineEdit(lineedit)
location.setPlaceholderText('Select a location')
location.setStyleSheet('background-color: #f7d6e0;')
location.setFixedSize(300, 40)
container_layout.addWidget(location)

time = QComboBox()
lineedit = QLineEdit()
lineedit.setPlaceholderText('Select a time')
time.setLineEdit(lineedit)
time.setPlaceholderText('Select a time')
time.setStyleSheet('background-color: #f7d6e0;')
time.setFixedSize(300, 40)
container_layout.addWidget(time)

# Set the container layout for the container widget
container.setLayout(container_layout)

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
