import sdl2.ext

class Rect:
    """
    Instantiate an object that draws a rectangle on the window.

    :param window: The window object.
    :type window: SDL_Window

    :param x: The x position of the top-left corner of the rectangle.
    :type x: int

    :param y: The y position of the top-left corner of the rectangle.
    :type y: int

    :param width: The width of the rectangle.
    :type width: int

    :param height: The height of the rectangle.
    :type height: int

    :param color: The r, g, b values of the color of the square.
    :type color: tuple
    """

    def __init__(self, window, x, y, width, height, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.window = window

        sdl2.ext.draw.fill(window.sdl_window.get_surface(), sdl2.ext.Color(self.color[0], self.color[1], self.color[2]), (self.x, self.y, self.width, self.height))