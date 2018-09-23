import shape
class Circle(shape):
    """Instance is a Circle @ x,y with radius"""
    
    def __init__(self,x,y,radius):
        self.radius = radius
        super().__init__(x, y)
    def __str__(self):
        return "Circle: Radius= " + str(self.radius) + " " + shape.__str__(self)
    def draw(self):