from PyQt5.QtWidgets import QMainWindow
from gui2 import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file_name = "results.csv"
        
        from PyQt5.QtWidgets import QButtonGroup
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(self.radio_button)
        self.buttonGroup.addButton(self.radio_button_2)

        """Ai was used for the following two lines."""
        with open(self.file_name, "w", newline="") as file:
            pass

        self.button_name.clicked.connect(lambda: self.submit())


    def submit(self) -> None:
        """Submit a vote."""
        voter_id = self.input_name.text().strip()
        candidate = ""


        if self.radio_button.isChecked():
            candidate = "Jane"

        elif self.radio_button2.isChecked():
            candidate = "John"

        # --- Validation ---
        try:
            if voter_id == "":
                raise ValueError("Enter ID")

            if not voter_id.isdigit():
                self.show_error("ID must be numbers only")
                return

            if len(voter_id) != 6:
                raise ValueError("ID must be 6 digits")

        except ValueError as error:
            self.show_error(str(error))
            return

        except TypeError:
            self.show_error("Invalid ID type")
            return

        if candidate == "":
            self.show_error("Select a candidate")
            return

        if self.already_voted(voter_id):
            self.show_error("Already Voted")
            return

        # --- Save vote ---
        try:
            with open(self.file_name, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([voter_id, candidate])

            """Ai was used for the following two lines."""
            self.label_name6.setStyleSheet("color: white;")
            self.label_name6.setText(f"Vote submitted for {candidate}")

            self.input_name.clear()
            self.buttonGroup.setExclusive(False)
            self.radio_button.setChecked(False)
            self.radio_button2.setChecked(False)
            self.buttonGroup.setExclusive(True)

            self.show_results()

        except:
            self.show_error("Could not save file")

    def already_voted(self, voter_id: str) -> bool:
        """Check if ID already voted."""
        try:
            with open(self.file_name, "r", newline="") as file:
                reader = csv.reader(file)

                for row in reader:
                    if len(row) > 0 and row[0] == voter_id:
                        return True

        except FileNotFoundError:
            return False

        return False

    def show_results(self) -> None:
        """Show vote totals."""
        john = 0
        jane = 0

        try:
            with open(self.file_name, "r", newline="") as file:
                reader = csv.reader(file)

                for row in reader:
                    if len(row) > 1:
                        if row[1] == "John":
                            john += 1
                        elif row[1] == "Jane":
                            jane += 1

        except FileNotFoundError:
            pass

        total = john + jane

        self.input_name2.setText(
            f"John: {john}, Jane: {jane}, Total: {total}"
        )

        """Ai was used for this part"""
    def show_error(self, message: str) -> None:
        """Show error message in red."""
        self.label_name6.setStyleSheet("color: red;")
        self.label_name6.setText(message)
