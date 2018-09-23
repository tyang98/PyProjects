class Shape():
    """Instance is shape @ x, y """
    def __init__(self, x, y):
        self.x = x
        self.y = y  
    
    def __str__(self):    
        return "Shape @ " +str(self.x) + ", " + str(self.y)  

    def __draw__(self):
        
        