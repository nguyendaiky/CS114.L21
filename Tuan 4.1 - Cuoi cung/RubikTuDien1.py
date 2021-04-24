import sys
import bisect

input = sys.stdin.readline

# 4 colors
# front, down, left and right surface
# u , b , l , r chop
# U u U' u',... moves

# TAKE INPUT
colors = input().split() # 4 colors
moves  = input().split()

front = [colors[0]] * 9
down  = [colors[1]] * 9
left  = [colors[2]] * 9
right = [colors[3]] * 9

dottrash = input()


def output():
    sys.stdout.write( ' '.join(front) + '\n')
    sys.stdout.write( ' '.join(down) + '\n')
    sys.stdout.write( ' '.join(left) + '\n')
    sys.stdout.write( ' '.join(right))

#def move format
achop, bchop, cchop = 0 ,4 ,8
amid, bmid, cmid = [1,2,3], [6,5,1], [3,7,6]
def turn(a,b,c):
    a[achop], b[bchop], c[cchop] = c[cchop],a[achop], b[bchop] 

def turnmid(a,b,c):
    x,y,z = a[amid[0]], a[amid[1]], a[amid[2]]

    a[amid[0]], a[amid[1]], a[amid[2]] = c[cmid[0]], c[cmid[1]], c[cmid[2]]
    c[cmid[0]], c[cmid[1]], c[cmid[2]] = b[bmid[0]], b[bmid[1]], b[bmid[2]]
    b[bmid[0]], b[bmid[1]], b[bmid[2]] = x,y,z 

#def move for chop and mid
def chopu():
    turn(front, left, right)
def midu():
    turnmid(front, left, right)

def chopl():
    turn(left, front, down)
def midl():
    turnmid(left,front,down)

def chopr():
    turn(right, down, front)
def midr():
    turnmid(right, down, front)

def chopb():
    turn(down, right, left)
def midb():
    turnmid(down,right,left)

#def move for specific digits
def umove( mid = False, reverse = False ):
    time = 1
    if reverse:
        time = 2
    while time > 0:
        if mid :
            midu()
        chopu()
        time -= 1
def bmove( mid = False, reverse = False ):
    time = 1
    if reverse:
        time = 2
    while time > 0:
        if mid :
            midb()
        chopb()
        time -= 1
def lmove( mid = False, reverse = False ):
    time = 1
    if reverse:
        time = 2
    while time > 0:
        if mid :
            midl()
        chopl()
        time -= 1
def rmove( mid = False, reverse = False ):
    time = 1
    if reverse:
        time = 2
    while time > 0:
        if mid :
            midr()
        chopr()
        time -= 1

# CODE CORE
moves.reverse()
for move in moves:
    reverse = False
    if len(move) > 1:
        reverse = True
    mid = True
    if move[0].isupper():
        mid = False

    letter = move[0].lower()

    if letter == 'u':
        umove(mid,reverse)
    elif letter == 'b':
        bmove(mid,reverse)
    elif letter == 'l':
        lmove(mid, reverse)
    elif letter == 'r':
        rmove(mid,reverse)


# END
output()