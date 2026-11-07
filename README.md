# budgetbook

Turn a bank CSV export into a simple monthly spending report.

## Usage

```bash
python -m budgetbook data/sample_transactions.csv 2026 1
```

The CSV needs `date`, `description`, `amount` and `category` columns. Dates can be `YYYY-MM-DD` or `DD/MM/YYYY`. Amounts are negative for money out and positive for money in; `$`, thousands separators and `(parentheses)` negatives are accepted.

## Tests

```bash
pip install pytest
pytest
```

## License

MIT
