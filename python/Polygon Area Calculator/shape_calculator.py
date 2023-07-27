import math


class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        output = ""
        for i in range(0,self.height,1):
            output += "*"*self.width + "\n"
        return output

    def get_amount_inside(self, square):

        return math.floor(self.get_area()/square.get_area())

    def __str__(self):
        output = "Rectangle(width={}, height={})".format(self.width,self.height)
        # for i in range(0,self.height,1):
        #     output += "\n"+"*"*self.width
        return output


class Square(Rectangle):
    def __init__(self,side):
        self.side = side
        Rectangle.__init__(self,side,side)

    def set_width(self,width):
        self.side = width
        super().set_width(width)
        super().set_height(width)

    def set_height(self,height):
        self.side = height
        super().set_height(height)
        super().set_width(height)

    def set_side(self,side):
        self.side = side
        super().set_height(side)
        super().set_width(side)

    def __str__(self):
        output = "Square(side={})".format(self.side)
        return output
