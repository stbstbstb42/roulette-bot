import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QCheckBox, QLabel, QPushButton
from PyQt5.QtChart import QChart, QLineSeries, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class AutoDBGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoDB v0.1")
        self.setGeometry(100, 100, 800, 600)

        # Create widgets
        self.strategy_dropdown = QComboBox(self)
        self.strategy_dropdown.setGeometry(20, 20, 200, 30)
        self.strategy_dropdown.addItems(["Strategy 1", "Strategy 2", "Strategy 3"])

        self.if_six_checkbox = QCheckBox("Use ifSixOrNot strategy", self)
        self.if_six_checkbox.setGeometry(240, 20, 200, 30)

        self.gain_label = QLabel("Gain:", self)
        self.gain_label.setGeometry(20, 70, 200, 30)

        self.roundgain_label = QLabel("Round Gain:", self)
        self.roundgain_label.setGeometry(20, 100, 200, 30)

        self.bet_label = QLabel("Bet:", self)
        self.bet_label.setGeometry(20, 130, 200, 30)

        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.setGeometry(20, 180, 100, 30)
        self.calculate_button.clicked.connect(self.calculate)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setGeometry(140, 180, 100, 30)
        self.clear_button.clicked.connect(self.clear)

        self.chart = QChart()
        self.chart.setTitle("Balance over time")
        self.chart.setGeometry(20, 250, 760, 300)

        self.series = QLineSeries()
        self.chart.addSeries(self.series)

        self.x_axis = QValueAxis()
        self.x_axis.setLabelFormat("%i")
        self.x_axis.setTitleText("Time")
        self.chart.addAxis(self.x_axis, Qt.AlignBottom)
        self.series.attachAxis(self.x_axis)

        self.y_axis = QValueAxis()
        self.y_axis.setLabelFormat("%.2f")
        self.y_axis.setTitleText("Balance")
        self.chart.addAxis(self.y_axis, Qt.AlignLeft)
        self.series.attachAxis(self.y_axis)

        # Set initial values
        self.balance = 100
        self.series.append(0, self.balance)

    #def calculate(self):
        # Insert your gain, roundgain and bet calculation here
        # Use self.strategy_dropdown.currentText() and self.if_six_checkbox.isChecked() to get the selected options
        # Update self.balance with the calculated balance
        # Update self.series with the new data point

    def clear(self):
        self.balance = 100
        self.series.clear()
        self.series.append(0, self.balance)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawLine(20, 220, 780, 220)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = AutoDBGUI()
    gui.show()
    sys.exit(app.exec_())