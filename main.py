from PyQt5.QtWidgets import QApplication
from logic import Logic

def main() -> None:
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec_()


if __name__ == "__main__":
    main()