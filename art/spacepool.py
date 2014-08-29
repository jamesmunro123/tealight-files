# By CAMbassador James

from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import (sin, cos, pi, sqrt)

from tealight.art import screen_width, screen_height

from random import (random, randint)

from tealight.utils import sleep

a=[]
n=16
# n even, total number of balls

radius=25
s1=7
e=0.7
e2=1
mu=0.01

mx=0
my=0
mmx=mx
mmy=my


aimrad=min(screen_width/3,screen_height/3)

cx=screen_width/2
cy=screen_height/2
#(x,y,u,v,colr,colg,colb,out)
d=8

shiftx=0
shifty=0
dshiftx=0
dshifty=0
ffwd=0

sr=0
sb=0
gamestate=0
# gamestate 0 shot ready
# gamestate 1 no shot, balls moving
# gamestate 2 gameover
gameover=0
player=0
counter=0

for i in range (0,n):
  c=1
  r1=randint(0,screen_width)
  r2=randint(0,screen_height)
  #r3=randint(0,s1*100)/100-s1/2
  #r4=randint(0,s1*100)/100-s1/2
  
  if i<(n/2)-1:
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
      if (a[d*i]-cx)**2+(a[d*i+1]-cy)**2<9*radius**2 and i!=n-1:
        c=1
        r1=randint(0,screen_width)
        r2=randint(0,screen_height)
        a[d*i]=r1
        a[d*i+1]=r2

a[d*(n-2)+4]=70
a[d*(n-2)+5]=70
a[d*(n-2)+6]=70

        
a[d*(n-1)+4]=255
a[d*(n-1)+5]=255
a[d*(n-1)+6]=255

def ctorgba(c):
  string_out = "rgba("
  string_out = string_out + str(c[0]) + "," + str(c[1]) + "," + str(c[2]) + "," + str(c[3]) + ")"
  return string_out

 

def handle_mousedown(x,y):
  global n, a, gamestate, player
  a1=x-shiftx-a[d*(n-1)]
  a2=y-shifty-a[d*(n-1)+1]
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
    if player==0:
      player=1
    elif player==1:
      player=0
  gamestate=1
  
def handle_mousemove(x,y):
  global mmx, mmy
  mmx=x
  mmy=y

def handle_keydown(key):
  global dshiftx, dshifty, ffwd
  if key == "left":
    dshiftx=-5
  elif key == "up":
    dshifty=-5
  elif key == "right":
    dshiftx=5
  elif key == "down":
    dshifty=5
  elif key == "q":
    ffwd=1
    
def handle_keyup(key):
  global dshiftx, dshifty, ffwd
  if key == "left":
    dshiftx=0
  elif key == "up":
    dshifty=0
  elif key == "right":
    dshiftx=0
  elif key == "down":
    dshifty=0
  elif key == "q":
    ffwd=0
  

def handle_frame():
  global mx,my, gamestate, sr, sb, shiftx, shifty, dshiftx, dshifty, gameover, player, aimrad, ffwd, counter
  
  counter=(counter+1)%20
  
  if ffwd==0 or counter==0:  
    color("black")
    box(0,0,screen_width,screen_height)
  
  vsum=0
  shiftx=(shiftx+dshiftx)%screen_width
  shifty=(shifty+dshifty)%screen_height
  mx=mmx-shiftx
  my=mmy-shifty
  
  if ffwd==0 or counter==0:
    color("white")
    circle(cx+shiftx,cy+shifty,2*radius)
    circle(cx+screen_width+shiftx,cy+shifty,2*radius)
    circle(cx+shiftx-screen_width,cy+shifty,2*radius)
    circle(cx+shiftx,cy+shifty+screen_height,2*radius)
    circle(cx+shiftx,cy+shifty-screen_height,2*radius)
    circle(cx+shiftx+screen_width,cy+shifty+screen_height,2*radius)
    circle(cx+shiftx+screen_width,cy+shifty-screen_height,2*radius)
    circle(cx+shiftx-screen_width,cy+shifty+screen_height,2*radius)
    circle(cx+shiftx-screen_width,cy+shifty-screen_height,2*radius)
    color("rgba(255,0,0,1)")
    text(cx+shiftx-6,cy+shifty-24,sr)
    text(cx+shiftx+screen_width-6,cy+shifty-24,sr)
    text(cx+shiftx-screen_width-6,cy+shifty-24,sr)
    text(cx+shiftx-6,cy+shifty+screen_height-24,sr)
    text(cx+shiftx-6,cy+shifty-screen_height-24,sr)
    text(cx+shiftx+screen_width-6,cy+shifty+screen_height-24,sr)
    text(cx+shiftx+screen_width-6,cy+shifty-screen_height-24,sr)
    text(cx+shiftx-screen_width-6,cy+shifty+screen_height-24,sr)
    text(cx+shiftx-screen_width-6,cy+shifty-screen_height-24,sr)
    
    color("rgba(0,0,255,1)") 
    text(cx+shiftx-6,cy+shifty,sb)
    text(cx+shiftx+screen_width-6,cy+shifty,sb)
    text(cx+shiftx-screen_width-6,cy+shifty,sb)
    text(cx+shiftx-6,cy+shifty+screen_height,sb)
    text(cx+shiftx-6,cy+shifty-screen_height,sb)
    text(cx+shiftx+screen_width-6,cy+shifty+screen_height,sb)
    text(cx+shiftx+screen_width-6,cy+shifty-screen_height,sb)
    text(cx+shiftx-screen_width-6,cy+shifty+screen_height,sb)
    text(cx+shiftx-screen_width-6,cy+shifty-screen_height,sb)
  
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
    a1=a1*aimrad/sqrt(aa)
    a2=a2*aimrad/sqrt(aa)
    if gamestate==0 and aa<aimrad**2:
      if player==0:
        color("rgba(255,0,0,1)")
      elif player==1:
        color("rgba(0,0,255,1)")
      line(a[d*(n-1)]+shiftx,a[d*(n-1)+1]+shifty,a[d*(n-1)]+shiftx+a1,a[d*(n-1)+1]+shifty+a2)
      line(a[d*(n-1)]+shiftx+screen_width,a[d*(n-1)+1]+shifty,a[d*(n-1)]+shiftx+screen_width+a1,a[d*(n-1)+1]+shifty+a2)
      line(a[d*(n-1)]+shiftx-screen_width,a[d*(n-1)+1]+shifty,a[d*(n-1)]+shiftx-screen_width+a1,a[d*(n-1)+1]+shifty+a2)
      line(a[d*(n-1)]+shiftx,a[d*(n-1)+1]+shifty+screen_height,a[d*(n-1)]+shiftx+a1,a[d*(n-1)+1]+shifty+screen_height+a2)
      line(a[d*(n-1)]+shiftx,a[d*(n-1)+1]+shifty-screen_height,a[d*(n-1)]+shiftx+a1,a[d*(n-1)+1]+shifty-screen_height+a2)
      
      line(a[d*(n-1)]+shiftx+screen_width,a[d*(n-1)+1]+shifty+screen_height,a[d*(n-1)]+shiftx+screen_width+a1,a[d*(n-1)+1]+shifty+screen_height+a2)
      line(a[d*(n-1)]+shiftx+screen_width,a[d*(n-1)+1]+shifty-screen_height,a[d*(n-1)]+shiftx+screen_width+a1,a[d*(n-1)+1]+shifty-screen_height+a2)
      line(a[d*(n-1)]+shiftx-screen_width,a[d*(n-1)+1]+shifty+screen_height,a[d*(n-1)]+shiftx-screen_width+a1,a[d*(n-1)+1]+shifty+screen_height+a2)
      line(a[d*(n-1)]+shiftx-screen_width,a[d*(n-1)+1]+shifty-screen_height,a[d*(n-1)]+shiftx-screen_width+a1,a[d*(n-1)+1]+shifty-screen_height+a2)

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
        if i<(n/2)-1:
          sr=sr+1
        elif i<n-2:
          sb=sb+1
        else:
          if gameover==0:
            gameover=1
            if player==0:
              if sb==n/2-1:
                print("Blue wins.")
              else:
                print("Red wins.")
            if player==1:
              if sr==n/2-1:
                print("Red wins.")
              else:
                print("Blue wins.")
              
      if ffwd==0 or counter==0:
        c=[a[d*i+4],a[d*i+5],a[d*i+6],1]
        colstring = ctorgba(c)
        color(colstring)
        spot(a[d*i]+shiftx,a[d*i+1]+shifty,radius)
        spot(a[d*i]+shiftx+screen_width,a[d*i+1]+shifty,radius)
        spot(a[d*i]+shiftx-screen_width,a[d*i+1]+shifty,radius)
        spot(a[d*i]+shiftx,a[d*i+1]+shifty+screen_height,radius)
        spot(a[d*i]+shiftx,a[d*i+1]+shifty-screen_height,radius)
        spot(a[d*i]+shiftx+screen_width,a[d*i+1]+shifty+screen_height,radius)
        spot(a[d*i]+shiftx+screen_width,a[d*i+1]+shifty-screen_height,radius)
        spot(a[d*i]+shiftx-screen_width,a[d*i+1]+shifty+screen_height,radius)
        spot(a[d*i]+shiftx-screen_width,a[d*i+1]+shifty-screen_height,radius)
  
  
  if vsum>0.1:
    gamestate=1
  else:
    gamestate=0
    for i in range(0,n):
      a[d*i+2]=0
      a[d*i+3]=0
  
  
    