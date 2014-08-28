# By CAMbassador James

from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import (sin, cos, pi, sqrt)

from tealight.art import screen_width, screen_height

from random import (random, randint)

from tealight.utils import sleep

a=[]
n=13
s1=10
e=0.5
e2=1
mu=0.01

mx=0
my=0
redcount=2*n
bluecount=2*n
domain=min(screen_width,screen_height)/2-10
radius=15

aimrad=20*radius

domain=domain-radius
hipporadius=domain/4
cx=screen_width/2
cy=screen_height/2
#(x,y,u,v,colr,colg,colb,out)
d=8


sr=0
sb=0
gamestate=0
# gamestate 0 shot ready
# gamestate 1 no shot, balls moving
player=0


for i in range (0,n):
  c=1
  r1=randint(0,screen_width)
  r2=randint(0,screen_height)
  #r3=randint(0,s1*100)/100-s1/2
  #r4=randint(0,s1*100)/100-s1/2
  
  if i<int(n/2):
    a=a+[r1,r2,0,0,255,0,0,0]
  else:
    a=a+[r1,r2,0,0,0,0,255,0]
  while c==1:
    c=0
    for j in range (0,i):
      n1=(a[d*i]-a[d*j])
      n2=(a[d*i+1]-a[d*j+1])
      nn=n1*n1+n2*n2
      
      if nn<4*radius*radius:
        c=1
        r1=randint(0,screen_width)
        r2=randint(0,screen_height)
        a[d*i]=r1
        a[d*i+1]=r2
      if (a[d*i]-cx)**2+(a[d*i+1]-cy)**2<4*radius**2 and i!=n-1:
        c=1
        r1=randint(0,screen_width)
        r2=randint(0,screen_height)
        a[d*i]=r1
        a[d*i+1]=r2
        
a[d*(n-1)+4]=255
a[d*(n-1)+5]=255
a[d*(n-1)+6]=255

def ctorgba(c):
  string_out = "rgba("
  string_out = string_out + str(c[0]) + "," + str(c[1]) + "," + str(c[2]) + "," + str(c[3]) + ")"
  return string_out

def sphere(x,y,rad,colr,colg,colb):
  for i in range(0,rad):
    r=radius-i
    c=[min(colr+10*i,255),min(colg+10*i,255),min(colb+10*i,255),1]
    colstring = ctorgba(c)
    color(colstring)
    spot(int((x+i)/(2*sqrt(2))),int((y+i)/(2*sqrt(2))),r)
  

def handle_mousedown(x,y):
  global n, a, gamestate
  a1=x-a[d*(n-1)]
  a2=y-a[d*(n-1)+1]
  if a1>screen_width/2:
    a1=-screen_width+a1
  elif a1<-screen_width/2:
    a1=screen_width+a1
  if a2>screen_height/2:
    a2=-screen_height+a2
  elif a2<-screen_height/2:
    a2=screen_height+a2
  aa=a1*a1+a2*a2
  if gamestate==0 and aa<aimrad**2:
    a[d*(n-1)+2]=s1*a1/sqrt(aa)
    a[d*(n-1)+3]=s1*a2/sqrt(aa)

def handle_mousemove(x,y):
  global mx, my
  mx=x
  my=y
  
def handle_frame():
  global mx,my, gamestate, sr, sb
  
  sleep(20)
  color("black")
  box(0,0,screen_width,screen_height)
  color("white")
  circle(cx,cy,2*radius)
  color("rgba(255,0,0,1)")
  text(cx-6,cy-24,sr)
  color("rgba(0,0,255,1)")
  text(cx-6,cy,sb)  
  
  vsum=0
  
  for i in range (0,n):
    if a[d*i+7]!=1:
      a[d*i]=a[d*i]+a[d*i+2]
      a[d*i+1]=a[d*i+1]+a[d*i+3]
      vv=sqrt(a[d*i+2]**2+a[d*i+3]**2)
      if vv!=0:
        a[d*i+2]=a[d*i+2]*(1-mu/vv)
        a[d*i+3]=a[d*i+3]*(1-mu/vv)
      
      a[d*i]=a[d*i]%screen_width
      a[d*i+1]=a[d*i+1]%screen_height
      
      vsum=vsum+vv
      
      #Collisions   
      for j in range (i+1,n):
        if a[d*j+7]!=1:
          n1=(a[d*i]-a[d*j])
          n2=(a[d*i+1]-a[d*j+1])
          nn=n1*n1+n2*n2
          if nn<4*radius*radius:
            if nn !=0:
              v1x=a[d*i+2]
              v1y=a[d*i+3]
              v2x=a[d*j+2]
              v2y=a[d*j+3]        
              v3x=n1*v1x+n2*v1y
              v3y=-n2*v1x+n1*v1y
              v4x=n1*v2x+n2*v2y
              v4y=-n2*v2x+n1*v2y              
              v5x=0.5*((1-e)*v3x+(1+e)*v4x)
              v6x=0.5*((1-e)*v4x+(1+e)*v3x)              
              v7x=(n1*v5x-n2*v3y)/nn
              v7y=(n2*v5x+n1*v3y)/nn
              v8x=(n1*v6x-n2*v4y)/nn
              v8y=(n2*v6x+n1*v4y)/nn
              a[d*i+2]=v7x
              a[d*i+3]=v7y
              a[d*j+2]=v8x
              a[d*j+3]=v8y 
              a[d*i]=a[d*i]+(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
              a[d*i+1]=a[d*i+1]+(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
              a[d*j]=a[d*j]-(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
              a[d*j+1]=a[d*j+1]-(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
          n1=(a[d*i]-a[d*j]-screen_width)
          n2=(a[d*i+1]-a[d*j+1])
          nn=n1*n1+n2*n2
          if nn<4*radius*radius:
            if nn !=0:
              v1x=a[d*i+2]
              v1y=a[d*i+3]
              v2x=a[d*j+2]
              v2y=a[d*j+3]        
              v3x=n1*v1x+n2*v1y
              v3y=-n2*v1x+n1*v1y
              v4x=n1*v2x+n2*v2y
              v4y=-n2*v2x+n1*v2y              
              v5x=0.5*((1-e)*v3x+(1+e)*v4x)
              v6x=0.5*((1-e)*v4x+(1+e)*v3x)              
              v7x=(n1*v5x-n2*v3y)/nn
              v7y=(n2*v5x+n1*v3y)/nn
              v8x=(n1*v6x-n2*v4y)/nn
              v8y=(n2*v6x+n1*v4y)/nn
              a[d*i+2]=v7x
              a[d*i+3]=v7y
              a[d*j+2]=v8x
              a[d*j+3]=v8y 
              a[d*i]=a[d*i]+(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
              a[d*i+1]=a[d*i+1]+(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
              a[d*j]=a[d*j]-(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
              a[d*j+1]=a[d*j+1]-(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
          n1=(a[d*i]-a[d*j]+screen_width)
          n2=(a[d*i+1]-a[d*j+1])
          nn=n1*n1+n2*n2
          if nn<4*radius*radius:
            if nn !=0:
              v1x=a[d*i+2]
              v1y=a[d*i+3]
              v2x=a[d*j+2]
              v2y=a[d*j+3]        
              v3x=n1*v1x+n2*v1y
              v3y=-n2*v1x+n1*v1y
              v4x=n1*v2x+n2*v2y
              v4y=-n2*v2x+n1*v2y              
              v5x=0.5*((1-e)*v3x+(1+e)*v4x)
              v6x=0.5*((1-e)*v4x+(1+e)*v3x)              
              v7x=(n1*v5x-n2*v3y)/nn
              v7y=(n2*v5x+n1*v3y)/nn
              v8x=(n1*v6x-n2*v4y)/nn
              v8y=(n2*v6x+n1*v4y)/nn
              a[d*i+2]=v7x
              a[d*i+3]=v7y
              a[d*j+2]=v8x
              a[d*j+3]=v8y 
              a[d*i]=a[d*i]+(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
              a[d*i+1]=a[d*i+1]+(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
              a[d*j]=a[d*j]-(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
              a[d*j+1]=a[d*j+1]-(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
        
          n1=(a[d*i]-a[d*j])
          n2=(a[d*i+1]-a[d*j+1]+screen_height)
          nn=n1*n1+n2*n2
          if nn<4*radius*radius:
            if nn !=0:
              v1x=a[d*i+2]
              v1y=a[d*i+3]
              v2x=a[d*j+2]
              v2y=a[d*j+3]        
              v3x=n1*v1x+n2*v1y
              v3y=-n2*v1x+n1*v1y
              v4x=n1*v2x+n2*v2y
              v4y=-n2*v2x+n1*v2y              
              v5x=0.5*((1-e)*v3x+(1+e)*v4x)
              v6x=0.5*((1-e)*v4x+(1+e)*v3x)              
              v7x=(n1*v5x-n2*v3y)/nn
              v7y=(n2*v5x+n1*v3y)/nn
              v8x=(n1*v6x-n2*v4y)/nn
              v8y=(n2*v6x+n1*v4y)/nn
              a[d*i+2]=v7x
              a[d*i+3]=v7y
              a[d*j+2]=v8x
              a[d*j+3]=v8y 
              a[d*i]=a[d*i]+(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
              a[d*i+1]=a[d*i+1]+(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
              a[d*j]=a[d*j]-(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
              a[d*j+1]=a[d*j+1]-(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
          n1=(a[d*i]-a[d*j])
          n2=(a[d*i+1]-a[d*j+1]-screen_height)
          nn=n1*n1+n2*n2
          if nn<4*radius*radius:
            if nn !=0:
              v1x=a[d*i+2]
              v1y=a[d*i+3]
              v2x=a[d*j+2]
              v2y=a[d*j+3]        
              v3x=n1*v1x+n2*v1y
              v3y=-n2*v1x+n1*v1y
              v4x=n1*v2x+n2*v2y
              v4y=-n2*v2x+n1*v2y              
              v5x=0.5*((1-e)*v3x+(1+e)*v4x)
              v6x=0.5*((1-e)*v4x+(1+e)*v3x)              
              v7x=(n1*v5x-n2*v3y)/nn
              v7y=(n2*v5x+n1*v3y)/nn
              v8x=(n1*v6x-n2*v4y)/nn
              v8y=(n2*v6x+n1*v4y)/nn
              a[d*i+2]=v7x
              a[d*i+3]=v7y
              a[d*j+2]=v8x
              a[d*j+3]=v8y 
              a[d*i]=a[d*i]+(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
              a[d*i+1]=a[d*i+1]+(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
              a[d*j]=a[d*j]-(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
              a[d*j+1]=a[d*j+1]-(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
        
      #Pocket
      if (a[d*i]-cx)**2+(a[d*i+1]-cy)**2<4*radius**2 and i!=n-1:
        a[d*i+7]=1
        if i<int(n/2):
          sr=sr+1
        else:
          sb=sb+1
        
              
      
      #c=[a[d*i+4],a[d*i+5],a[d*i+6],1]
      #colstring = ctorgba(c)
      #color(colstring)
      sphere(a[d*i],a[d*i+1],radius,a[d*i+4],a[d*i+5],a[d*i+6])
      #spot(a[d*i]+screen_width,a[d*i+1],radius)
      #spot(a[d*i]-screen_width,a[d*i+1],radius)
      #spot(a[d*i],a[d*i+1]+screen_height,radius)
      #spot(a[d*i],a[d*i+1]-screen_height,radius)
  
  if vsum>0.1:
    gamestate=1
  else:
    gamestate=0
    for i in range(0,n):
      a[d*i+2]=0
      a[d*i+3]=0
  
  a1=mx-a[d*(n-1)]
  a2=my-a[d*(n-1)+1]
  if a1>screen_width/2:
    a1=-screen_width+a1
  elif a1<-screen_width/2:
    a1=screen_width+a1
  if a2>screen_height/2:
    a2=-screen_height+a2
  elif a2<-screen_height/2:
    a2=screen_height+a2
  aa=a1*a1+a2*a2
  if gamestate==0 and aa<aimrad**2:
    color("rbga(0,0,0,0)")
    line(a[d*(n-1)],a[d*(n-1)+1],a[d*(n-1)]+a1,a[d*(n-1)+1]+a2)
    line(a[d*(n-1)]+screen_width,a[d*(n-1)+1],a[d*(n-1)]+screen_width+a1,a[d*(n-1)+1]+a2)
    line(a[d*(n-1)]-screen_width,a[d*(n-1)+1],a[d*(n-1)]-screen_width+a1,a[d*(n-1)+1]+a2)
    line(a[d*(n-1)],a[d*(n-1)+1]+screen_height,a[d*(n-1)]+a1,a[d*(n-1)+1]+screen_height+a2)
    line(a[d*(n-1)],a[d*(n-1)+1]-screen_height,a[d*(n-1)]+a1,a[d*(n-1)+1]-screen_height+a2)
    
    line(a[d*(n-1)]+screen_width,a[d*(n-1)+1]+screen_height,a[d*(n-1)]+screen_width+a1,a[d*(n-1)+1]+screen_height+a2)
    line(a[d*(n-1)]+screen_width,a[d*(n-1)+1]-screen_height,a[d*(n-1)]+screen_width+a1,a[d*(n-1)+1]-screen_height+a2)
    line(a[d*(n-1)]-screen_width,a[d*(n-1)+1]+screen_height,a[d*(n-1)]-screen_width+a1,a[d*(n-1)+1]+screen_height+a2)
    line(a[d*(n-1)]-screen_width,a[d*(n-1)+1]-screen_height,a[d*(n-1)]-screen_width+a1,a[d*(n-1)+1]-screen_height+a2)
