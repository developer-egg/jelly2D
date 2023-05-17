import sdl2.sdlgfx

class Circle:
    def __init__(self, window, x, y, radius, isFilled, color=(0, 0, 0)):
        self.window = window
        self.x = x
        self.y = y
        self.radius = radius
        self.isFilled = isFilled
        self.color = color

        if isFilled:
            sdl2.sdlgfx.filledCircleRGBA(window.renderer.renderer, x, y, radius, self.color[0], self.color[1], self.color[2], 255)
        else:
            sdl2.sdlgfx.circleRGBA(window.renderer.renderer, x, y, radius, self.color[0], self.color[1], self.color[2], 255)