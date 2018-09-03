# Newton's method, all about maths, just memorize it.

def mySqrt(x):
    r = x
    while r**2 > x:
        r = (r+r//x)//2
    return r