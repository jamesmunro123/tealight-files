from tealight.art import (color, line, spot, circle, box, image, text, background)

import math

from tealight.art import screen_width, screen_height

from random import (random, randint)

a=[]

for i in range (1,3):
  r=randint(0,6)
  a=a+[r,r,1,0,0,0,0]
  

print(a) 
for i in range (0,2):
  spot(a[7*i],a[7*i+1],10)
  