import sdl2.sdlgfx

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
    :type isFilled: int

    :param color: The r, g, b values of the color of the circle.
    :type color: tuple
    """

class Circle:
    def __init__(self, window, x, y, radius, isFilled=True, color=(0, 0, 0)):
        self.window = window
        self.x = x
        self.y = y
        self.radius = radius
        self.isFilled = isFilled
        self.color = color

        # *parmas unpacks the tuple
        params = (window.renderer.renderer, x, y, radius, self.color[0], self.color[1], self.color[2], 255) 
        if isFilled:
            sdl2.sdlgfx.filledCircleRGBA(*params)
        else:
            sdl2.sdlgfx.circleRGBA(*params)