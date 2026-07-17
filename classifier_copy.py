"""Code classification module (compatibility re-export).

The classification logic lives in :mod:`classifier`. This module re-exports it
so existing ``classifier_copy.classify`` callers keep working without holding a
second, drifting copy of the implementation.
"""

from classifier import classify

__all__ = ["classify"]
