import msvcrt

def readch(echo=True):
    "Get a single character on Windows."
    while msvcrt.kbhit():  # clear out keyboard buffer
        ch = msvcrt.getch()
        if ch in '\x00\xe0':  # arrow or function key prefix?
            ch = msvcrt.getch()  # second call returns the actual key code
    ch = msvcrt.getch()
    if ch in '\x00\xe0':  # arrow or function key prefix?
        ch = msvcrt.getch()  # second call returns the actual key code
    if echo:
        msvcrt.putch(ch)
    return ch

def key_down():
    print("Key Down pressed")


def key_up():
    print("Key UP pressed")


def key_left():
    print("Key Left pressed")


def do_shit():
    print("Shit is being done")
    while True:
        key = readch()
        print("Key pressed:{0}".format(key))
        if key == 80: #Down arrow
            key_down()
        elif key == 72: #Up arrow
            key_up()



print("Here we come!")
do_shit()

from msvcrt import getch
while True:
    print(ord(getch()))