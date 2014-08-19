from tealight.art import (color, line, spot, circle, box, image, text, background)

import math

from tealight.art import screen_width, screen_height

phi=0
theta=0
alpha=0

def linethree(x1,y1,z1,x2,y2,z2):

  a1=x1*math.cos(phi)-y1*math.sin(phi)
  b1=x1*math.sin(phi)+y1*math.cos(phi)
  
  c1=b1*math.cos(theta)-z1*math.sin(theta)
  d1=b1*math.sin(theta)+z1*math.cos(theta)
  
  e1=screen_width/2+a1*math.cos(alpha)-c1*math.sin(alpha)
  f1=screen_height/2+a1*math.sin(alpha)+c1*math.cos(alpha)
  
  
  a2=x2*math.cos(phi)-y2*math.sin(phi)
  b2=x2*math.sin(phi)+y2*math.cos(phi)
  
  c2=b2*math.cos(theta)-z2*math.sin(theta)
  d2=b2*math.sin(theta)+z2*math.cos(theta)
  
  e2=screen_width/2+a2*math.cos(alpha)-c2*math.sin(alpha)
  f2=screen_height/2+a2*math.sin(alpha)+c2*math.cos(alpha)
  
#  a1=screen_width/2+x1*math.sqrt(3)/2-y1/2
#  b1=screen_height/2+x1/2+y1*math.sqrt(3)/2-z1
#  a2=screen_width/2+x2*math.sqrt(3)/2-y2/2
#  b2=screen_height/2+x2/2+y2*math.sqrt(3)/2-z2
  line(e1,f1,e2,f2)
  
  
def handle_keydown(key):
  global phi, theta, alpha
  
  if key == "a":
    phi=phi+0.1
  elif key == "s":
    theta=theta+0.1
  elif key == "d":
    alpha=alpha+0.1
  elif key == "z":
    phi=phi-0.1
  elif key == "x":
    theta=theta-0.1
  elif key == "c":
    alpha=alpha-0.1 
    

  color("white")
  box(0,0,screen_width,screen_height)
  color("black")
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