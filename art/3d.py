from tealight.art import (color, line, spot, circle, box, image, text, background)

import math

from tealight.art import screen_width, screen_height

def linethree(x1,y1,z1,x2,y2,z2):
  phi=0.1
  theta=0.2
  alpha=0.5
  a1=x1*math.cos(phi)-y1*math.sin(phi)
  b1=x1*math.sin(phi)+y1*math.cos(phi)
  
  c1=b1*math.cos(theta)-z1*math.sin(theta)
  d1=b1*math.sin(theta)+z1*math.cos(theta)
  
  
  
  a1=screen_width/2+x1*math.sqrt(3)/2-y1/2
  b1=screen_height/2+x1/2+y1*math.sqrt(3)/2-z1
  a2=screen_width/2+x2*math.sqrt(3)/2-y2/2
  b2=screen_height/2+x2/2+y2*math.sqrt(3)/2-z2
  line(a1,b1,a2,b2)
  
  
  
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
linethree(100,0,0,100,100,0)