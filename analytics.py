"""Analytics module."""


def total(items):
    """Compute the total price of a list of items (duplicated in reporting.py)."""
    return sum(i.price for i in items)


def average(items):
    if not items:
        return 0
    return total(items) / len(items)
