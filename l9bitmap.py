#!/bin/env python3
# Decode Level 9 bitmaps
# Most of the code is adapted from the GS/DK Level 9 Interpreter

import os, sys
from PIL import Image
from l9graphics import initGraphics, clearGraphics, showImage
from enum import Enum
class B(Enum):
    NO_BITMAPS    = 0,
    AMIGA_BITMAPS = 1,
    PC1_BITMAPS   = 2,
    PC2_BITMAPS   = 3,
    C64_BITMAPS   = 4,
    BBC_BITMAPS   = 5,
    CPC_BITMAPS   = 6,
    MAC_BITMAPS   = 7,
    ST1_BITMAPS   = 8,
    ST2_BITMAPS   = 9

class Bitmap:
    def __init__(self, x, y):
        self.width = x
        self.height = y
        self.npalette = 0
        self.palette = [0] * 32
        self.bitmap = [[0] * y for _ in range(x)]
        global image, pixels
        image = Image.new('RGB', (x, y), 'black')
        pixels = image.load()

MAX_BITMAP_WIDTH  = 512
MAX_BITMAP_HEIGHT = 218

def setupBitmap(dir):
    global _graphicsDir, _bitmapType
    _graphicsDir = dir
    _bitmapType = _bitmap_detect(_graphicsDir)
    if _bitmapType == B.NO_BITMAPS:
        return False
    else:
        return True

_graphInited = False
_mode = 2
def initBitmap(mode = _mode):
    global _graphInited, _mode
    _mode = mode
    if mode == 0:
        image = None
        pixels = None
        _bitmap = None
        _bitmapType = B.NO_BITMAPS
        _graphInited = False
    elif mode == 2:
        if not _debug:
            initGraphics()
        _graphInited = True

    clearBitmap(mode)

def clearBitmap(mode = _mode):
    if _mode == 2 and mode == _mode:
        if not _graphInited:
            initBitmap()

    if mode == 0:
        clearGraphics()

def showBitmap(pic, x, y):
    if _mode == 0:
        return
    elif not _graphInited:
        initBitmap()

    if _bitmap_decode(_graphicsDir, _bitmapType, pic, x, y):
        if _debug:
            dirname = _graphicsDir.replace('roms/', 'pics/')
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            filename = f'{dirname}{pic}.png'
            _processImage(filename)
        else:
            _processImage()
        return True
    else:
        return False

def _bitmap_load(filename, start = 0, length = -1):
    try:
        with open(filename, 'rb') as bitmapFile:
            bitmapFile.seek(start, 0 if start >= 0 else 2)
            return bytearray(bitmapFile.read(length))
    except:
        return None

_bitmap = None
def _bitmap_alloc(x, y):
    global _bitmap
    _bitmap = Bitmap(x, y)

'''
    A PC or ST palette colour is a sixteen bit value in which the low three nybbles
    hold the rgb colour values. The lowest nybble holds the blue value, the 
    second nybble the blue value and the third nybble the red value. (The high
    nybble is ignored). Within each nybble, only the low three bits are used
    IE the value can only be 0-7 not the full possible 0-15 and so the MSbit in
    each nybble is always 0.
'''
def _bitmap_pcst_colour(big, small):
    r = big & 0xF
    g = (small >> 4) & 0xF
    b = small & 0xF

    r *= 0x49; r >>= 1
    g *= 0x49; g >>= 1
    b *= 0x49; b >>= 1

    return (r & 0xFF, g & 0xFF, b & 0xFF)

'''
    ST Bitmaps

    On the ST different graphics file formats were used for the early V4
    games (Knight Orc, Gnome Ranger) and the later V4 games (Lancelot,
    Ingrid's Back, Time & Magik and Scapeghost).
'''

'''
    Extracts the number of pixels requested from an eight-byte data block (4 bit-
    planes) passed to it.

    Note:   On entry each one of four pointers is set to poto the start of each
            bit-plane in the block. The function then indexes through each byte in
            each bit plane. and uses shift and mask operations to extract each four
            bit pixel into an L9PIXEL.

            The bit belonging to the pixel in the current byte of the current bit-
            plane is moved to its position in an eight-bit pixel. The byte is then
            masked by a value to select only that bit and added to the final pixel
            value.
'''
def _bitmap_st1_decode_pixels(bitmap, data, count, pixels):
    bitplane_length = count // 4 # length of each bitplane 
    bitplane0 = data # address of bit0 bitplane 
    bitplane1 = data + (bitplane_length) # address of bit1 bitplane 
    bitplane2 = data + (bitplane_length * 2) # address of bit2 bitplane 
    bitplane3 = data + (bitplane_length * 3) # address of bit3 bitplane 
    pixel_index = 0 # index variables 

    for bitplane_index in range(bitplane_length):
        # build the eight pixels from the current bitplane bytes, high bit to low 

        # bit7 byte 
        bitmap[pixel_index] = (((bitplane3[bitplane_index] >> 4) & 0x08)
            + ((bitplane2[bitplane_index] >> 5) & 0x04)
            + ((bitplane1[bitplane_index] >> 6) & 0x02)
            + ((bitplane0[bitplane_index] >> 7) & 0x01))
        pixel_index += 1
        if pixels == pixel_index:
            break

        # bit6 byte 
        bitmap[pixel_index] = (((bitplane3[bitplane_index] >> 3) & 0x08) 
            + ((bitplane2[bitplane_index] >> 4) & 0x04)
            + ((bitplane1[bitplane_index] >> 5) & 0x02)
            + ((bitplane0[bitplane_index] >> 6) & 0x01))
        pixel_index += 1
        if pixels == pixel_index:
            break

        # bit5 byte 
        bitmap[pixel_index] = (((bitplane3[bitplane_index] >> 2) & 0x08) 
            + ((bitplane2[bitplane_index] >> 3) & 0x04)
            + ((bitplane1[bitplane_index] >> 4) & 0x02)
            + ((bitplane0[bitplane_index] >> 5) & 0x01))
        pixel_index += 1
        if pixels == pixel_index:
            break

        # bit4 byte 
        bitmap[pixel_index] = (((bitplane3[bitplane_index] >> 1) & 0x08) 
            + ((bitplane2[bitplane_index] >> 2) & 0x04)
            + ((bitplane1[bitplane_index] >> 3) & 0x02)
            + ((bitplane0[bitplane_index] >> 4) & 0x01))
        pixel_index += 1
        if pixels == pixel_index:
            break

        # bit3 byte 
        bitmap[pixel_index] = (((bitplane3[bitplane_index]) & 0x08) 
            + ((bitplane2[bitplane_index] >> 1) & 0x04)
            + ((bitplane1[bitplane_index] >> 2) & 0x02)
            + ((bitplane0[bitplane_index] >> 3) & 0x01))
        pixel_index += 1
        if pixels == pixel_index:
            break

        # bit2 byte 
        bitmap[pixel_index] = (((bitplane3[bitplane_index] << 1) & 0x08) 
            + ((bitplane2[bitplane_index])      & 0x04)
            + ((bitplane1[bitplane_index] >> 1) & 0x02)
            + ((bitplane0[bitplane_index] >> 2) & 0x01))
        pixel_index += 1
        if pixels == pixel_index:
            break

        # bit1 byte 
        bitmap[pixel_index] = (((bitplane3[bitplane_index] << 2) & 0x08) 
            + ((bitplane2[bitplane_index] << 1) & 0x04)
            + ((bitplane1[bitplane_index])      & 0x02)
            + ((bitplane0[bitplane_index] >> 1) & 0x01))
        pixel_index += 1
        if pixels == pixel_index:
            break

        # bit0 byte 
        bitmap[pixel_index] = (((bitplane3[bitplane_index] << 3) & 0x08) 
            + ((bitplane2[bitplane_index] << 2) & 0x04)
            + ((bitplane1[bitplane_index] << 1) & 0x02)
            + ((bitplane0[bitplane_index]) & 0x01))
        pixel_index += 1
        if pixels == pixel_index:
            break

    return pixel_index

'''
    The ST image file has the following format. It consists of a 44 byte header
    followed by the image data. 

    The header has the following format:
    Bytes 0-31:        sixteen entry ST palette
    Bytes 32-33:    padding
    Bytes 34-35:    big-endian word holding number of bitplanes needed to make
                up a row of pixels*
    Bytes 36-37:    padding
    Bytes 38-39:    big-endian word holding number of rows in the image*
    Bytes 40-41:    padding**
    Bytes 42-43:    mask for pixels to show in last 16 pixel block. Again, this 
                is big endian

    [*]        these are probably big-endian unsigned longs but I have designated
            the upper two bytes as padding because (a) Level 9 does not need
            them as longs and (b) using unsigned shorts reduces byte sex induced
            byte order juggling.
    [**]    not certain what this is for but I suspect that, like bytes 42-43
            it is a mask to indicate which pixels to show, in this case in the 
            first 16 pixel block 

    The image data is essentially a memory dump of the video RAM representing
    the image in lo-res mode. In lo-res mode each row is 320 pixels wide
    and each pixel can be any one of sixteen colours - needs 4 bits to store. 

    In the ST video memory (in lo-res mode which we are dealing with here)
    is organised as follows. The lowest poin memory in the frame buffer 
    represents the top-left of the screen, the highest the bottom-right. 
    Each row of pixels is stored in sequence. 

    Within each pixel row the pixels are stored as follows. Each row is
    divided into groups of 16 pixels. Each sixteen pixel group is stored
    in 8 bytes, logically four groups of two. Each two byte pair 
    is a bit-plane for that sixteen pixel group - that is it stores the
    same bit of each pixel in that group. The first two bytes store the 
    lowest bit, the second pair the second bit &c. 

    The word at bytes 34-35 of the header stores the number of bitplanes
    that make up each pixel row in the image. Multplying this number by
    four gives the number of pixels in the row***. For title and frame 
    images that will be 320, for sub-images it will be less. 

    [***]    Not always exactly. For GnomeRanger sub-images this value is 60 
            - implying there are 240 pixels per row. In fact there are only 
            225 pixels in each row. To identify this situation look at the 
            big-endian word in bytes 42-43 of the header. This is a mask 
            telling you the pixels to use. Each bit represents one pixel in 
            the block, with the MSBit representing the first pixel and the 
            LSbit the last.

            In this situation, the file does contain the entire sixteen
            pixel block (it has to with the bitplane arrangement) but
            the pixels which are not part of the image are just noise. When
            decoding the image, the produced has the actual pixel 
            dimensions - the surplus pixels are discarded.

            I suspect, though I have not found an instance, that in theory
            the same situation could apply at the start of a pixel row and that
            in this case the big-endian word at bytes 40-41 is the mask.

    Having obtained the pixel dimensions of the image the function uses
    them to allocate memory for the bitmap and then extracts the pixel
    information from the bitmap row by row. For each row eight byte blocks
    are read from the image data and passed to UnpackSTv1Pixels along with
    the number of pixels to extract (usually 16, possibly less for the last
    block in a row.)
'''
def _bitmap_st1_decode(filename, x, y):
    data = _bitmap_load(filename)
    if not data:
        return False

    bitplanes_row = data[35]+data[34]*256
    bitmaps_row = bitplanes_row//4
    max_x = bitplanes_row*4
    max_y = data[39]+data[38]*256
    last_block = data[43]+data[42]*256

    # Check if sub-image with rows shorter than max_x 
    if last_block != 0xFFFF:
        # use last_block to adjust max_x 
        i = 0
        while (0x0001 & last_block) == 0: # test for ls bit set 
            last_block >>= 1 # if not, shift right one bit 
            i += 1
        max_x = max_x - i

    if max_x > MAX_BITMAP_WIDTH or max_y > MAX_BITMAP_HEIGHT:
        return False

    if x == 0 and y == 0:
        _bitmap_alloc(max_x, max_y)

    if x+max_x > _bitmap.width:
        max_x = _bitmap.width-x
    if y+max_y > _bitmap.height:
        max_y = _bitmap.height-y

    for yi in range(max_y):
        pixel_count = 0
        for xi in range(bitmaps_row):
            if (max_x - pixel_count) < 16:
                get_pixels = max_x - pixel_count
            else:
                get_pixels = 16

            pixel_count += _bitmap_st1_decode_pixels(
                _bitmap.bitmap[x + xi * 16][y + yi],
                data + 44 + yi * bitplanes_row * 2 + xi * 8, 8, get_pixels)

    _bitmap.npalette = 16
    for i in range(16):
        _bitmap.palette[i] = _bitmap_pcst_colour(data[i * 2], data[1 + i * 2])

    return True

def _bitmap_st2_name(num, dir):
    # title picture is #30 
    if num == 0:
        num = 30
    return f'{dir}{num}.squ'

'''
    PC Bitmaps

    On the PC different graphics file formats were used for the early V4
    games (Knight Orc, Gnome Ranger) and the later V4 games (Lancelot,
    Ingrid's Back, Time & Magik and Scapeghost).

    The ST and the PC both use the same image file format for the later 
    V4 games (Lancelot, Ingrid's Back, Time & Magik and Scapeghost.)
'''

def _bitmap_pc_name(num, dir):
    # title picture is #30 
    if num == 0:
        num = 30
    return f'{dir}{num}.pic'

'''
    The EGA standard for the IBM PCs and compatibles defines 64 colors, any
    16 of which can be mapped to the usable palette at any given time. If
    you display these 64 colors in numerical order, 16 at a time, you get a
    hodgepodge of colors in no logical order. The 64 EGA color numbers are
    assigned in a way that the numbers can easily be converted to a relative
    intensity of each of the three phosphor colors R,G,B. If the number is
    converted to six bit binary, the most significant three bits represent
    the 25% level of R,G,B in that order and the least significant three
    bits represent the 75% level of R,G,B in that order. Take EGA color 53
    for example. In binary, 53 is 110101. Since both R bits are on, R = 1.0.
    Of the G bits only the 25% bit is on so G = 0.25. Of the B bits only the
    75% bit is on so B = 0.75.
'''
def _bitmap_pc1_colour(i):
    r = (((i & 4) >>1 ) | ((i & 0x20) >> 5)) * 0x55
    g = ( (i & 2)       | ((i & 0x10) >> 4)) * 0x55
    b = (((i & 1) << 1) | ((i & 0x08) >> 3)) * 0x55
    return (r, g, b)

'''
    The PC (v1) image file has the following format. It consists of a 22
    byte header organised like this: 

    Byte 0:     probably a file type flag
    Byte 1:     the MSB of the file's length as a word
    Bytes 2-3:  little-endian word with picture width in pixels
    Bytes 4-5:  little-endian word with picture height in pixel rows
    Bytes 6-21: the image colour table. One EGA colour in each byte

    The image data is extremely simple. The entire block is packed array
    of 4-bit pixels - IE each byte holds two pixels - the first in the high
    nybble, the second in the low. The pixel value is an index into the 
    image colour table. The pixels are organised with the top left first and 
    bottom left last, each row in turn.
'''
def _bitmap_pc1_decode(filename, x, y):
    data = _bitmap_load(filename)
    if not data:
        return False

    max_x = data[2]+data[3]*256
    max_y = data[4]+data[5]*256
    if max_x > MAX_BITMAP_WIDTH or max_y > MAX_BITMAP_HEIGHT:
        return False

    if x == 0 and y == 0:
        _bitmap_alloc(max_x, max_y)

    if x+max_x > _bitmap.width:
        max_x = _bitmap.width-x
    if y+max_y > _bitmap.height:
        max_y = _bitmap.height-y

    for yi in range(max_y):
        for xi in range(max_x):
            _bitmap.bitmap[x + xi][y + yi] = (data[23 +((yi * max_x) // 2)
                + (xi // 2)] >> ((1 - (xi & 1)) * 4)) & 0x0f

    _bitmap.npalette = 16
    for i in range(16):
        _bitmap.palette[i] = _bitmap_pc1_colour(data[6 + i])

    return True

'''
    The PC (v2) image file has the following format. It consists of a 44
    byte header followed by the image data. 

    The header has the following format:
    Bytes 0-1: "datalen":     length of file -1 as a big-endian word*
    Bytes 2-3: "flagbyte1 & flagbyte2": unknown, possibly type identifiers. 
        Usually 0xFF or 0xFE followed by 0x84, 0x72, 0xFF, 0xFE or
        some other (of a fairly small range of possibles) byte.
    Bytes 4-35: "colour_index[]": sixteen entry palette. Basically an ST 
        palette (even if in a PC image file. Each entry is a sixteen
        bit value in which the low three nybbles hold the rgb colour
        values. The lowest nybble holds the blue value, the second
        nybble the blue value and the third nybble the red value. (The
        high nybble is ignored). Within each nybble, only the low
        three bits are used IE the value can only be 0-7 not the full
        possible 0-15 and so the MSbit in each nybble is always 0.**,
    Bytes 36-37: "width": image width in pixels as a big-endian word
    Bytes 38-39: "numrows": image height in pixel rows as a big-endian word
    Byte 40: "seedByte": seed byte to start picture decoding.
    Byte 41: "padByte": unknown. Possibly padding to word align the next 
        element?
    Bytes 42-297: "pixelTable": an array of 0x100 bytes used as a lookup table 
        for pixel values
    Bytes 298-313: "bitStripTable": an array of 0x10 bytes used as a lookup table 
        for the number of bytes to strip from the bit stream for the pixel being
        decoded
    Bytes 314-569:    "indexByteTable": an array of 0x100 bytes used as a lookup 
        table to index into bitStripTable and pixelTable****

    The encoded image data then follows ending in a 0x00 at the file length stored
    in the first two bytes of the file. there is then one extra byte holding a 
    checksum produced by the addition of all the bytes in the file (except the first 
    two and itself)*

    [*] in some PC games the file is padded out beyond this length to the
    nearest 0x80/0x00 boundary with the byte 0x1A. The valid data in the 
    file still finishes where this word says with the checkbyte following it.
    [**] I imagine when a game was running on a PC this standard palette
    was algorithimcally changed to suit the graphics mode being used
    (Hercules, MDA, CGA, EGA, MCGA, VGA &c.) 
    [***]    Note also, in image 1 of PC Time & Magik I think one palette entry
    is bad as what should be white in the image is actually set to
    a very pale yellow. This is corrected with the display of the next 
    sub-picture and I am pretty sure it is note a decoding problem
    here as when run on the PC the same image has the same pale yellow
    cast.
    [****] for detail of how all this works see below

    As this file format is intended for two very different platforms the decoded
    imaged data is in a neutral, intermediate form. Each pixel is extracted as a
    byte with only the low four bits significant. The pixel value is an index into
    the sixteen entry palette.

    The pixel data is compressed, presumably to allow a greater number of images
    to be distributed on the (rather small) default ST & PC floppy disks (in both
    cases about 370 Kbytes.)*****

    Here's how to decode the data. The image data is actually a contiguous bit
    stream with the byte structure on disk having almost no relevance to the
    encoding. We access the bit stream via a two-byte buffer arranged as a word.

    Preparation:

    Initially, move the first byte from the image data into the low byte of
    theBitStreamBuffer and move the second byte of the image data into the
    high byte of theBitStreamBuffer.

    Set a counter (theBufferBitCounter) to 8 which you will use to keep track
    of when it is necesary to refill the buffer.

    Set a variable (theNewPixel) to byte 40 (seedByte) of the header.
    We need to do this because as part of identifying the pixel being
    extracted we need to know the value of the previous pixel extracted. Since
    none exists at this powe must prime this variable with the correct
    value.

    Extraction:

    Set up a loop which you will execute once for each pixel to be extracted
    and within that loop do as follows.

    Copy the low byte of theBitStreamBuffer to an L9BYTE
    (theNewPixelIndexSelector). Examine theNewPixelIndexSelector. If this
    is 0xFF this flags that the index to the new pixel is present as a
    literal in the bit stream; if it is NOT 0xFF then the new pixel index
    value has to be decoded.

    If theNewPixelIndexSelector is NOT 0xFF do as follows:

    Set the variable theNewPixelIndex to the byte in the
    indexByteTable array of the header indexed by
    theNewPixelIndexSelector.

    Set the variable theBufferBitStripCount to the value in the
    bitStripTable array of the header indexed by theNewPixelIndex.

    One-by-one use right bit shift (>>) to remove
    theBufferBitStripCount bits from theBitStreamBuffer. After each
    shift decrement theBufferBitCounter and check whether it has
    reached 0. If it has, get the next byte from the image data and
    insert it in the high byte of theBitStreamBuffer and reset
    theBufferBitCounter to 8. What is happening here is as we remove
    each bit from the bottom of the bit stream buffer we check to see
    if there are any bits left in the high byte of the buffer. As soon
    as we know there are none, we refill it with the next eight bits
    from the image data.

    When this 'bit-stripping' is finished, other than actually identifying
    the new pixel we are nearly done. I will leave that for the moment and
    look at what happens if the low byte of theBitStreamBuffer we put in
    theNewPixelIndexSelector was actually 0xFF:

    In this case, instead of the above routine we begin by removing
    the low eight bits from the theBitStreamBuffer. We use the same
    ono-by-one bit shift right process described above to do this,
    again checking after each shift if it is necesary to refill the
    buffer's high byte.

    When the eight bits have been removed we set theNewPixelIndex to
    the value of the low four bits of theBitStreamBuffer. Having done
    that we again one-by-one strip off those low four bits from the
    theBitStreamBuffer, again checking if we need to refill the buffer
    high byte.

    Irrespective of whether we initially had 0xFF in
    theNewPixelIndexSelector we now have a new value in theNewPixelIndex.
    This value is used as follows to obtain the new pixel value.

    The variable theNewPixel contains either the seedByte or the value of
    the previously extracted pixel. In either case this is a 4-bit value
    in the lower 4 bits. Use the left bit shift operator (or multiply by
    16) to shift those four bits into the high four bits of theNewPixel.

    Add the value in theNewPixelIndex (it is a 4-bit value) to
    theNewPixel. The resulting value is used as an index into the
    pixelTable array of the header to get the actual new pixel value so
    theNewPixel = header.pixelTable[theNewPixel] gets us our new pixel and
    primes theNewPixel for the same process next time around the loop.

    Having got our new pixel it is stored in the next empty space in the
    bitmap and we loop back and start again.

    [*****]    I am not sure how the compression was done - someone with a better
    understanding of this area may be able to work out the method from the above.
    I worked out how to decode it by spending many, many hours tracing through the
    code in a debugger - thanks to the now defunct HiSoft for their DevPac ST and
    Gerin Philippe for NoSTalgia <http://users.skynet.be/sky39147/>.
'''
def _bitmap_pc2_decode(filename, x, y):
    data = _bitmap_load(filename)
    if not data:
        return False

    max_x = data[37]+data[36]*256
    max_y = data[39]+data[38]*256
    if max_x > MAX_BITMAP_WIDTH or max_y > MAX_BITMAP_HEIGHT:
        return False

    if x == 0 and y == 0:
        _bitmap_alloc(max_x, max_y)

    if x+max_x > _bitmap.width:
        max_x = _bitmap.width-x
    if y+max_y > _bitmap.height:
        max_y = _bitmap.height-y

    # prime the new pixel variable with the seed byte 
    theNewPixel = data[40]
    # initialise the index to the image data 
    theImageDataIndex = 570
    # prime the bit stream buffer 
    theImageFileData = data
    theBitStreamBuffer = theImageFileData[theImageDataIndex]
    theImageDataIndex += 1
    theBitStreamBuffer = theBitStreamBuffer + 0x100 * theImageFileData[theImageDataIndex]
    theImageDataIndex += 1
    # initialise the bit stream buffer bit counter 
    theBufferBitCounter = 8

    for yi in range(max_y):
        for xi in range(max_x):
            theNewPixelIndexSelector = (theBitStreamBuffer & 0x00FF)
            if theNewPixelIndexSelector != 0xFF:
                # get index for new pixel and bit strip count 
                theNewPixelIndex = data[314 + theNewPixelIndexSelector]
                # get the bit strip count 
                theBufferBitStripCount = data[298 + theNewPixelIndex]
                # strip theBufferBitStripCount bits from theBitStreamBuffer 
                while theBufferBitStripCount > 0:
                    theBitStreamBuffer = theBitStreamBuffer >> 1
                    theBufferBitStripCount -= 1
                    theBufferBitCounter -= 1
                    if theBufferBitCounter == 0:
                        # need to refill the theBitStreamBuffer high byte 
                        theBitStreamBuffer = theBitStreamBuffer + 0x100 * theImageFileData[theImageDataIndex]
                        theImageDataIndex += 1
                        # re-initialise the bit stream buffer bit counter 
                        theBufferBitCounter = 8
            else:
                # strip the 8 bits holding 0xFF from theBitStreamBuffer 
                theBufferBitStripCount = 8
                while theBufferBitStripCount > 0:
                    theBitStreamBuffer = theBitStreamBuffer >> 1
                    theBufferBitStripCount -= 1
                    theBufferBitCounter -= 1
                    if theBufferBitCounter == 0:
                        # need to refill the theBitStreamBuffer high byte 
                        theBitStreamBuffer = theBitStreamBuffer + 0x100 * theImageFileData[theImageDataIndex]
                        theImageDataIndex += 1
                        # re-initialise the bit stream buffer bit counter 
                        theBufferBitCounter = 8
                # get the literal pixel index value from the bit stream 
                theNewPixelIndex = (0x000F & theBitStreamBuffer)
                theBufferBitStripCount = 4
                # strip 4 bits from theBitStreamBuffer 
                while theBufferBitStripCount > 0:
                    theBitStreamBuffer = theBitStreamBuffer >> 1
                    theBufferBitStripCount -= 1
                    theBufferBitCounter -= 1
                    if theBufferBitCounter == 0:
                        # need to refill the theBitStreamBuffer high byte 
                        theBitStreamBuffer = theBitStreamBuffer + 0x100 * theImageFileData[theImageDataIndex]
                        theImageDataIndex += 1
                        # re-initialise the bit stream buffer bit counter 
                        theBufferBitCounter = 8

            # shift the previous pixel into the high four bits of theNewPixel 
            theNewPixel = (0xF0 & (theNewPixel << 4))
            # add the index to the new pixel to theNewPixel 
            theNewPixel = theNewPixel + theNewPixelIndex
            # extract the nex pixel from the table 
            theNewPixel = data[42 + theNewPixel]
            # store new pixel in the bitmap 
            _bitmap.bitmap[x + xi][y + yi] = theNewPixel

    _bitmap.npalette = 16
    for i in range(16):
        _bitmap.palette[i] = _bitmap_pcst_colour(data[4 + i * 2], data[5 + i * 2])

    return True

def _bitmap_pc_type(filename):
    type = B.PC2_BITMAPS

    data = _bitmap_load(filename, length = 6)
    if data != None:
        x = data[2] + data[3] * 256
        y = data[4] + data[5] * 256

        if x == 0x0140 and y == 0x0087:
            type = B.PC1_BITMAPS
        if x == 0x00E0 and y == 0x0074:
            type = B.PC1_BITMAPS
        if x == 0x0140 and y == 0x0087:
            type = B.PC1_BITMAPS
        if x == 0x00E1 and y == 0x0076:
            type = B.PC1_BITMAPS

    return type

'''
    Amiga Bitmaps
'''

def _bitmap_noext_name(num, dir):
    if num == 0:
        filename = f'{dir}title'
        if os.path.isfile(filename):
            return filename
        else:
            num = 30

    return f'{dir}{num}'

def _bitmap_amiga_intensity(col):
    return int(pow(col/15, 1.0/0.8) * 0xff)

'''
    Amiga palette colours are word length structures with the red, green and blue
    values stored in the second, third and lowest nybles respectively. The high
    nybble is always zero.
'''
def _bitmap_amiga_colour(i1, i2):
    r = _bitmap_amiga_intensity(i1 & 0xf)
    g = _bitmap_amiga_intensity(i2 >> 4)
    b = _bitmap_amiga_intensity(i2 & 0xf)
    return (r, g, b)

'''
    The Amiga image file has the following format. It consists of a 44 byte
    header followed by the image data. 

    The header has the following format:
    Bytes 0-63:  thirty-two entry Amiga palette
    Bytes 64-65: padding
    Bytes 66-67: big-endian word holding picture width in pixels*
    Bytes 68-69: padding
    Bytes 70-71: big-endian word holding number of pixel rows in the image*

    [*] these are probably big-endian unsigned longs but I have designated
    the upper two bytes as padding because (a) Level 9 does not need
    them as longs and (b) using unsigned shorts reduces byte sex induced
    byte order juggling.

    The images are designed for an Amiga low-res mode screen - that is they 
    assume a 320*256 (or 320 * 200 if NSTC display) screen with a palette of 
    32 colours from the possible 4096.

    The image data is organised the same way that Amiga video memory is. The 
    entire data block is divided into five equal length bit planes with the 
    first bit plane holding the low bit of each 5-bit pixel, the second bitplane
    the second bit of the pixel and so on up to the fifth bit plane holding the 
    high bit of the f5-bit pixel.
'''
def _bitmap_amiga_decode(filename, x, y):
    data = _bitmap_load(filename)
    if not data:
        return False

    max_x = (((((data[64]<<8)|data[65])<<8)|data[66])<<8)|data[67]
    max_y = (((((data[68]<<8)|data[69])<<8)|data[70])<<8)|data[71]
    if max_x > MAX_BITMAP_WIDTH or max_y > MAX_BITMAP_HEIGHT:
        return False

    if x == 0 and y == 0:
        _bitmap_alloc(max_x, max_y)

    if x+max_x > _bitmap.width:
        max_x = _bitmap.width-x
    if y+max_y > _bitmap.height:
        max_y = _bitmap.height-y

    for yi in range(max_y):
        for xi in range(max_x):
            p = 0
            for b in range(5):
                p |= ((data[72+(max_x//8)*(max_y*b+yi)+xi//8]>>(7-(xi%8)))&1)<<b
            _bitmap.bitmap[x + xi][y + yi] = p

    _bitmap.npalette = 32
    for i in range(32):
        _bitmap.palette[i] = _bitmap_amiga_colour(data[i*2],data[i*2+1])

    return True

def _bitmap_noext_type(filename):
    data = _bitmap_load(filename, length = 72)
    if data != None:
        x = data[67] + data[66] * 256
        y = data[71] + data[70] * 256

        if x == 0x0140 and y == 0x0088:
            return B.AMIGA_BITMAPS
        if x == 0x0140 and y == 0x0087:
            return B.AMIGA_BITMAPS
        if x == 0x00E0 and y == 0x0075:
            return B.AMIGA_BITMAPS
        if x == 0x00E4 and y == 0x0075:
            return B.AMIGA_BITMAPS
        if x == 0x00E0 and y == 0x0076:
            return B.AMIGA_BITMAPS
        if x == 0x00DB and y == 0x0076:
            return B.AMIGA_BITMAPS

        x = data[3] + data[2] * 256
        y = data[7] + data[6] * 256

        if x == 0x0200 and y == 0x00D8:
            return B.MAC_BITMAPS
        if x == 0x0168 and y == 0x00BA:
            return B.MAC_BITMAPS
        if x == 0x0168 and y == 0x00BC:
            return B.MAC_BITMAPS
        if x == 0x0200 and y == 0x00DA:
            return B.MAC_BITMAPS
        if x == 0x0168 and y == 0x00DA:
            return B.MAC_BITMAPS

        x = data[35] + data[34] * 256
        y = data[39] + data[38] * 256

        if x == 0x0050 and y == 0x0087:
            return B.ST1_BITMAPS
        if x == 0x0038 and y == 0x0074:
            return B.ST1_BITMAPS

    return B.NO_BITMAPS

'''
    Macintosh Bitmaps
'''

'''
    The Mac image file format is very simple. The header is ten bytes
    with the width of the image in pixels in the first long and the 
    height (in pixel rows) in the second long - both are big-endian. 
    (In both cases I treat these as unsigned shorts to minimise byte 
    twiddling when working around byte sex issues). There follow two
    unidentified bytes - possibly image type identifiers or maybe 
    valid pixel masks for the beginning and end of pixel rows in
    sub-images.

    The image data is extremely simple. The entire block is a packed array
    of 1-bit pixels - I.E. each byte holds eight pixels - with 1 representing
    white and 0 representing black. The pixels are organised with the top
    left first and bottom left last, each row in turn.

    The image sizes are 512 * 216 pixels for main images and 360 * 186 pixels
    for sub-images.
'''
def _bitmap_mac_decode(filename, x, y):
    data = _bitmap_load(filename)
    if not data:
        return False

    max_x = data[3]+data[2]*256
    max_y = data[7]+data[6]*256
    if max_x > MAX_BITMAP_WIDTH or max_y > MAX_BITMAP_HEIGHT:
        return False

    if x > 0: # Mac bug, apparently 
        x = 78

    if x == 0 and y == 0:
        _bitmap_alloc(max_x, max_y)

    if x+max_x > _bitmap.width:
        max_x = _bitmap.width-x
    if y+max_y > _bitmap.height:
        max_y = _bitmap.height-y

    for yi in range(max_y):
        for xi in range(max_x):
            _bitmap.bitmap[x + xi][y + yi] = (data[10 + (max_x // 8) * yi + xi //8] >> (7 - (xi % 8))) & 1

    _bitmap.npalette = 2
    _bitmap.palette[0] = (0, 0, 0)
    _bitmap.palette[1] = (0xff, 0xff, 0xff)

    return True

'''
    C64 Bitmaps, also related formats (BBC B, Amstrad CPC and Spectrum +3)
'''

'''
    Commodore 64 palette from Vice
'''
_bitmap_c64_colours = [
        (0x00, 0x00, 0x00),
        (0xff, 0xff, 0xff),
        (0x89, 0x40, 0x36),
        (0x7a, 0xbf, 0xc7),
        (0x8a, 0x46, 0xae),
        (0x68, 0xa9, 0x41),
        (0x3e, 0x31, 0xa2),
        (0xd0, 0xdc, 0x71),
        (0x90, 0x5f, 0x25),
        (0x5c, 0x47, 0x00),
        (0xbb, 0x77, 0x6d),
        (0x55, 0x55, 0x55),
        (0x80, 0x80, 0x80),
        (0xac, 0xea, 0x88),
        (0x7c, 0x70, 0xda),
        (0xab, 0xab, 0xab)]

_bitmap_bbc_colours = [
        (0x00, 0x00, 0x00),
        (0xff, 0x00, 0x00),
        (0x00, 0xff, 0x00),
        (0xff, 0xff, 0x00),
        (0x00, 0x00, 0xff),
        (0xff, 0x00, 0xff),
        (0x00, 0xff, 0xff),
        (0xff, 0xff, 0xff)]

def _bitmap_c64_name(num, dir):
    if num == 0:
        return f'{dir}title mpic'
    else:
        return f'{dir}pic{num}'

def _bitmap_bbc_name(num, dir):
    if num == 0:
        filename = f'{dir}P.Title'
        if os.path.isfile(filename):
            return filename
        else:
            return f'{dir}title'
    else:
        filename = f'{dir}P.Pic{num}'
        if os.path.isfile(filename):
            return filename
        else:
            return f'{dir}pic{num}'

def _bitmap_cpc_name(num, dir):
    if num == 0:
        return f'{dir}title.pic'
    elif num == 1:
        return f'{dir}1.pic'
    else:
        return f'{dir}allpics.pic'

def _bitmap_c64_type(filename):
    type = B.C64_BITMAPS

    if os.path.isfile(filename):
        size = os.path.getsize(filename)

        if size == 10048:
            type = B.BBC_BITMAPS
        if size == 6494:
            type = B.BBC_BITMAPS

    return type

'''
    The C64 graphics file format is (loosely) based on the layout of
    C64 graphics memory. There are in fact two formats (i) the
    standard game images and (ii) title pictures. For both formats
    the file begins within the 2-byte pair 0x00 and 0x20.

    The images are "multi-color bitmap mode" images which means they
    have rows of 160 double width pixels and can be up to 200 rows
    long. (The title images are 200 lines long, the game images are
    136 lines long.) Unlike Amiga, Mac, ST and PC graphics there are
    no "main" and "sub" images. All game graphics have the same
    dimensions and each completely replaces its predecessor.

    The graphics files used on the Amstrad CPC and Spectrum +3 are also
    virtually identical to C64 graphics files. This choice was presumably
    made because although the CPC screen was more capable than the c64 it
    was (in low resolution) the same size (160*200) and presumably
    algorothmic conversion conversion of the colours was trivial for
    the interpreter. In addition (a) the artwork already existed so no
    extra expense would be incurred and (b) by accepting the C64's
    limitation of only four colours in each 4*8 pixel block (but still
    with sixteen colours on screen) they got a compressed file format
    allowing more pictures on each disk.

    The file organisation is rather different though. Only picture 
    one and the title picture are separate files. All the other 
    pictures (2-29) are stored in one large file "allpics.pic".

    On these platforms the picture 1 file and title picture file have
    an AMSDOS header (a 128 byte block of metadata) which contains a
    checksum of the first 66 bytes of the header in a little-endian
    word at bytes 67 & 68. On the original C64 platform there was a
    simple two byte header. Following the header the data is organised
    exactly as in the C64 game and title image files. The
    'allpics.pic" file has no header and consists of 0x139E blocks
    each forming a picture, in the C64 game file format (minus the two
    byte header).
'''
def _bitmap_c64_decode(filename, type, num):
    data = _bitmap_load(filename)
    if not data:
        return False

    if type == B.C64_BITMAPS:
        if len(data) == 10018: # C64 title picture 
            max_x = 320
            max_y = 200
            off = 2
            off_scr = 8002
            off_bg = 9003
            off_col = 9018
            col_comp = 0
        elif len(data) == 6464: # C64 picture 
            max_x = 320
            max_y = 136
            off = 2
            off_scr = 5442
            off_col = 6122
            off_bg = 6463
            col_comp = 1
        else:
            return False
    elif type == B.BBC_BITMAPS:
        if len(data) == 10058: # BBC title picture 
            max_x = 320
            max_y = 200
            off = 10
            off_scr = 8010
            off_bg = 9011
            off_col = 9026
            col_comp = 0
        elif len(data) == 10048: # BBC title picture 
            max_x = 320
            max_y = 200
            off = 0
            off_scr = 8000
            off_bg = 9001
            off_col = 9016
            col_comp = 0
        elif len(data) == 6504: # BBC picture 
            max_x = 320
            max_y = 136
            off = 10
            off_scr = 5450
            off_col = 6130
            off_bg = 6471
            col_comp = 1
        elif len(data) == 6494: # BBC picture 
            max_x = 320
            max_y = 136
            off = 0
            off_scr = 5440
            off_col = 6120
            off_bg = 6461
            col_comp = 1
        else:
            return False
    elif type == B.CPC_BITMAPS:
        if num == 0: # CPC/+3 title picture 
            max_x = 320
            max_y = 200
            off = 128
            off_scr = 8128
            off_bg = 9128
            off_col = 9144
            col_comp = 0
        elif num == 1: # First CPC/+3 picture 
            max_x = 320
            max_y = 136
            off = 128
            off_scr = 5568
            off_col = 6248
            off_bg = 6588
            col_comp = 1
        elif num >= 2 and num <= 29: # Subsequent CPC/+3 pictures 
            max_x = 320
            max_y = 136
            off = ((num-2)*6462)
            off_scr = 5440+((num-2)*6462)
            off_col = 6120+((num-2)*6462)
            off_bg = 6460+((num-2)*6462)
            col_comp = 1
        else:
            return False

    _bitmap_alloc(max_x, max_y)

    for yi in range(max_y):
        for xi in range(max_x//2):
            cx = xi//4
            px = xi%4
            cy = yi//8
            py = yi%8

            p = data[off+(cy*40+cx)*8+py]
            p = (p>>((3-px)*2))&3

            match p:
                case 0:
                    i = data[off_bg] & 0x0f
                case 1:
                    i = data[off_scr+cy*40+cx] >> 4
                case 2:
                    i = data[off_scr+cy*40+cx] & 0x0f
                case 3:
                    if col_comp:
                        i = (data[off_col+(cy*40+cx)//2]>>((1-(cx%2))*4)) & 0x0f
                    else:
                        i = data[off_col+(cy*40+cx)] & 0x0f

            _bitmap.bitmap[xi * 2][yi] = i
            _bitmap.bitmap[xi * 2 + 1][yi] = i

    _bitmap.npalette = 16
    for i in range(16):
        _bitmap.palette[i] = _bitmap_c64_colours[i]

    return True

'''
    The graphics files used by the BBC B are virtually identical
    to C64 graphics files. I assume that (as with the CPC and
    Spectrum+3) this choice was made because the BBC mode 2 screen,
    was nearly the same size (160*256) and had roughly the same capability
    as the C64 screen (displays 16 colours, although eight of those ar
    just the first eight flashing).

    In addition (a) the artwork already existed so no extra expense would
    be incurred and (b) by accepting the C64's limitation of only four
    colours in each 4*8 pixel block (but still with sixteen colours on
    screen) they got a compressed file format allowing more pictures
    on each disk.

    The file organisation is very close to the C64. The naming system
    can be the same eg "PIC12", but another form is also used :
    "P.Pic12". Unlike the C64 the BBC has well defined title images,
    called "TITLE" or P.Title. All pictures are in separate files.

    The only difference seems to be:

    * There is either *no* header before the image data or a simple
    10 byte header which I think *may* be a file system header
    left in place by the extractor system.

    * There is an extra 32 bytes following the data at the end of
    each file. These bytes encode a table to convert between the 16
    C64 colours and 16, four-pixel pix-patterns used to let the BBC
    (with only 8 colours) represent the sixteen possible C64 colours.

    A pix-pattern looks like this:

             |   Even |   Odd   |
             | Column | Column  |
        -----------------------------
        Even Row |Pixel 1 | Pixel 2 |
        ---------|--------|---------|
        Odd Row  |Pixel 3 | Pixel 4 |
        -----------------------------

    Each of the four pixel *can* be any of the eight BBC Mode 2
    steady colours. In practice they seem either to be all the
    same or a simple check of two colours - the pixels in the 
    odd row being in the reverse order to those in the even row.

    When converting a C64 pixel to a BBC pixel the game uses the
    value of the C64 pixel as an index into the array of sixteen
    BBC pix-patterns. The game looks at the selected pattern and
    chooses the BBC pixel colour thus: if the pixel is in an even
    numbered row and an even numbered column, it uses Pixel 1 from 
    the pattern, if in an even row but an odd column, it uses Pixel 3
    and so on.

    The pix-pattern data is encoded thus: the first sixteen bytes 
    encode the even row pixels for the patterns, one byte per
    pattern, and in the same way the second sixteen bytes encode
    the odd row pixels for each pattern. For example for the 
    pattern representing C64 colour 0 the even row pixels are encoded 
    in the first byte and the odd row pixels in the sixteenth byte.

    Within each byte the pixels are encoded in this way:

    Bit        7    6    5    4    3    2    1    0
    -------------------------------------
            0    0    1    0    0    1    1    1
            |    |    |    |    |    |    |    |
            +---|---+---|---+---|---+---|----- Even Pixel 0101 (5)
                |        |        |        |
                +-------+-------+-------+----- Odd Pixel 0011 (3)

    This function calls the C64 decoding routines to do the actual
    loading. See the comments to that function for details of how the
    image is encoded and stored.
'''
def _bitmap_bbc_decode(file, type, num):
    if _bitmap_c64_decode(file, type, num) == False:
        return False

    # Seek to the offset of the pixPat data and read in the data
    patRowDat = _bitmap_load(file, start = -32)
    if patRowDat == None:
        return False

    # Extract the patterns 
    i = 0
    patArray = [[[0, 0] for _ in range(2)] for _ in range(16)]
    for k in range(2):
        for j in range(16):
            # Extract the even col pixel for this pattern row 
            patArray[j][k][0] = (
                ((patRowData[i] >> 4) & 0x8) + ((patRowData[i] >> 3) & 0x4) +
                ((patRowData[i] >> 2) & 0x2) + ((patRowData[i] >> 1) & 0x1) )
            # Extract the odd col pixel for this pattern row 
            patArray[j][k][1] = (
                ((patRowData[i] >> 3) & 0x8) + ((patRowData[i] >> 2) & 0x4) +
                ((patRowData[i] >> 1) & 0x2) + ( patRowData[i]       & 0x1) )
            i += 1

    # Convert the image. Each BBC pixel is represented by two pixels here 
    isOddRow = 0
    for j in range(_bitmap.height):
        isOddColumn = 0
        for k in range(_bitmap.width // 2):
            pixel = _bitmap.bitmap[k * 2][j]
            _bitmap.bitmap[k * 2][j]     = patArray[pixel][isOddColumn][isOddRow]
            _bitmap.bitmap[k * 2 + 1][j] = patArray[pixel][isOddColumn][isOddRow]
            isOddColumn ^= 1
        isOddRow ^= 1

    _bitmap.npalette = 8
    for i in range(8):
        _bitmap.palette[i] = _bitmap_bbc_colours[i]

    return True

def _bitmap_detect(dir):
    filename = _bitmap_noext_name(2, dir)
    if os.path.isfile(filename):
        return _bitmap_noext_type(filename)

    filename = _bitmap_pc_name(2, dir)
    if os.path.isfile(filename):
        return _bitmap_pc_type(filename)

    filename = _bitmap_c64_name(2, dir)
    if os.path.isfile(filename):
        return _bitmap_c64_type(filename)

    filename = _bitmap_bbc_name(2, dir)
    if os.path.isfile(filename):
        return B.BBC_BITMAPS

    filename = _bitmap_cpc_name(2, dir)
    if os.path.isfile(filename):
        return B.CPC_BITMAPS

    filename = _bitmap_st2_name(2, dir)
    if os.path.isfile(filename):
        return B.ST2_BITMAPS

    return B.NO_BITMAPS

def _bitmap_decode(dir, type, num, x, y):
    match type:
        case B.PC1_BITMAPS:
            filename = _bitmap_pc_name(num, dir)
            if os.path.isfile(filename):
                if _bitmap_pc1_decode(filename, x, y):
                    return True

        case B.PC2_BITMAPS:
            filename = _bitmap_pc_name(num, dir)
            if os.path.isfile(filename):
                if _bitmap_pc2_decode(filename, x, y):
                    return True

        case B.AMIGA_BITMAPS:
            filename = _bitmap_noext_name(num, dir)
            if os.path.isfile(filename):
                if _bitmap_amiga_decode(filename, x, y):
                    return True

        case B.C64_BITMAPS:
            filename = _bitmap_c64_name(num, dir)
            if os.path.isfile(filename):
                if _bitmap_c64_decode(filename, type, num):
                    return True

        case B.BBC_BITMAPS:
            filename = _bitmap_bbc_name(num, dir)
            if os.path.isfile(filename):
                if _bitmap_bbc_decode(filename, type, num):
                    return True

        case B.CPC_BITMAPS:
            filename = _bitmap_cpc_name(num, dir)
            if os.path.isfile(filename):
                if _bitmap_c64_decode(filename, type, num): # Nearly identical to C64 
                    return True

        case B.MAC_BITMAPS:
            filename = _bitmap_noext_name(num, dir)
            if os.path.isfile(filename):
                if _bitmap_mac_decode(filename, x, y):
                    return True

        case B.ST1_BITMAPS:
            filename = _bitmap_noext_name(num, dir)
            if os.path.isfile(filename):
                if _bitmap_st1_decode(filename, x, y):
                    return True

        case B.ST2_BITMAPS:
            filename = _bitmap_st2_name(num, dir)
            if os.path.isfile(filename):
                if _bitmap_pc2_decode(filename, x, y):
                    return True

    return False

def _processImage(filename = None):
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixels[i, j] = _bitmap.palette[_bitmap.bitmap[i][j]]

    if filename:
        image.save(filename, 'PNG')
    else:
        showImage(image)

def _decodeBitmaps(dirs):
    for dir in dirs:
        setupBitmap(dir)
        initBitmap()
        for pic in range(1, 31):
            showBitmap(pic, 0, 0)
        clearBitmap()

_debug = False
if __name__ == "__main__":
    _debug = True
    import glob
    _decodeBitmaps(glob.glob('roms/*/'))
