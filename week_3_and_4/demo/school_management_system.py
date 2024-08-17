from PyQt6.QtWidgets import QMainWindow,QPushButton,QLabel,QLineEdit,QApplication
import sys
import student

class EntryPoint(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1350,700)
        
        self.app_components()
        self.show()

    def app_components(self):
        self.title_of_application=QLabel("Unn School Management System",self)
        self.title_of_application.setGeometry(400,0,700,80)
        self.title_of_application.setStyleSheet("font-size:40px;")
        self.students_component()
        
    def students_component(self):
        student_object=student.MechStudents("Christian Kelechi Eze","2018/123456","Graduate","5.0")
        
        self.full_name=QLabel(student_object.belong_to()+" managed by Unn Vc",self)
        self.full_name.setGeometry(300,200,600,80)
        
       
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=EntryPoint()
    sys.exit(app.exec())
