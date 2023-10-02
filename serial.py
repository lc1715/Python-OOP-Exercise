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
    
    Attributtes
    ___________

    start: int
    original starting serial number that will increment by 1

    original_start_num: int
    original starting serial number
    """



    def __init__(self, start):
        """
        Begin to generate the first serial number
        """
        self.start = start
        self.original_serial_num = start

    def __repr__(self):
        """
        Show representation of generator
        """
        return f"<SerialGenerator original_serial_num={self.original_serial_num} start={self.start}>" 


    def generate(self):
        """
        increment the original starting serial number by 1
        """ 
        n = self.start 
        self.start += 1
        return n

    def reset(self):
        """
        resets the incremented serial number back to the original serial number
        """
        self.start = self.original_serial_num
        return self.start


