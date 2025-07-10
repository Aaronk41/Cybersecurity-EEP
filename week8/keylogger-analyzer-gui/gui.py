from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QHBoxLayout
)
from parser import parse_log, filter_suspicious
from PyQt5.QtGui import QColor

class KeylogAnalyzerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keylogger Analyzer")
        self.resize(700, 500)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button = QPushButton("Open Keylogger Log")
        self.button.clicked.connect(self.load_file)
        self.layout.addWidget(self.button)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search...")
        self.search_input.textChanged.connect(self.search_table)
        search_layout.addWidget(QLabel("Filter:"))
        search_layout.addWidget(self.search_input)
        self.layout.addLayout(search_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Timestamp", "Key", "Flag"])
        self.layout.addWidget(self.table)

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt *.log *.csv)")
        if path:
            entries = parse_log(path)
            self.update_table(entries)

    def update_table(self, entries):
        self.table.setRowCount(len(entries))
        for row, (timestamp, key, flag) in enumerate(entries):
            self.table.setItem(row, 0, QTableWidgetItem(timestamp))
            self.table.setItem(row, 1, QTableWidgetItem(key))
            item = QTableWidgetItem(flag)
            if flag == "SUSPICIOUS":
                item.setForeground(QColor("red"))
            self.table.setItem(row, 2, item)

    def search_table(self, text):
        for row in range(self.table.rowCount()):
            match = False
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if text.lower() in item.text().lower():
                    match = True
            self.table.setRowHidden(row, not match)
