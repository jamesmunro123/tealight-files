from tealight.art import (color, line, spot, circle, box, image, text, background)

import math

from tealight.art import screen_width, screen_height

from random import (random, randint)

a=[]
n=7

for i in range (1,n+1):
  r1=randint(10,screen_width-10)
  r2=randint(10,screen_height-10)
  a=a+[r1,r2,1,0,0,0,255]

for i in range (1,n+1):
  r1=randint(5,screen_width-5)
  r2=randint(5,screen_height-5)
  a=a+[r1,r2,1,0,255,0,255]

for i in range (1,n+1):
  r1=randint(10,screen_width-10)
  r2=randint(10,screen_height-10)
  a=a+[r1,r2,1,0,255,0,0]

for i in range (1,n+1):
  r1=randint(5,screen_width-5)
  r2=randint(5,screen_height-5)
  a=a+[r1,r2,1,0,255,100,0]

def ctorgba(c):
  string_out = "rgba("
  string_out = string_out + str(c[0]) + "," + str(c[1]) + "," + str(c[2]) + "," + str(c[3]) + ")"
  return string_out



  
def handle_frame():
  sleep(30)
  color("white")
  box(0,0,screen_width,screen_height)
  for i in range (0,4*n):
    c=[a[7*i+4],a[7*i+5],a[7*i+6],1]
    colstring = ctorgba(c)
    color(colstring)
    spot(a[7*i],a[7*i+1],10)