from tealight.art import (color, line, spot, circle, box, image, text, background)

import math

from tealight.art import screen_width, screen_height

from random import (random, randint)

a=[]

for i in range (1,3):
  r1=randint(0,screen_width)
  r2=randint(0,screen_height)
  a=a+[r1,r2,1,0,0,0,0]
  

print(a) 
for i in range (0,2):
  spot(a[7*i],a[7*i+1],10)
  