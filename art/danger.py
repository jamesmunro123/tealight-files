from tealight.art import (color, line, spot, circle, box, image, text, background)

import math

from tealight.art import screen_width, screen_height

from random import (random, randint)

from tealight.utils import sleep

a=[]
n=7
s1=10

for i in range (1,n+1):
  r1=randint(10,screen_width-10)
  r2=randint(10,screen_height-10)
  r3=randint(0,s1*100)/100-s1/2
  r4=randint(0,s1*100)/100-s1/2
  a=a+[r1,r2,r3,r4,0,0,255]

for i in range (1,n+1):
  r1=randint(5,screen_width-5)
  r2=randint(5,screen_height-5)
  r3=randint(0,s1*100)/100-s1/2
  r4=randint(0,s1*100)/100-s1/2
  a=a+[r1,r2,r3,r4,255,0,255]

for i in range (1,n+1):
  r1=randint(10,screen_width-10)
  r2=randint(10,screen_height-10)
  r3=randint(0,s1*100)/100-s1/2
  r4=randint(0,s1*100)/100-s1/2
  a=a+[r1,r2,r3,r4,255,0,0]

for i in range (1,n+1):
  r1=randint(5,screen_width-5)
  r2=randint(5,screen_height-5)
  r3=randint(0,s1*100)/100-s1/2
  r4=randint(0,s1*100)/100-s1/2
  a=a+[r1,r2,r3,r4,255,100,0]

def ctorgba(c):
  string_out = "rgba("
  string_out = string_out + str(c[0]) + "," + str(c[1]) + "," + str(c[2]) + "," + str(c[3]) + ")"
  return string_out



  
def handle_frame():
  sleep(30)
  color("white")
  box(0,0,screen_width,screen_height)
  
  for i in range (0,4*n):
    a[7*i]=a[7*i]+a[7*i+2]
    a[7*i+1]=a[7*i+1]+a[7*i+3]
  
  for i in range (0,4*n):
    c=[a[7*i+4],a[7*i+5],a[7*i+6],1]
    colstring = ctorgba(c)
    color(colstring)
    spot(a[7*i],a[7*i+1],20)
    
  for i in range (0,4*n):
    for j in range (i+1,4*n):
      #print a[7*j]
      print (a[7*i]-a[7*j])*(a[7*i]-a[7*j])
      #print((a[7*i+1]-a[7*j+1])^2)
      n1=(a[7*i]-a[7*j])
      n2=(a[7*i+1]-a[7*j+1])
      nn=n1*n1+n2*n2
      v1x=a[7*i+2]
      v1y=a[7*i+3]
      v2x=a[7*j+2]
      v2y=a[7*j+3]
      if nn<1600:
        print("crash!")
        a[7*i+2]=((n2*n2-n1*n1)*v1x-2*n1*n2*v1y)/nn
        a[7*i+3]=(-2*n1*n2*v1x+(n1*n1-n2*n2)*v1y)/nn
        a[7*j+2]=((n2*n2-n1*n1)*v2x-2*n1*n2*v2y)/nn
        a[7*j+3]=(-2*n1*n2*v2x+(n1*n1-n2*n2)*v2y)/nn
            