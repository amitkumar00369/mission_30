
import math


def jug_mug(x,y,t):
    if t==0:
        return True
    if t>x+y:
        return False
    return  t % math.gcd(x,y) == 0

print(jug_mug(3,5,4))