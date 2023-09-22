import sys
import time
import pygetwindow as gw
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt
import threading
from PyQt5.QtWidgets import QHeaderView

# Initialize variables
current_window = None
start_time = None
app_data = {}
data_lock = threading.Lock()

class HistoryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a timer to update the active window
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_active_window)
        self.timer.start(1000)  # Check every 1 second

        self.setWindowTitle("History Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Create a table to display history
        self.history_table = QTableWidget(self)
        self.history_table.setColumnCount(3)
        self.history_table.setHorizontalHeaderLabels(["Time", "Activity", "Time Spent"])
        self.history_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        # Create a layout for the table
        layout = QVBoxLayout()
        layout.addWidget(self.history_table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_active_window(self):
        global current_window, start_time
        new_window = gw.getActiveWindow()

        if new_window != current_window:
            # Calculate the time spent on the previous window
            if current_window is not None:
                end_time = time.time()
                elapsed_time = end_time - start_time
                app_name = current_window.title

                with data_lock:
                    if app_name in app_data:
                        app_data[app_name] += elapsed_time
                    else:
                        app_data[app_name] = elapsed_time

                current_datetime = time.strftime("%Y-%m-%d %H:%M:%S")
                with open("TrackRecords.txt", "a") as file:
                    file.write(f"{current_datetime} - Time spent on {app_name}: {elapsed_time:.2f} seconds\n")

            current_window = new_window
            start_time = time.time()

        self.update_table()

    def update_table(self):
        self.history_table.setRowCount(len(app_data))
        row = 0
        for app, time_spent in app_data.items():
            current_datetime = time.strftime("%I:%M %p")
            self.history_table.setItem(row, 0, QTableWidgetItem(current_datetime))
            self.history_table.setItem(row, 1, QTableWidgetItem(f"{app}"))
            self.history_table.setItem(row, 2, QTableWidgetItem(f"{time_spent:.2f} seconds"))
            row += 1

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()

if __name__ == "__main__":
    current_window = gw.getActiveWindow()
    start_time = time.time()
    
    app = QApplication(sys.argv)
    window = HistoryApp()
    window.show()

    def track_app_time():
        while True:
            window.update_active_window()
            time.sleep(1)  # Check the active window every 1 second

    tracking_thread = threading.Thread(target=track_app_time)
    tracking_thread.daemon = True
    tracking_thread.start()

    sys.exit(app.exec_())
