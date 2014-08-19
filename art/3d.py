from tealight.art import (color, line, spot, circle, box, image, text, background)

import math


def linethree(x1,y1,z1,x2,y2,z2):
  a1=100+x1*math.sqrt(3)/2-y1/2
  b1=100+x1/2+y1*math.sqrt(3)/2-z1
  a2=100+x2*math.sqrt(3)/2-y2/2
  b2=100+x2/2+y2*math.sqrt(3)/2-z2
  line(a1,a2,30,40)

linethree(0,0,0,1,0,0)