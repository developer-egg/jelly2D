import sdl2.sdlgfx
from errors import JellyInvalidColorException, JellyInvalidOpacityException

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
    :type isFilled: bool

    :param color: The r, g, b values of the color of the oval.
    :type color: tuple
    """


class Oval:
    def __init__(
        self, window, x, y, width, height, isFilled=True, opacity=100, color=(0, 0, 0)
    ):
        if opacity < 0 or opacity > 100:
            raise JellyInvalidOpacityException(opacity)

        if not all(0 <= c <= 255 for c in color):
            raise JellyInvalidColorException(color)

        self.window = window

        self.x = x
        self.y = y

        # width and height are divided in half because pysdl takes in radius
        self.width = width // 2
        self.height = height // 2

        self.isFilled = isFilled
        self.opacity = round(255 * (opacity / 100))
        self.color = color

        window.shapes.append(self)

        params = (
            window.renderer.renderer,
            self.x,
            self.y,
            self.width,
            self.height,
            self.color[0],
            self.color[1],
            self.color[2],
            self.opacity,
        )

        sdl2.sdlgfx.filledEllipseRGBA(*params) if isFilled else sdl2.sdlgfx.ellipseRGBA(
            *params
        )
