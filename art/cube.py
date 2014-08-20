from tealight.art import (color, line, spot, circle, box, image, text, background)

import math

from tealight.art import screen_width, screen_height

from tealight.utils import sleep

phi=0
theta=0
alpha=0
dphi=0
dtheta=0
dalpha=0

def xy3(x1,y1,z1):

  a1=x1*math.cos(phi)-y1*math.sin(phi)
  b1=x1*math.sin(phi)+y1*math.cos(phi)
  
  c1=b1*math.cos(theta)-z1*math.sin(theta)
  d1=b1*math.sin(theta)+z1*math.cos(theta)
  
  e1=screen_width/2+a1*math.cos(alpha)-c1*math.sin(alpha)
  f1=screen_height/2+a1*math.sin(alpha)+c1*math.cos(alpha)
  

  
#  a1=screen_width/2+x1*math.sqrt(3)/2-y1/2
#  b1=screen_height/2+x1/2+y1*math.sqrt(3)/2-z1
#  a2=screen_width/2+x2*math.sqrt(3)/2-y2/2
#  b2=screen_height/2+x2/2+y2*math.sqrt(3)/2-z2
  return (e1,f1)

def z3(x1,y1,z1):
  b1=x1*math.sin(phi)+y1*math.cos(phi)
  f1=b1*math.sin(theta)+z1*math.cos(theta)
  return f1
  
def handle_keydown(key):
  global dphi, dtheta, dalpha
  if key == "left":
    dphi=0.1
  elif key == "up":
    dtheta=0.1
  elif key == "d":
    dalpha=0.1
  elif key == "right":
    dphi=-0.1
  elif key == "down":
    dtheta=-0.1
  elif key == "c":
    dalpha=-0.1
    
def handle_keyup(key):
  global dphi, dtheta, dalpha
  if key == "left":
    dphi=0
  elif key == "up":
    dtheta=0
  elif key == "d":
    dalpha=0
  elif key == "right":
    dphi=-0
  elif key == "down":
    dtheta=-0
  elif key == "c":
    dalpha=-0 
    

  
def parallel(x1,y1,x2,y2,x3,y3):
  #x1=int(x1)
  #y1=int(y1)
  #x2=int(x2)
  #y2=int(y2)
  #x3=int(x3)
  #y3=int(y3)
  if x2!=x1:
    for j in range(0,150):
      i=x1+(x2-x1)*j/150
      line(i,(y2-y1)*(i-x1)/(x2-x1)+y1,x3-x1+i,(y2-y1)*(i-x1)/(x2-x1)+y3)
  if x2!=x1:  
    for j in range(0,150):
      i=x2+(x1-x2)*j/150
      line(i,(y1-y2)*(i-x2)/(x1-x2)+y2,x3-x1+i,(y1-y2)*(i-x2)/(x1-x2)+y3+y2-y1)
  if y1!=y3:
    for j in range(0,150):
      i=y1+(y3-y1)*j/150
      line((x3-x1)*(i-y1)/(y3-y1)+x1,i,(x3-x1)*(i-y1)/(y3-y1)+x2,i+y2-y1)
  if y1!=y3:
    for j in range(0,150):
      i=y3+(y1-y3)*j/150
      line((x1-x3)*(i-y3)/(y1-y3)+x3,i,(x1-x3)*(i-y3)/(y1-y3)+x3+x2-x1,i+y2-y1)
def side(x1,y1,z1,x2,y2,z2,x3,y3,z3):
  a1=xy3(x1,y1,z1)
  a2=xy3(x2,y2,z2)
  a3=xy3(x3,y3,z3)
  a5=a1+a2+a3
  parallel(*a5)

def handle_frame():
  sleep(100)  
  global phi, theta, alpha, dphi, dtheta, dalpha
  
  phi=phi+dphi
  theta=theta+dtheta
  alpha=alpha+dalpha
  color("white")
  box(0,0,screen_width,screen_height)
  
  
  
  color("black")
  side(-100,-100,-100,100,-100,-100,-100,-100,100)
  color("red")
  side(-100,-100,-100,-100,100,-100,-100,-100,100)
  color("green")
  side(-100,-100,-100,100,-100,-100,-100,100,-100)
  #linethree(100,-100,-100,100,-100,100)
  #linethree(100,-100,100,-100,-100,100)
  #linethree(-100,-100,-100,-100,-100,100)
  #linethree(-100,100,-100,100,100,-100)
  #linethree(100,100,-100,100,100,100)
  #linethree(100,100,100,-100,100,100)
  #linethree(-100,100,-100,-100,100,100)
  #linethree(-100,-100,-100,-100,100,-100)
  #linethree(-100,-100,100,-100,100,100)
  #linethree(100,-100,100,100,100,100)
  #linethree(100,-100,-100,100,100,-100)