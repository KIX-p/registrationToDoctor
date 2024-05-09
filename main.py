import random
import sys

from PyQt5.QtWidgets import QDialog, QApplication, QButtonGroup

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.ui.internistaradio)
        self.button_group.addButton(self.ui.pediatraradio)
        self.button_group.addButton(self.ui.dermatologradio)
        self.ui.reservationbutton.clicked.connect(self.reservation)


    def reservation(self):
        specjalizacja = self.button_group.checkedButton().text()
        wynik = self.ui.result
        iloscdni = random.randint(0, 14)
        if specjalizacja == "Internista" and self.ui.isPrivateReservationCheckBox.isChecked():
            wynik.setText("Pomyślnie zarezerwowano wizytę u internisty. Termin wizyty przepada za " + str(iloscdni) + " dni. Koszt wizyty to 200zł")
        elif specjalizacja == "Pediatra" and self.ui.isPrivateReservationCheckBox.isChecked():
            wynik.setText("Pomyślnie zarezerwowano wizytę u pediatry. Termin wizyty przepada za " + str(iloscdni) + " dni. Koszt wizyty to 200zł")
        elif specjalizacja == "Dermatolog" and self.ui.isPrivateReservationCheckBox.isChecked():
            wynik.setText("Pomyślnie zarezerwowano wizytę u dermatologa. Termin wizyty przepada za " + str(iloscdni) + " dni. Koszt wizyty to 200zł")
        else:
            wynik.setText("Pomyślnie zarezerwowano wizytę u " + specjalizacja + ". Termin wizyty przepada za " + str(random.randint(0, 1000)) + " dni. Koszt wizyty to 0zł")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

