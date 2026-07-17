"""User management module."""

from dataclasses import asdict, dataclass


@dataclass
class UserProfile:
    """Grouped attributes that together describe a user."""

    name: str
    email: str
    age: int
    city: str
    role: str
    active: bool
    verified: bool


def make_user(profile):
    """Create a user record from a grouped :class:`UserProfile`."""
    return asdict(profile)
