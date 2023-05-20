import sdl2.sdlgfx

"""
    Instantiate an object that draws a circle on the window.

    :param window: The window object.
    :type window: SDL_Window

    :param x: The x position of the center of the oval.
    :type x: int

    :param y: The y position of the center of the oval.
    :type y: int

    :param width: The width of the oval.
    :type width: int

    :param height: The height of the oval.
    :type height: int

    :param isFilled: Determines if the oval is filled or not.
    :type isFilled: int

    :param color: The r, g, b values of the color of the oval.
    :type color: tuple
    """

class Oval:
    def __init__(self, window, x, y, width, height, isFilled=True, color=(0, 0, 0)):
        self.window = window

        self.x = x
        self.y = y


        # width and height are divided in half because pysdl takes in radius
        self.width = width // 2
        self.height = height // 2

        self.isFilled = isFilled
        self.color = color

        params = (window.renderer.renderer, self.x, self.y, self.width, self.height, self.color[0], self.color[1], self.color[2], 255)

        sdl2.sdlgfx.filledEllipseRGBA(*params) if isFilled else sdl2.sdlgfx.ellipseRGBA(*params)