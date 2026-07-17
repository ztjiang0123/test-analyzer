"""Invoice generation module (compatibility re-export).

The invoice logic lives in :mod:`invoices`. This module re-exports it so
existing ``invoices_copy.build_invoice`` callers keep working without holding a
second, drifting copy of the implementation.
"""

from invoices import build_invoice, total

__all__ = ["build_invoice", "total"]
