import sdl2.ext
import sdl2.sdlgfx
class Rect:
    """
    Instantiate an object that draws a rectangle on the window.

    :param window: The window object.
    :type window: SDL_Window

    :param x1: The x position of the top-left corner of the rectangle.
    :type x1: int

    :param y1: The y position of the top-left corner of the rectangle.
    :type y1: int

    :param x2: The x position of the bottom-right corner of the rectangle.
    :type x2: int

    :param y2: The y position of the bottom-right corner of the rectangle.
    :type y2: int

    :param isFilled: Determines if the rectangle is filled or not.
    :type isFilled: bool

    :param color: The r, g, b values of the color of the rectangle.
    :type color: tuple
    """

    def __init__(self, window, x1, y1, x2, y2, isFilled, color=(0, 0, 0)):
        self.x1 = x1
        self.y1 = y1
        self.x2= x2
        self.y2 = y2
        self.color = color
        self.window = window
        self.isFilled = isFilled

        params = (window.renderer.renderer, self.x1, self.y1, self.x2, self.y2, sdl2.ext.Color(self.color[0], self.color[1], self.color[2]))
        sdl2.sdlgfx.boxColor(*params) if isFilled else sdl2.sdlgfx.rectangleColor(*params)