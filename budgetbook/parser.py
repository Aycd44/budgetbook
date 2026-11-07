"""Read bank transaction exports into Transaction records."""

import csv
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

DATE_FORMATS = ("%Y-%m-%d", "%d/%m/%Y")


@dataclass(frozen=True)
class Transaction:
    when: date
    description: str
    amount: Decimal  # negative = money out, positive = money in
    category: str


def parse_date(text: str) -> date:
    text = text.strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Unrecognised date: {text!r}")


def parse_amount(text: str) -> Decimal:
    cleaned = text.strip().replace("$", "").replace(",", "")
    if cleaned.startswith("(") and cleaned.endswith(")"):
        cleaned = "-" + cleaned[1:-1]
    try:
        return Decimal(cleaned)
    except InvalidOperation as exc:
        raise ValueError(f"Unrecognised amount: {text!r}") from exc


def load_transactions(path: str | Path) -> list[Transaction]:
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            Transaction(
                when=parse_date(row["date"]),
                description=row["description"].strip(),
                amount=parse_amount(row["amount"]),
                category=(row.get("category") or "Uncategorised").strip() or "Uncategorised",
            )
            for row in reader
        ]
