import sys
import sdl2.ext

class Window:
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
