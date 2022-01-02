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
        my_label = qtw.QLabel("pick somthing from the list below?")
        
        #change the font size of label

        my_label.setFont(qtg.QFont("helvetica",18))

        self.layout().addWidget(my_label)


        #create an combo box
        my_combo = qtw.QComboBox(self, editable = True, insertPolicy = qtw.QComboBox.InsertAtTop)
        #my_combo = qtw.QComboBox(self, editable = True, insertPolicy = qtw.QComboBox.InsertAtBottom)

        # add item to the combo box
        my_combo.addItem("Peperoni", "something")
        my_combo.addItem("cheese", 2)
        my_combo.addItem("mushroom", qtw.QWidget)
        my_combo.addItem("Peppers")
        my_combo.addItems(["one", "two","three"])
        my_combo.insertItem(2, "third thing")
        my_combo.insertItems(2, ["4","5","fourth thing"])
        #put combobox on the screen 
        self.layout().addWidget(my_combo)


        # create a button
        my_button = qtw.QPushButton("press me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)


        #show the app    
        self.show()

        def press_it():
            # add name to lable
            my_label.setText(f'You  picked  {my_combo.currentText()}')
            # show current text
            #my_label.setText(f'You  picked  {my_combo.currentText()}')
            #my_label.setText(f'You  picked  {my_combo.currentIndex()+1}')
            #my_label.setText(f'You  picked  {my_combo.currentData()}')


app = qtw.QApplication([])
mw = MainWindow()

#run the app

app.exec_()