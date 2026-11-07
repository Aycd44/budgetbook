from datetime import date
from decimal import Decimal

from budgetbook.parser import Transaction
from budgetbook.report import format_report, month_report


def tx(day, amount, category):
    return Transaction(day, "test", Decimal(amount), category)


def test_month_report_sums_spending_per_category():
    transactions = [
        tx(date(2026, 3, 1), "-10.00", "Groceries"),
        tx(date(2026, 3, 9), "-5.50", "Groceries"),
        tx(date(2026, 3, 12), "-40.00", "Utilities"),
    ]
    assert month_report(transactions, 2026, 3) == {
        "Groceries": Decimal("15.50"),
        "Utilities": Decimal("40.00"),
    }


def test_income_is_not_spending():
    transactions = [tx(date(2026, 3, 15), "2000.00", "Income")]
    assert month_report(transactions, 2026, 3) == {}


def test_format_report_total():
    text = format_report(2026, 3, {"Groceries": Decimal("15.50"), "Utilities": Decimal("40.00")})
    assert "Total                  55.50" in text
