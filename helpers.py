"""Helper utilities."""


def format_name(user):
    """Referenced helper: builds a display name."""
    return f"{user.get('first', '')} {user.get('last', '')}".strip()


def _unused(x):
    """Defined but never referenced anywhere in the codebase."""
    return x + 1


def _also_unused(a, b):
    """Another dead helper that nothing calls."""
    return a * b + 1
