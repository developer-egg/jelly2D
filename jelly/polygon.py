import ctypes
import sdl2.sdlgfx

"""
    Instantiate an object that draws a polygon on the window.

    :param window: The window object.
    :type window: SDL_Window

    :param isFilled: Determines if the polygon is filled or not.
    :type isFilled: bool

    :param opacity: Opacity of the polygon 0 - 100
    :type opacity: int

    :param color: The r, g, b values of the color of the polygon.
    :type color: tuple

    :param points: List of tuples (x, y), which are the x,y points of the polygon
    :type points: tuple
"""


class Polygon:
    def __init__(self, window, isFilled=True, opacity=100, color=(0, 0, 0), *points):
        self.window = window
        self.isFilled = isFilled
        self.color = color
        self.opacity = round(255 * (opacity / 100))
        self.points = points

        x_coords = []
        y_coords = []

        for point in self.points:
            x_coords.append(point[0])
            y_coords.append(point[1])

        vx = (ctypes.c_int16 * len(x_coords))(*x_coords)
        vy = (ctypes.c_int16 * len(y_coords))(*y_coords)

        params = (window.renderer.renderer, vx, vy, len(self.points),
                  self.color[0], self.color[1], self.color[2], self.opacity)

        sdl2.sdlgfx.filledPolygonRGBA(
            *params) if isFilled else sdl2.sdlgfx.aapolygonRGBA(*params)
