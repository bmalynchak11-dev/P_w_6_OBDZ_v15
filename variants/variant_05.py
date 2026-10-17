"""
Варіант 15. NOT EXISTS: рядки без зв'язаних (облік обладнання)
Задача 5, набір 3
"""

VARIANT = 15


def query() -> str:
    return """
    SELECT d.name, d.parent_id
    FROM department AS d
    WHERE NOT EXISTS (
        SELECT 1
        FROM device AS dev
        WHERE dev.department_id = d.id
    );
    """