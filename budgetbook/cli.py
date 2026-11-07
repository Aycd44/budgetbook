"""Command line entry point: python -m budgetbook FILE YEAR MONTH"""

import argparse

from .parser import load_transactions
from .report import format_report, month_report


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Monthly spending report from a bank CSV export.")
    parser.add_argument("csv_file")
    parser.add_argument("year", type=int)
    parser.add_argument("month", type=int)
    args = parser.parse_args(argv)

    transactions = load_transactions(args.csv_file)
    spending = month_report(transactions, args.year, args.month)
    print(format_report(args.year, args.month, spending))


if __name__ == "__main__":
    main()
