from decimal import Decimal
from datetime import date

import pytest

from budgetbook.parser import parse_amount, parse_date


def test_parse_iso_date():
    assert parse_date("2026-01-15") == date(2026, 1, 15)


def test_parse_day_first_date():
    assert parse_date("27/01/2026") == date(2026, 1, 27)


def test_parse_bad_date():
    with pytest.raises(ValueError):
        parse_date("Jan 15")


@pytest.mark.parametrize(
    "text, expected",
    [
        ("-142.18", Decimal("-142.18")),
        ("2,450.00", Decimal("2450.00")),
        ("$15.99", Decimal("15.99")),
        ("(61.25)", Decimal("-61.25")),
    ],
)
def test_parse_amount(text, expected):
    assert parse_amount(text) == expected
