"""Authentication module (part of a dependency cycle: auth -> billing -> auth)."""

import billing


def authenticate(user):
    """Authenticate a user, then check their billing standing."""
    if not user.get("token"):
        return False
    return billing.has_valid_subscription(user)


def get_account_status(user):
    return "active" if authenticate(user) else "locked"
