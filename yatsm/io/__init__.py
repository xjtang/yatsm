""" YATSM IO module

.. todo::

   Include result file IO abstraction (:issue:`69`)

Contents:

    * :mod:`._util`: Collection of helper functions that ease common
      filesystem operations
"""
from ._api import get_readers, read_and_preprocess


__all__ = [
    'get_readers',
    'read_and_preproces'
]
