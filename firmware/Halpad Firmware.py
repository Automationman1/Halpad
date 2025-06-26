print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

keyboard.modules.append(Encoder_handler)
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())

Encoder_handler.pins = ((board.D8, board.D7,None))
macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.D0,board.D1,board.D2,board.D3)
keyboard.row_pins = (board.D6,board.D10,board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.F14,KC.F15,KC.F16,KC.MB_MMB],
    [KC.F17,KC.F18,KC.F19,KC.MB_MMB],
    [KC.F20,KC.F21,KC.F22,KC.MB_MMB]

]
encoder_handler.map= [
((KC.MW_UP, KC.MW_DN))
]
if __name__ == '__main__':
    keyboard.go()
