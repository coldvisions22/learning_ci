import pytest

from app.password import check_password, is_strong


def test_strong_password_has_no_problems():
    assert check_password("Str0ng!Passw0rd") == []
    assert is_strong("Str0ng!Passw0rd")


def test_short_password():
    assert "короче 12 символов" in check_password("Ab1!")


def test_common_password():
    assert "слишком распространённый" in check_password("qwerty")
    assert not is_strong("qwerty")


@pytest.mark.parametrize(
    ("password", "problem"),
    [
        ("str0ng!password", "нет заглавной буквы"),
        ("STR0NG!PASSWORD", "нет строчной буквы"),
        ("Strong!Password", "нет цифры"),
        ("Str0ngPassword1", "нет спецсимвола"),
    ],
    ids=["no-upper", "no-lower", "no-digit", "no-special"],
)
def test_missing_character_class(password, problem):
    assert problem in check_password(password)
