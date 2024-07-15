import sys
import constants as const
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QTextEdit, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Circuits Simulator")
        self.setGeometry(
            const.MainWindow.X,
            const.MainWindow.Y,
            const.MainWindow.WIDTH,
            const.MainWindow.HEIGHT)
        self.setFixedSize(const.MainWindow.WIDTH,
                          const.MainWindow.HEIGHT)
        
        self.netlist_text = QTextEdit(self)
        self.netlist_text.setReadOnly(True)
        self.netlist_text.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.netlist_text.setFont(QFont("Times", const.MainWindow.NETLIST_TEXT_TEXT_SIZE))
        self.netlist_text.setGeometry(const.MainWindow.NETLIST_TEXT_X,
                                      const.MainWindow.NETLIST_TEXT_Y,
                                      const.MainWindow.NETLIST_TEXT_WIDTH,
                                      const.MainWindow.NETLIST_TEXT_HEIGHT)

        self.netlist_line_edit = QTextEdit(self)
        self.netlist_line_edit.setFont(QFont("Times", const.MainWindow.NETLIST_TEXT_SIZE))
        self.netlist_line_edit.setPlaceholderText("Enter your netlist: ")
        self.netlist_line_edit.setGeometry(const.MainWindow.NETLIST_LE_X,
                                      const.MainWindow.NETLIST_LE_Y,
                                      const.MainWindow.NETLIST_LE_WIDTH,
                                      const.MainWindow.NETLIST_LE_HEIGHT)

        self.append_btn = QPushButton("Append", self)
        self.append_btn.setFont(QFont("Times", const.MainWindow.APPEND_TEXT_SIZE))
        self.append_btn.clicked.connect(self.append_to_text)
        self.append_btn.setGeometry(const.MainWindow.APPEND_BUTTON_X,
                        const.MainWindow.APPEND_BUTTON_Y,
                        const.MainWindow.APPEND_BUTTON_WIDTH,
                        const.MainWindow.APPEND_BUTTON_HEIGHT)
        
        self.push_up_btn = QPushButton("Push Up", self)
        self.push_up_btn.setFont(QFont("Times", const.MainWindow.PUSH_UP_BUTTON_TEXT_SIZE))
        self.push_up_btn.clicked.connect(self.push_to_text)
        self.push_up_btn.setGeometry(const.MainWindow.PUSH_UP_BUTTON_X,
                                     const.MainWindow.PUSH_UP_BUTTON_Y,
                                     const.MainWindow.PUSH_UP_BUTTON_WIDTH,
                                     const.MainWindow.PUSH_UP_BUTTON_HEIGHT)

        self.push_down_btn = QPushButton("Push Down", self)
        self.push_down_btn.setFont(QFont("Times", const.MainWindow.PUSH_DOWN_BUTTON_TEXT_SIZE))
        self.push_down_btn.clicked.connect(self.pull_from_text)
        self.push_down_btn.setGeometry(const.MainWindow.PUSH_DOWN_BUTTON_X,
                                     const.MainWindow.PUSH_DOWN_BUTTON_Y,
                                     const.MainWindow.PUSH_DOWN_BUTTON_WIDTH,
                                     const.MainWindow.PUSH_DOWN_BUTTON_HEIGHT)

    def push_to_text(self):
        self.netlist_text.setText(self.netlist_line_edit.toPlainText())
        self.netlist_line_edit.setText("")

    def pull_from_text(self):
        self.netlist_line_edit.setText(self.netlist_text.toPlainText())

    def append_to_text(self):
        if len(self.netlist_text.toPlainText()) == 0:
            self.push_to_text()
        elif self.netlist_line_edit.toPlainText() == "":
            pass
        else:
            curr_text = self.netlist_text.toPlainText()
            self.netlist_text.setText(curr_text + "\n" + self.netlist_line_edit.toPlainText())
            self.netlist_line_edit.setText("")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())