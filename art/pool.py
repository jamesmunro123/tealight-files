# By CAMbassador James

from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import (sin, cos, pi, sqrt)

from tealight.art import screen_width, screen_height

from random import (random, randint)

from tealight.utils import sleep

a=[]
n=2
s1=5
e=0.5
e2=1
mu=5
g=0
mx=0
my=0
redcount=2*n
bluecount=2*n
domain=min(screen_width,screen_height)/2-10
radius=15
domain=domain-radius
hipporadius=domain/4
cx=screen_width/2
cy=screen_height/2
#(x,y,u,v,colr,colg,colb,inert,ax,ay)
d=10
hippo1=0
hippo2=0
hippo3=0
hippo4=0

sr=0
sb=0
gameend=0


for i in range (0,n):
  c=1
  r5=sqrt(randint(4*radius**2,domain**2))
  r6=randint(0,100)*(360)/100
  r1=r5*cos(r6)+screen_width/2
  r2=r5*sin(r6)+screen_height/2
  #r3=randint(0,s1*100)/100-s1/2
  #r4=randint(0,s1*100)/100-s1/2
  r7=randint(0,256)
  r8=randint(0,256)
  r9=randint(0,256)
  a=a+[r1,r2,0,0,r7,r8,r9,0,0,g]
 


  while c==1:
    c=0
    for j in range (0,i):
      n1=(a[d*i]-a[d*j])
      n2=(a[d*i+1]-a[d*j+1])
      nn=n1*n1+n2*n2
      
      if nn<4*radius*radius:
        c=0
        r5=randint(0,domain)
        r6=randint(0,100)*(360)/100
        r1=r5*cos(r6)+screen_width/2
        r2=r6*sin(r6)+screen_height/2
        a[d*i]=r1
        a[d*i+1]=r2
a[d*(n-1)+4]=0
a[d*(n-1)+5]=0
a[d*(n-1)+6]=0

def ctorgba(c):
  string_out = "rgba("
  string_out = string_out + str(c[0]) + "," + str(c[1]) + "," + str(c[2]) + "," + str(c[3]) + ")"
  return string_out

def handle_mousedown(x,y):
  global n, a
  a1=x-a[d*(n-1)]
  a2=y-a[d*(n-1)+1]
  aa=a1*a1+a2*a2
  a[d*(n-1)+2]=s1*a1/sqrt(aa)
  a[d*(n-1)+3]=s1*a2/sqrt(aa)

def handle_mousemove(x,y):
  global mx, my
  mx=x
  my=y
  
def handle_frame():
  global mx,my 
  sleep(20)
  color("white")
  box(0,0,screen_width,screen_height)
  color("black")
  circle(cx,cy,2*radius)
  
  for i in range (0,n):
    #a[d*i+8]=-a[d*i]/1000
    #a[d*i+9]=-a[d*i+1]/1000
    a[d*i]=a[d*i]+a[d*i+2]
    a[d*i+1]=a[d*i+1]+a[d*i+3]
    
    a[d*i]=a[d*i]%screen_width
    a[d*i+1]=a[d*i+1]%screen_height
    
    a1=a[d*i]-screen_width/2
    a2=a[d*i+1]-screen_height/2
    aa=sqrt(a1*a1+a2*a2)
    #a[d*i+8]=-mu*a[d*i+2]-g*a1/aa
    #a[d*i+9]=-mu*a[d*i+3]-g*a2/aa
    
    #a[d*i+8]=-mu*a[d*i+2]
    #a[d*i+9]=-mu*a[d*i+3]+g
   
    
    a[d*i+2]=a[d*i+2]*1+a[d*i+8]
    a[d*i+3]=a[d*i+3]*1+a[d*i+9]
   
 
    for j in range (i+1,n):
      n1=(a[d*i]-a[d*j])
      n2=(a[d*i+1]-a[d*j+1])
      nn=n1*n1+n2*n2
      if nn<4*radius*radius:
        if nn !=0:
          if a[d*i+7]==0 and a[d*i+7]==0:
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
            a[d*i+7]=0
            a[d*j+7]=0
            
            #c1=int((a[d*i+4]+a[d*j+4])/2)
            #c2=int((a[d*i+5]+a[d*j+5])/2)
            #c3=int((a[d*i+6]+a[d*j+6])/2)
            #a[d*i+4]=c1
            #a[d*i+5]=c2
            #a[d*i+6]=c3
            #a[d*j+4]=c1
            #a[d*j+5]=c2
            #a[d*j+6]=c3
    if a[d*i+7]!=0:
      a[d*i+7]=a[d*i+7]-1
  #print(i,domain*domain,(a[d*i]-screen_width/2)*(a[d*i]-screen_width/2)+(a[d*i+1]-screen_height/2)*(a[d*i+1]-screen_height/2))
    if 0==1:        
      if a[d*i]<radius:
        #print(i)
        n1=1
        n2=0
        v1x=a[d*i+2]
        v1y=a[d*i+3]
        nn=n1*n1+n2*n2
        a[d*i+2]=((n2*n2-e2*n1*n1)*v1x-(1+e2)*n1*n2*v1y)/nn
        a[d*i+3]=(-(1+e2)*n1*n2*v1x+(n1*n1-e2*n2*n2)*v1y)/nn
        a[d*i]=radius
        a[d*i+1]=a[d*i+1]
        
      if a[d*i]>screen_width-radius:
        #print(i)
        n1=-1
        n2=0
        v1x=a[d*i+2]
        v1y=a[d*i+3]
        nn=n1*n1+n2*n2
        a[d*i+2]=((n2*n2-e2*n1*n1)*v1x-(1+e2)*n1*n2*v1y)/nn
        a[d*i+3]=(-(1+e2)*n1*n2*v1x+(n1*n1-e2*n2*n2)*v1y)/nn
        a[d*i]=screen_width-radius
        a[d*i+1]=a[d*i+1]
      
      if a[d*i+1]<radius:
        #print(i)r
        n1=0
        n2=1
        v1x=a[d*i+2]
        v1y=a[d*i+3]
        nn=n1*n1+n2*n2
        a[d*i+2]=((n2*n2-e2*n1*n1)*v1x-(1+e2)*n1*n2*v1y)/nn
        a[d*i+3]=(-(1+e2)*n1*n2*v1x+(n1*n1-e2*n2*n2)*v1y)/nn
        a[d*i]=a[d*i]
        a[d*i+1]=radius
        
      if a[d*i+1]>screen_height-radius:
        #print(i)r
        n1=0
        n2=-1
        v1x=a[d*i+2]
        v1y=a[d*i+3]
        nn=n1*n1+n2*n2
        a[d*i+2]=((n2*n2-e2*n1*n1)*v1x-(1+e2)*n1*n2*v1y)/nn
        a[d*i+3]=(-(1+e2)*n1*n2*v1x+(n1*n1-e2*n2*n2)*v1y)/nn
        a[d*i]=a[d*i]
        a[d*i+1]=screen_height-radius
      
    if (a[d*i]-cx)**2+(a[d*i+1]-cy)**2<4*radius**2 and i!=n-1:
      print("Ding!")
            
    v=min(100*int(sqrt(a[d*i+2]**2+a[d*i+3]**2)),255)
    #c=[v,256-v,0,1]
    c=[a[d*i+4],a[d*i+5],a[d*i+6],1]
    colstring = ctorgba(c)
    color(colstring)
    spot(a[d*i],a[d*i+1],radius)
  color("rbga(0,0,0,0)")
  line(a[d*(n-1)],a[d*(n-1)+1],mx,my)
  