import sqlite3


def create_database():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # Создаем таблицу "departments"
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        budget REAL
    )
    """)

    # Создаем таблицу "employees"
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments (id)
    )
    """)

    # Добавляем тестовые данные
    cursor.execute(
        "INSERT INTO departments (name, budget) VALUES ('IT', 100000)")
    cursor.execute(
        "INSERT INTO departments (name, budget) VALUES ('HR', 50000)")

    cursor.execute(
        "INSERT INTO employees (name, position, department_id) VALUES ('Alice', 'Developer', 1)")
    cursor.execute(
        "INSERT INTO employees (name, position, department_id) VALUES ('Bob', 'Manager', 2)")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database 'example.db' created with tables 'departments' and 'employees'.")
