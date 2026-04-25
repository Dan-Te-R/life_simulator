"""
Вспомогательный модуль utils.py
Функции логирования и валидации.
"""


def log_event(message: str) -> None:
    """Вывод события в лог."""
    print(f"[LOG] {message}")