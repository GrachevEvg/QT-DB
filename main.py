import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from ui_database_loader import Ui_MainWindow


class DatabaseLoaderApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Подключаем кнопку
        self.btn_load_db.clicked.connect(self.load_database)

        # Инициализируем модель для TableView
        self.model = None

    def load_database(self):
        # Открываем диалог выбора файла
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open SQLite Database", "", "SQLite Databases (*.db *.sqlite)"
        )

        if file_path:
            # Подключаемся к базе данных
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(file_path)

            if not db.open():
                print("Error: Could not open database.")
                return

            # Создаем модель и привязываем к TableView
            self.model = QSqlTableModel()
            # Указываем таблицу для отображения
            self.model.setTable("employees")
            self.model.select()

            self.tableView.setModel(self.model)
            self.tableView.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DatabaseLoaderApp()
    window.show()
    sys.exit(app.exec_())
