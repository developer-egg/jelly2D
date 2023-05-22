import sys
import sdl2.ext


class Window:
    """
    Instantiate a game window.

    :param title: The title of the window.
    :type title: str

    :param width: The width of the window.
    :type width: int

    :param height: The height of the window.
    :type height: int
    """

    def __init__(self, title, width, height):
        self.width = width
        self.height = height
        self.title = title

        sdl2.ext.init()

        # sdl_window should be used when accessing sdl window methods
        self.sdl_window = sdl2.ext.Window(self.title, size=(self.width, self.height))

        self.sdl_window.show()

        # fill the background white
        sdl2.ext.fill(self.sdl_window.get_surface(), sdl2.ext.Color(255, 255, 255))

        # renderer must be made using the window surface, not the window itself
        self.renderer = sdl2.ext.renderer.Renderer(self.sdl_window.get_surface())
        
        self.shapes = []

    def refresh(self):
        self.renderer.clear(sdl2.SDL_Color(255, 255, 255))

        for shape in self.shapes:
            shape.draw()

        self.sdl_window.refresh()
