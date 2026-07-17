"""Reporting module."""


def total(items):
    """Compute the total price of a list of items (duplicated in analytics.py)."""
    return sum(i.price for i in items)


def summary(items):
    return {"count": len(items), "total": total(items)}
