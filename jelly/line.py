import sdl2.sdlgfx

class Line:
    """
    Instantiate an object that draws a line on the window.

    :param window: The window object.
    :type window: SDL_Window

    :param x1: The x position of the first endpoint of the line.
    :type x1: int

    :param y1: The y position of the first endpoint of the line.
    :type y1: int

    :param x2: The x position of the second endpoint of the line.
    :type x2: int

    :param y2: The y position of the second endpoint of the line.
    :type y2: int

    :param color: The r, g, b values of the color of the line.
    :type color: tuple
    """

    def __init__(self, window, x1, y1, x2, y2, width=1, color=(255, 255, 255)):
        self.window = window
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.width = width

        self.color = color

        sdl2.sdlgfx.thickLineColor(window.renderer.renderer, x1, y1, x2, y2, width, sdl2.ext.Color(self.color[0], self.color[1], self.color[2]))