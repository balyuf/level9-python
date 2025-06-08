#!/bin/env python3
# Decode Level 9 pictures
# Most of the code is adapted from the GS/DK Level 9 Interpreter
#
# Each subroutine starts with a header: nn | nl | ll
# nnn : the subroutine number ( 0x000 - 0x7ff )
# lll : the subroutine length ( 0x004 - 0x3ff )
#
# The first subroutine usually has the number 0x000.
# Each subroutine ends with 0xff.

from l9graphics import initGraphics, clearGraphics, showImage

# Load the picture file
# Graphics version   Resolution     Scale stack reset
# ---------------------------------------------------
# 2                  160 x 128            yes
# 3.1                160 x 96             yes
# 3.2                160 x 96             no
# 3.3                320 x 96             no
_graphicsVersion = 2
def setupPictures(filename, version = _graphicsVersion):
    global data, _graphicsVersion
    _graphicsVersion = version
    with open(filename, 'rb') as dataFile:
        data = bytearray(dataFile.read())
        dataFile.close()
    if _debug: print(f'+++ {filename}')

# Show a picture
def showPicture(picNumber, filename = None):
    global gintcolour, option, reflectflag, drawx, drawy, scale, picStack, scaleStack
    gintcolour = 3
    option = 0x80
    reflectflag = 0
    drawx = 0x1400
    drawy = 0x1400
    scale = 0x80
    picStack = []
    scaleStack = []
    if _mode == 0:
        return
    elif not _graphInited:
        initPictures()
    clearPictures()

    picture = _findPicture(data, picNumber)
    if picture is not None:
        if _debug: print(f'*** picture {picNumber}')
        address = _findPicture(data, 0)
        if address is not None:
            if _debug: print(f'0x{address:04x} (init) : ', end = '')
            _drawPicture(data, address) 
        if _debug: print(f'0x{picture:04x} (body) : ', end = '')
        _drawPicture(data, picture)
        if filename:
            filename = filename.replace("roms/", "pics/").replace(".pic", "")
            _processImage(f'{filename}-{picNumber}.png')
        else:
            _processImage(None)

def _findPicture(data, picNumber):
    address = 0
    while address < len(data) and data[address] != 0xff:
        number = ((data[address] << 4) + (data[address + 1] >> 4)) & 0x7ff
        length = ((data[address + 1] << 8) + (data[address + 2])) & 0x3ff
        if number == picNumber:
            return address
        address += length
    return None

def _drawPicture(data, picAddress):
    address = picAddress
    number = ((data[address] << 4) + (data[address + 1] >> 4)) & 0x7ff
    length = ((data[address + 1] << 8) + (data[address + 2])) & 0x3ff
    if _debug: print(f'number = 0x{number:03x}, length = 0x{length:03x}')
    address += 3
    while address < len(data):
        byte = data[address]
        if _debug: print(f'0x{address:04x} (0x{byte:02x}) : ', end = '')
        if (byte & 0xc0) != 0xc0:
            match (byte >> 6) & 0x03:
                case 0: address = _sdraw(data, byte, address)
                case 1: address = _smove(data, byte, address)
                case 2: address = _sgosub(data, byte, address)
        elif (byte & 0x38) != 0x38:
            match (byte >> 3) & 0x07:
                case 0: address = _draw(data, byte, address)
                case 1: address = _move(data, byte, address)
                case 2: address = _icolour(data, byte, address)
                case 3: address = _size(data, byte, address)
                case 4: address = _gintfill(data, byte, address)
                case 5: address = _gosub(data, byte, address)
                case 6: address = _reflect(data, byte, address)
        else:
            match byte & 0x07:
                case 0: address = _notimp(data, byte, address)
                case 1: address = _gintchgcol(data, byte, address)
                case 2: address = _notimp(data, byte, address)
                case 3: address = _amove(data, byte, address)
                case 4: address = _opt(data, byte, address)
                case 5: address = _restorescale(data, byte, address)
                case 6: address = _notimp(data, byte, address)
                case 7: address = _rts(data, byte, address)
        if address is None: return

def _scalex(x):
    return x >> (6 if _graphicsVersion < 3.3 else 5)

def _scaley(y):
    return 127 - (y >> 7) if _graphicsVersion == 2 else 95 - (((y >> 5) + (y >> 6)) >> 3)

def _newxy(x, y):
    global drawx, drawy
    drawx += (x * scale) & ~7
    drawy += (y * scale) & ~7

# sdraw instruction plus arguments are stored in an 8 bit word.
#       76543210
#       iixxxyyy
# where i is instruction code
#       x is x argument, high bit is sign
#       y is y argument, high bit is sign
def _sdraw(data, code, address):
    x = (code & 0x18) >> 3
    if code & 0x20:
        x = (x | 0xfc) - 0x100
    y = (code & 0x3) << 2
    if code & 0x4:
        y = (y | 0xf0) - 0x100

    if reflectflag & 2:
        x = -x
    if reflectflag & 1:
        y = -y

    x1 = drawx
    y1 = drawy
    _newxy(x, y)

    _drawline(_scalex(x1), _scaley(y1), _scalex(drawx), _scaley(drawy), gintcolour & 3, option & 3)
    if _debug: print(f'sdraw ({x1}, {y1}) - ({drawx}, {drawy}) colours ({gintcolour & 3}, {option & 3})')
    return address + 1

# smove instruction plus arguments are stored in an 8 bit word.
#       76543210
#       iixxxyyy
#  where i is instruction code
#        x is x argument, high bit is sign
#        y is y argument, high bit is sign
def _smove(data, code, address):
    x = (code & 0x18) >> 3
    if code & 0x20:
        x = (x | 0xfc) - 0x100
    y = (code & 0x3) << 2
    if code & 0x4:
        y = (y | 0xf0) - 0x100

    if reflectflag & 2:
        x = -x
    if reflectflag & 1:
        y = -y

    _newxy(x, y)
    if _debug: print(f'smove ({drawx}, {drawy})')
    return address + 1

def _sgosub(data, code, address):
    picNumber = code & 0x3f
    picture = _findPicture(data, picNumber)
    if picture is not None:
        scaleStack.append(scale)
        picStack.append(address + 1)
        address = picture + 2

    if _debug: print(f'sgosub 0x{picNumber:03x} (picture {picNumber} -> 0x{address + 1:04x})')
    return address + 1

# draw instruction plus arguments are stored in a 16 bit word.
#      FEDCBA9876543210
#      iiiiixxxxxxyyyyy
# where i is instruction code
#       x is x argument, high bit is sign
#       y is y argument, high bit is sign
def _draw(data, code, address):
    byte = data[address + 1]

    xy = (code << 8) + byte
    x = (xy & 0x3e0) >> 5
    if xy & 0x400:
        x = (x | 0xe0) - 0x100
    y = (xy & 0xf) << 2
    if xy & 0x10:
        y = (y | 0xc0) - 0x100

    if reflectflag & 2:
        x = -x
    if reflectflag & 1:
        y = -y

    x1 = drawx
    y1 = drawy
    _newxy(x, y)

    _drawline(_scalex(x1), _scaley(y1), _scalex(drawx), _scaley(drawy), gintcolour & 3, option & 3)
    if _debug: print(f'draw  ({x1}, {y1}) - ({drawx}, {drawy}) colours ({gintcolour & 3}, {option & 3})')
    return address + 2

# move instruction plus arguments are stored in a 16 bit word.
#      FEDCBA9876543210
#      iiiiixxxxxxyyyyy
# where i is instruction code
#       x is x argument, high bit is sign
#       y is y argument, high bit is sign
def _move(data, code, address):
    byte = data[address + 1]

    xy = (code << 8) + byte
    x = (xy & 0x3e0) >> 5
    if xy & 0x400:
        x = (x | 0xe0) - 0x100
    y = (xy & 0xf) << 2
    if xy & 0x10:
        y = (y | 0xc0) - 0x100

    if reflectflag & 2:
        x = -x
    if reflectflag & 1:
        y = -y

    _newxy(x, y)
    if _debug: print(f'move  ({drawx}, {drawy})')
    return address + 2

def _icolour(data, code, address):
    global gintcolour
    gintcolour = code & 3

    if _debug: print(f'fgcol  {gintcolour}')
    return address + 1

def _size(data, code, address):
    global scale, scaleStack
    sizetable = [ 0x02, 0x04, 0x06, 0x07, 0x09, 0x0c, 0x10 ]

    code &= 7
    if code:
        scale = (scale * sizetable[code - 1]) >> 3
        if scale >= 0x100:
            scale = 0xff
    else:
        scale = 0x80
        if _graphicsVersion <= 3.1:
            scaleStack = []

    if _debug: print(f'size   {code&7} -> scale {scale}')
    return address + 1

def _gintfill(data, code, address):
    if (code & 7) == 0:
        code = gintcolour
    else:
        code &= 3

    _fill(_scalex(drawx), _scaley(drawy), code & 3, option & 3)

    if _debug: print(f'fill  ({drawx}, {drawy}) colours ({code & 3}, {option & 3})')
    return address + 1

def _gosub(data, code, address):
    byte = data[address + 1]

    picNumber = ((code & 7) << 8) + byte;
    picture = _findPicture(data, picNumber)
    if picture is not None:
        scaleStack.append(scale)
        picStack.append(address + 2)
        address = picture + 1

    if _debug: print(f'gosub  0x{picNumber:03x} (picture {picNumber} -> 0x{address + 2:04x})')
    return address + 2

def _reflect(data, code, address):
    global reflectflag
    if code & 4:
        code &= 3
        code ^= reflectflag
    reflectflag = code

    if _debug: print(f'reflect {reflectflag}')
    return address + 1

def _gintchgcol(data, code, address):
    byte = data[address + 1]
    
    rc = (byte >> 3) & 3
    ac = byte & 7

    _setcolour(rc, ac)
    if _debug: print(f'chgcol {rc} = {ac}')
    return address + 2

def _amove(data, code, address):
    global drawx, drawy
    drawx = 0x40 * data[address + 1]
    drawy = 0x40 * data[address + 2]

    if _debug: print(f'amove ({drawx}, {drawy})')
    return address + 3

def _opt(data, code, address):
    global option
    byte = data[address + 1]

    option = byte
    if byte:
        option = (byte & 3) | 0x80

    if _debug: print(f'bgcol  {byte & 3} (opt {byte})')
    return address + 2

def _restorescale(data, code, address):
    if scaleStack:
        scale = scaleStack[-1]

    if _debug: print(f'restorescale -> scale {scale}')
    return address + 1

def _rts(data, code, address):
    global scale
    address = None
    if picStack:
        address = picStack.pop()
        if scaleStack:
            scale = scaleStack.pop()

    if _debug: print(f'return')
    return address

def _notimp(data, code, address):
    if _debug: print(f'notimp')
    return address + 1

# Graphical primitives to be implemented in backend
from PIL import Image

# plot a single dot
def _plot(x, y, fg, bg):
    if x < 0 or x >= image.size[0] or y < 0 or y >= image.size[1]:
        return

    if frameBuffer[x][y] == bg:
        frameBuffer[x][y] = fg

# Bresenham's line algorithm, as described by Wikipedia
def _drawline(x1, y1, x2, y2, fg, bg):
    steep = abs (y2 - y1) > abs (x2 - x1);

    if steep:
        tmp = x1
        x1 = y1
        y1 = tmp

        tmp = x2
        x2 = y2
        y2 = tmp

    delta_x = abs (x2 - x1)
    delta_y = abs (y2 - y1)
    err = 0
    delta_err = delta_y
    x = x1
    y = y1

    x_step = 1 if x1 < x2 else -1
    y_step = 1 if y1 < y2 else -1

    if steep:
        _plot(y, x, fg, bg)
    else:
        _plot(x, y, fg, bg)

    while x != x2:
        x += x_step
        err += delta_err

        if 2 * err > delta_x:
            y += y_step
            err -= delta_x

        if steep:
            _plot(y, x, fg, bg)
        else:
            _plot(x, y, fg, bg)

# As found in Bill Kendrick's TuxPaint
def _fill(x, y, fg, bg):
    if fg == bg:
        return

    if x < 0 or x >= image.size[0] or y < 0 or y >= image.size[1]:
        return

    if frameBuffer[x][y] != bg:
        return

    # Find left side, filling along the way

    left = x

    while left >= 0 and frameBuffer[left][y] == bg:
        frameBuffer[left][y] = fg
        left -= 1

    left += 1

    # Find right side, filling along the way

    right = x + 1

    while right < image.size[0] and frameBuffer[right][y] == bg:
        frameBuffer[right][y] = fg
        right += 1

    right -= 1

    for i in range(left, right + 1):
        if y - 1 >= 0 and frameBuffer[i][y - 1] == bg:
            _fill(i, y - 1, fg, bg)

        if y + 1 < image.size[1] and frameBuffer[i][y + 1] == bg:
            _fill(i, y + 1, fg, bg)

basePalette = [
    (0x00, 0x00, 0x00), # Black
    (0xFF, 0x00, 0x00), # Red
    (0x30, 0xE8, 0x30), # Green
    (0xFF, 0xFF, 0x00), # Yellow
    (0x00, 0x00, 0xFF), # Blue
    (0xA0, 0x68, 0x00), # Brown
    (0x00, 0xFF, 0xFF), # Cyan
    (0xFF, 0xFF, 0xFF)] # White
imagePalette = [ (0, 0, 0) ] * 4
def _setcolour(rc, ac):
    imagePalette[rc] = basePalette[ac]

_graphInited = False
_mode = 1
def initPictures(mode = _mode, version = _graphicsVersion):
    global image, pixels, frameBuffer, _graphInited, _mode, _graphicsVersion
    _mode = mode
    if mode == 0:
        image = None
        pixels = None
        frameBuffer = None
        _graphInited = False
    elif mode == 1:
        width = 160 if version < 3.3 else 320
        height = 96 if version > 2 else 128
        image = Image.new('RGB', (width, height), 'black')
        pixels = image.load()
        frameBuffer = [[0] * height for _ in range(width)]
        if not _debug:
            initGraphics(width, height)
        _graphicsVersion = version
        _graphInited = True

    clearPictures(mode)

def clearPictures(mode = _mode):
    if _mode == 1 and mode == _mode:
        if not _graphInited:
            initPictures()

        for i in range(image.size[0]): 
            for j in range(image.size[1]):
                frameBuffer[i][j] = 0

    if mode == 0:
        clearGraphics()

def _processImage(filename):
    for i in range(image.size[0]): 
        for j in range(image.size[1]):
            pixels[i, j] = imagePalette[frameBuffer[i][j]]

    if filename:
        image.save(filename, 'PNG')
    else:
        showImage(image)

# Decode all pictures in specified files
def _decodePictures(filenames, version = _graphicsVersion):
    for filename in filenames:
        setupPictures(filename, version)
        for p in range(0, 0x800):
            showPicture(p, filename)

_debug = False
if __name__ == "__main__":
    _debug = True
    import os
    from l9config import v1Configuration
    for game in v1Configuration:
        filename = v1Configuration[game]['filename'].replace('.dat', '.pic')
        version = v1Configuration[game]['version']
        if version == 3:
            version = 3.1
        if 'graphics' in v1Configuration[game]:
            version = v1Configuration[game]['graphics']
        if version >= 2 and os.path.isfile(filename):
            _decodePictures([ filename ], version)
