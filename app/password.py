"""Проверка сложности пароля."""

import re

MIN_LENGTH = 12
COMMON_PASSWORDS = {"password", "123456", "qwerty", "admin", "letmein"}


def check_password(password: str) -> list[str]:
    """Возвращает список проблем с паролем. Пустой список значит, что пароль хороший."""
    problems = []
    if len(password) < MIN_LENGTH:
        problems.append(f"короче {MIN_LENGTH} символов")
    if password.lower() in COMMON_PASSWORDS:
        problems.append("слишком распространённый")
    if not re.search(r"[A-ZА-ЯЁ]", password):
        problems.append("нет заглавной буквы")
    if not re.search(r"[a-zа-яё]", password):
        problems.append("нет строчной буквы")
    if not re.search(r"\d", password):
        problems.append("нет цифры")
    if not re.search(r"[^\w\s]", password):
        problems.append("нет спецсимвола")
    return problems


def is_strong(password: str) -> bool:
    """True, если у пароля нет ни одной проблемы."""
    return not check_password(password)
