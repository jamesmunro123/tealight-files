from tealight.art import (color, line, spot, circle, box, image, text, background, color)

color("rgba(255,128,0,1)")


def parallel(x1,y1,x2,y2,x3,y3):
  x1=int(x1)
  y1=int(y1)
  x2=int(x2)
  y2=int(y2)
  x3=int(x3)
  y3=int(y3)
  x4=x2+x3-x1
  y4=y2+y3-y1
  for i in range(x1,x2):
    line(i,(y2-y1)*(i-x1)/(x2-x1)+y1,x3-x1+i,(y2-y1)*(i-x1)/(x2-x1)+y3)
 
parallel(20,40,200,100,100,120)

#line(i,(y2-y1)*(i-x1)/(x2-x1),x3-x1+i,(y2+y3-2*y1)*(i-x1)/(x2-x1))