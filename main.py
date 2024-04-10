import sys

from src.app_window import MainApp
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)

    # Load the style sheet
    with open('QTinterface/styling/stylings.qss', 'r') as f:
        style = f.read()
        app.setStyleSheet(style)

    main = MainApp()
    main.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()