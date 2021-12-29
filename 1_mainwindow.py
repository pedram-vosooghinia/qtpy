import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg 



class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #add a title
        self.setWindowTitle("hello pedram :0")

        #set vertual layout
        self.setLayout(qtw.QVBoxLayout())

        #create a lable
        my_label = qtw.QLabel("hello word, whats your name?")
        
        #change the font size of label

        my_label.setFont(qtg.QFont("helvetica",18))

        self.layout().addWidget(my_label)


        #create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName('name_field')
        my_entry.setText("pedram")
        self.layout().addWidget(my_entry)
        
        # create a button
        my_button = qtw.QPushButton("press me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)


        #show the app    
        self.show()

        def press_it():
            # add name to lable
            my_label.setText(f'hello {my_entry.text()}')
            # clear the entry box
            my_entry.setText("")


app = qtw.QApplication([])
mw = MainWindow()

#run the app

app.exec_()