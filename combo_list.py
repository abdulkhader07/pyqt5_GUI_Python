import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #adding title
        self.setWindowTitle("simple Gui with menu")

        #set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        #create a label
        my_label = qtw.QLabel("hello!.. please select from the list ")
        #change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)

        #create an combo box
        my_combo = qtw.QComboBox(self)
        #add items to the combo box
        my_combo.addItem("apple","something")
        my_combo.addItem("Mango",2)
        my_combo.addItem("Banana")
        my_combo.addItem("cherry")
        my_combo.addItem("papaya")
        my_combo.addItem("orange")

        #put combo box on the screen
        self.layout().addWidget(my_combo)

        #create a button
        my_button = qtw.QPushButton("press me!",clicked = lambda: press_it())
        self.layout().addWidget(my_button)


        #show the GUI
        self.show()

        def press_it():
          #add name to label
          my_label.setText(f"you picked {my_combo.currentText()}...")

app = qtw.QApplication([])
mw = MainWindow()

#run the gui
app.exec_()