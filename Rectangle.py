class Rectangle:

  def __init__(self, x, y, h, w):
    self.x = max(0, x)
    self.y = max(0, y)
    self.h = max(0, h)
    self.w = max(0, w)
"""
Sets instance variables to the x, y, height, and width.
"""

  def __str__(self):
    s = "(x: {}, y: {}), width: {}, height: {}"
    
    return s.format(self.x, self.y, self.h, self.w)
"""
Pulls the string from rectangle and returns it.
"""