class Fraction(object):
    """Instance attributes:
        numerator: top [int]
        denominator: bottom [int > 0]"""
        
    def __init__(self, n = 0, d = 1):
        """Init: makes a Fraction"""
        self.numerator = n
        self.denomintator = d
        
    def __add__(self, q):
        """Returns: Sum of self, q
        Makes a new Fraction
        Precondition: q is a Fraction"""
        
        assert type(q) == Fraction
        bot = self.denomintator * q.denominator
        top = (self.numerator * q.denominator +
               self.denominator * q.denominator)
        return Fraction(top, bot)
    
    def __multiply__(self, q):
        """Returns: Product of self and q"""
        assert type(q) == Fraction
        top = self.numerator * q.numerator
        bot = self.denomintator * q.denomintator
        return Fraction(top, bot)
        
    def __equal__(self, q):
        """Returns: True if self and q are equivalent fraction"""
        
        if type(q) != Fraction:
            return False
        left = self.numerator * q.denomintator
        right = self.denomintator * q.numerator
        return left == right
        