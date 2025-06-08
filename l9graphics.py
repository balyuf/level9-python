#!/bin/env python3

import os, sys

WIDTH  = 512
HEIGHT = 218

def showImage(image):
    import sdl2.ext
    if not _graphInited:
        initGraphics()

    surface = sdl2.ext.window.Window.get_surface(_window)
    sdl2.ext.fill(surface, (0, 0, 0))
    _window.show()

    surface = sdl2.ext.image.pillow_to_surface(image)
    sprite = _factory.from_surface(surface)

    w, h = image.size
    width, height = _window.size
    x = (width - w) // 2
    y = (height - h) // 2

    sprite.position = x, y
    _renderer.render(sprite)

_graphInited = False
def initGraphics(width = WIDTH, height = HEIGHT):
    global _graphInited
    if not _graphInited:
        global _window, _renderer, _factory
        print('[Initializing graphics subsystem ... ', end='', flush=True)
        import sdl2.ext
        print('done]')
        sdl2.ext.init()
        width, height = WIDTH, HEIGHT # Don't make the window too small
        _window = sdl2.ext.Window("Level 9 graphics", size=(width, height), flags = sdl2.SDL_WINDOW_SHOWN)
        _factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        _renderer = _factory.create_sprite_render_system(_window)
        _graphInited = True

def clearGraphics():
    if _graphInited:
        _window.hide()

def _signal_handler(signum, frame):
    sys.exit(0)

_debug = False
if __name__ == "__main__":
    _debug = True

    import signal
    signal.signal(signal.SIGINT, _signal_handler)

    initGraphics()

    import sdl2.ext
    _window.show()
    pics = sdl2.ext.Resources(__file__, "pics/knight-orc")
    sprite = _factory.from_image(pics.get_path("30.png"))
    sprite.position = 96, 17
    _renderer.render(sprite)

    processor = sdl2.ext.TestEventProcessor()
    processor.run(_window)
    sdl2.ext.quit()
