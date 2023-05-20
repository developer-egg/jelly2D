import sdl2.sdlgfx
from jelly.errors import JellyInvalidColorException, JellyInvalidOpacityException

"""
    Instantiate an object that draws a circle on the window.

    :param window: The window object.
    :type window: SDL_Window

    :param x: The x position of the center of the circle.
    :type x: int

    :param y: The y position of the center of the circle.
    :type y: int

    :param radius: The radius of the circle.
    :type radius: int

    :param isFilled: Determines if the circle is filled or not.
    :type isFilled: bool

    :param color: The r, g, b values of the color of the circle.
    :type color: tuple
    """


class Circle:
    def __init__(
        self, window, x, y, radius, isFilled=True, opacity=100, color=(0, 0, 0)
    ):
        if opacity < 0 or opacity > 100:
            raise JellyInvalidOpacityException(opacity)

        if not all(0 <= c <= 255 for c in color):
            raise JellyInvalidColorException(color)

        self.window = window
        self.x = x
        self.y = y
        self.radius = radius
        self.isFilled = isFilled
        self.color = color
        self.opacity = round(255 * (opacity / 100))

        params = (
            window.renderer.renderer,
            x,
            y,
            radius,
            self.color[0],
            self.color[1],
            self.color[2],
            opacity,
        )
        sdl2.sdlgfx.filledCircleRGBA(*params) if isFilled else sdl2.sdlgfx.aacircleRGBA(
            *params
        )
