"""Order processing module (compatibility re-export).

The order logic lives in :mod:`orders`. This module re-exports it so existing
``orders_copy.apply_discount`` callers keep working without holding a second,
drifting copy of the implementation.
"""

from orders import apply_discount, total

__all__ = ["apply_discount", "total"]
