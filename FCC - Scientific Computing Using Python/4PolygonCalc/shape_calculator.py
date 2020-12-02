class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2*(self.height+self.width)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        
        pict = ('*'*self.width+'\n')*self.height
        
        return pict
    
    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)
    
    def get_amount_inside(self, other):
        return (self.width//other.width)*(self.height//other.height)
    
class Square(Rectangle):
        
    def __init__(self, side_length):
        Rectangle.__init__(self, side_length, side_length)
        
    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length
        
    def set_width(self, side_length):
        self.width = side_length
        self.height = side_length
        
    def set_height(self, side_length):
        self.width = side_length
        self.height = side_length
            
    def __str__(self):
        return 'Square(side={})'.format(self.width)
        
        