import sys
import csv
from qtpy import QtWidgets, QtGui

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Studierendenverwaltung")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.readCsvFile(r'C:\Users\JodaBook\Documents\Python\Python\QT_App\students.csv')
        self.ui.newEntryButton.clicked.connect(self.onNewEntry)
        self.ui.saveButton.clicked.connect(self.onSave)

    def onSave(self):
        with open(r'C:\Users\JodaBook\Documents\Python\Python\QT_App\students.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",", quotechar='"')

            rows = self.ui.studentsTable.rowCount()
            for i in range(0, rows):
                rowContent = [
                    self.ui.studentsTable.item(i, 0).text(),
                    self.ui.studentsTable.item(i, 1).text(),
                    self.ui.studentsTable.item(i, 2).text()
                ]
                writer.writerow(rowContent)

    def onNewEntry(self):
        row = self.ui.studentsTable.rowCount()
        self.ui.studentsTable.insertRow(row)

        self.ui.studentsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(""))
        self.ui.studentsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(""))
        self.ui.studentsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(""))

        cell = self.ui.studentsTable.item(row, 0)
        self.ui.studentsTable.editItem(cell)

    def readCsvFile(self, filename):
        self.ui.studentsTable.setRowCount(0)
        with open(filename, "r", newline='', encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for line in reader:
                row = self.ui.studentsTable.rowCount()
                self.ui.studentsTable.insertRow(row)

                self.ui.studentsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.studentsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.studentsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(line[2]))




window = MainWindow()

window.show()

sys.exit(app.exec_())
