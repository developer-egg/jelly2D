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
        self.window = sdl2.ext.Window(title, size=(width, height))

        self.window.show()

        self.processor = sdl2.ext.TestEventProcessor()
        self.processor.run(self.window)

        sdl2.ext.quit()
