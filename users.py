"""User management module."""

from dataclasses import dataclass


@dataclass
class UserProfile:
    """Values that together describe a user."""

    name: str
    email: str
    age: int
    city: str
    role: str
    active: bool
    verified: bool


def make_user(profile):
    """Create a user record from a :class:`UserProfile`."""
    return {
        "name": profile.name,
        "email": profile.email,
        "age": profile.age,
        "city": profile.city,
        "role": profile.role,
        "active": profile.active,
        "verified": profile.verified,
    }
