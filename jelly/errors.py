class JellyInvalidOpacityException(Exception):
    def __init__(self, opacity):
        self.opacity = opacity
        super().__init__(
            f"Invalid opacity value: {opacity}\nHint: Opacity must be an integer between 0 and 100."
        )


class JellyInvalidColorException(Exception):
    def __init__(self, rgb):
        self.color = rgb
        super().__init__(
            f"Invalid color value: {rgb}\nHint: RGB values must be an integer between 0 and 255."
        )
