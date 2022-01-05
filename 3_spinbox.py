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

        my_label.setFont(qtg.QFont("helvetica",24))

        self.layout().addWidget(my_label)


        #create an spin box
        my_spin = qtw.QSpinBox(self, value= 10, maximum=100, minimum= 0, singleStep= 20,
            prefix="سفارش شما ",suffix=" عدد")
        ##### in Doublespinbox, you can use float number 

        #change the font size of spinbox

        my_spin.setFont(qtg.QFont("helvetica",18))
      
        #put combobox on the screen 
        self.layout().addWidget(my_spin)


        # create a button
        my_button = qtw.QPushButton("press me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)


        #show the app    
        self.show()

        def press_it():
            # add name to lable
            my_label.setText(f'You  picked  #{my_spin.value()} order!')
            

app = qtw.QApplication([])
mw = MainWindow()

#run the app

app.exec_()