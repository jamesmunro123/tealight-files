from tealight.art import (color, line, spot, circle, box, image, text, background)

import math

from tealight.art import screen_width, screen_height

from random import (random, randint)

from tealight.utils import sleep

a=[]
n=7
s1=15

#(x,y,u,v,colr,colg,colb,inert)
d=8
radius=10

for i in range (0,4*n):
  c=1
  r1=randint(10,screen_width-10)
  r2=randint(10,screen_height-10)
  r3=randint(0,s1*100)/100-s1/2
  r4=randint(0,s1*100)/100-s1/2
  a=a+[r1,r2,r3,r4,0,0,255,0]
  while c==1:
    c=0
    for j in range (0,i):
      n1=(a[d*i]-a[d*j])
      n2=(a[d*i+1]-a[d*j+1])
      nn=n1*n1+n2*n2
      
      if nn<1600:
        c=1
        
        r1=randint(10,screen_width-10)
        r2=randint(10,screen_height-10)
        a[d*i]=r1
        a[d*i+1]=r2

#for i in range (1,n+1):
#  r1=randint(5,screen_width-5)
#  r2=randint(5,screen_height-5)
#  r3=randint(0,s1*100)/100-s1/2
#  r4=randint(0,s1*100)/100-s1/2
#  a=a+[r1,r2,r3,r4,255,0,255]

#for i in range (1,n+1):
#  r1=randint(10,screen_width-10)
#  r2=randint(10,screen_height-10)
#  r3=randint(0,s1*100)/100-s1/2
#  r4=randint(0,s1*100)/100-s1/2
#  a=a+[r1,r2,r3,r4,255,0,0]

#for i in range (1,n+1):
#  r1=randint(5,screen_width-5)
#  r2=randint(5,screen_height-5)
#  r3=randint(0,s1*100)/100-s1/2
#  r4=randint(0,s1*100)/100-s1/2
#  a=a+[r1,r2,r3,r4,255,100,0]

def ctorgba(c):
  string_out = "rgba("
  string_out = string_out + str(c[0]) + "," + str(c[1]) + "," + str(c[2]) + "," + str(c[3]) + ")"
  return string_out



  
def handle_frame():
  sleep(30)
  color("white")
  box(0,0,screen_width,screen_height)
  
  for i in range (0,4*n):
    a[d*i]=a[d*i]+a[d*i+2]
    a[d*i+1]=a[d*i+1]+a[d*i+3]
  
  for i in range (0,4*n):
    c=[a[d*i+4],a[d*i+5],a[d*i+6],1]
    colstring = ctorgba(c)
    color(colstring)
    spot(a[d*i],a[d*i+1],radius)
    
  for i in range (0,4*n):
    for j in range (i+1,4*n):
      n1=(a[d*i]-a[d*j])
      n2=(a[d*i+1]-a[d*j+1])
      nn=n1*n1+n2*n2
      v1x=a[d*i+2]
      v1y=a[d*i+3]
      v2x=a[d*j+2]
      v2y=a[d*j+3]
      if nn<4*radius*radius:
        if nn !=0:
          if a[d*i+7]==0 and a[d*i+7]==0:
            a[d*i+2]=((n2*n2-n1*n1)*v1x-2*n1*n2*v1y)/nn
            a[d*i+3]=(-2*n1*n2*v1x+(n1*n1-n2*n2)*v1y)/nn
            a[d*j+2]=((n2*n2-n1*n1)*v2x-2*n1*n2*v2y)/nn
            a[d*j+3]=(-2*n1*n2*v2x+(n1*n1-n2*n2)*v2y)/nn
            a[d*i+7]=10
            a[d*j+7]=10
    if a[d*i+7]!=0:
      a[d*i+7]=a[d*i+7]-1
            #if a[7*i]*a[7*i]+a[7*i+1]*a[7*i+1]>10000:
     