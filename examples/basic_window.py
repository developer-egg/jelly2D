# Add this to each example, not sure how make this simpler
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
######

import jelly
import sdl2
import sdl2.ext
import sdl2.sdlgfx

# creates a 500 x 500 window titled "Hello, World!"
window = jelly.Window("Hello, World!", 500, 500)

# basic game loop to refresh to window
# eventually jelly may have its own game loop and event system
running = True

# shapes should not be inside the game loop for now

while running:
    events = sdl2.ext.get_events()

    for event in events:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break   

    window.refresh()