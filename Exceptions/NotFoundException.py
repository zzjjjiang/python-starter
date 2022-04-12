#
# File: NotFoundException.py
# Auth: Martin Burolla
# Date: 2/25/2021
# Desc: Thrown for all types of errors where something could not be found.
#

class NotFoundException(Exception):
    """Raised when something could not be found."""

    def __init__(self, message):
      self.message = message
      super().__init__(self.message)
