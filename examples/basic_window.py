import jelly
import sdl2
import sdl2.ext
import sdl2.sdlgfx

# creates a 500 x 500 window titled "Hello, World!"
window = jelly.Window("Hello, World!", 500, 500)


# basic game loop to refresh to window
# eventually jelly may have its own game loop and event system
running = True

while running:
    events = sdl2.ext.get_events()

    for event in events:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break

    window.refresh()