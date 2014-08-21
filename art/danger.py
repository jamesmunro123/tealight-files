from tealight.art import (color, line, spot, circle, box, image, text, background)

import math

from tealight.art import screen_width, screen_height

from random import (random, randint)

a=[]
n=7

for i in range (1,n):
  r1=randint(5,screen_width-5)
  r2=randint(5,screen_height-5)
  a=a+[r1,r2,1,0,255,128,0]
  

print(a) 
for i in range (0,n-1):
  c=(a[7*i+4],a[7*i+5],a[7*i+6],1)
  color("blue")
  #color("rgba(255,128,0,0.5)")
  spot(a[7*i],a[7*i+1],10)
  line(1,2,3,400)
  