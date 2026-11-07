"""Summarise transactions into monthly spending reports."""

from collections import defaultdict
from decimal import Decimal

from .parser import Transaction


def spending_by_month(transactions: list[Transaction]) -> dict[int, dict[str, Decimal]]:
    """Return {month: {category: amount spent}} for money going out."""
    summary: dict[int, dict[str, Decimal]] = defaultdict(lambda: defaultdict(Decimal))
    for tx in transactions:
        if tx.amount < 0:
            summary[tx.when.month][tx.category] += -tx.amount
    return {month: dict(cats) for month, cats in summary.items()}


def month_report(transactions: list[Transaction], year: int, month: int) -> dict[str, Decimal]:
    """Spending per category for one calendar month."""
    return spending_by_month(transactions).get(month, {})


def format_report(year: int, month: int, spending: dict[str, Decimal]) -> str:
    lines = [f"Spending for {year}-{month:02d}", "-" * 28]
    for category, amount in sorted(spending.items(), key=lambda item: -item[1]):
        lines.append(f"{category:<18}{amount:>10.2f}")
    lines.append("-" * 28)
    lines.append(f"{'Total':<18}{sum(spending.values(), Decimal(0)):>10.2f}")
    return "\n".join(lines)
