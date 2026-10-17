from conftest import load
from pgutil import Db
from schemas import SCHEMAS


def test_my_case():
    db = Db()
    try:
        # Схема 3 (облік обладнання)
        db.run(SCHEMAS[3])

        # Перевірка на початкових даних: очікується 3 порожніх підрозділи
        cols, rows = db.query(load(5).query())
        assert len(rows) == 3

        # Додаємо підрозділ без зазначення id (PostgreSQL згенерує його автоматично)
        db.run(
            "INSERT INTO department (name, parent_id) VALUES ('Новий тестовий відділ', NULL);"
        )

        # Перевірка після додавання нового порожнього підрозділу
        cols, rows = db.query(load(5).query())
        assert len(rows) == 4
    finally:
        db.close()