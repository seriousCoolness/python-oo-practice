"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def generate(self):
        """Returns the next sequential number."""
        self.current += 1
        return self.current

    def reset(self):
        """Resets to the initial value."""
        self.current = self.reset

