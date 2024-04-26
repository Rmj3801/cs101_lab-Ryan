import turtle

class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    
    def draw_action(self):
        turtle.dot()
class Box(Point):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height
    
    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
class BoxFilled(Box):
    def __init__(self, x, y, width, height, color, fillcolor):
        super().__init__(x, y, width, height, color)
        self.fill_color = fill_color
    
    def draw(self):
        turtle.fillcolor(self.fill_color)
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()
class Circle(Point):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius
    
    def draw_action(self):
        turtle.circle(self.radius)
class CircleFilled(Circle):
    def __init__(self, x, y, radius, color, fill_color):
        super().__init__(x, y, radius, color)
        self.fill_color = fill_color
    
    def draw(self):
        turtle.fillcolor(self.fill_color)
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()
