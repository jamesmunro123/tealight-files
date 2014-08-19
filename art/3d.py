from tealight.art import (color, line, spot, circle, box, image, text, background)

import math

from tealight.art import screen_width, screen_height

def linethree(x1,y1,z1,x2,y2,z2):
  a1=screen_width/2+x1*math.sqrt(3)/2-y1/2
  b1=screen_height/2+x1/2+y1*math.sqrt(3)/2-z1
  a2=screen_width/2+x2*math.sqrt(3)/2-y2/2
  b2=screen_height/2+x2/2+y2*math.sqrt(3)/2-z2
  line(a1,b1,a2,b2)
  print a2-screen_width/2
  print b2-screen_height/2

  
  
  
linethree(0,0,0,100,0,0)
linethree(100,0,0,100,0,100)
linethree(100,0,100,0,0,100)
linethree(0,0,0,0,0,100)
linethree(0,100,0,100,100,0)
linethree(100,100,0,100,100,100)
linethree(100,100,100,0,100,100)
linethree(0,100,0,0,100,100)
linethree(0,0,0,0,100,0)
linethree(0,0,100,0,100,100)
linethree(100,0,100,100,100,100)
linethree(100,0,0,0,100,100)