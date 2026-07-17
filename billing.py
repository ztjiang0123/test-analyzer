"""Billing module (part of a dependency cycle: billing -> auth -> billing)."""

import auth


def has_valid_subscription(user):
    """Check whether a user has a valid, paid subscription."""
    return user.get("plan") in {"pro", "enterprise"}


def charge(user, amount):
    """Charge a user, but only if they are authenticated first."""
    if not auth.authenticate(user):
        return False
    return {"user": user.get("id"), "charged": amount}
