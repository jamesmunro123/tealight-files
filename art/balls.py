# By CAMbassador James

from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import (sin, cos, pi, sqrt)

from tealight.art import screen_width, screen_height

from random import (random, randint)

from tealight.utils import sleep

a=[]
n=30
s1=15
e=0
e2=0.5
mu=0.01
g=0.5

redcount=2*n
bluecount=2*n
domain=min(screen_width,screen_height)/2-10
radius=10
domain=domain-radius
hipporadius=domain/4
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
  r5=randint(0,domain)
  r6=randint(0,100)*(360)/100
  r1=r5*cos(r6)+screen_width/2
  r2=r5*sin(r6)+screen_height/2
  r3=randint(0,s1*100)/100-s1/2
  r4=randint(0,s1*100)/100-s1/2
  r7=randint(0,256)
  r8=randint(0,256)
  r9=randint(0,256)
  a=a+[r1,r2,r3,r4,r7,r8,r9,0,0,g]
 
  
  while c==1:
    c=0
    for j in range (0,i):
      n1=(a[d*i]-a[d*j])
      n2=(a[d*i+1]-a[d*j+1])
      nn=n1*n1+n2*n2
      
      if nn<4*radius*radius:
        c=1
        r5=randint(0,domain)
        r6=randint(0,100)*(360)/100
        r1=r5*cos(r6)+screen_width/2
        r2=r6*sin(r6)+screen_height/2
        a[d*i]=r1
        a[d*i+1]=r2


def ctorgba(c):
  string_out = "rgba("
  string_out = string_out + str(c[0]) + "," + str(c[1]) + "," + str(c[2]) + "," + str(c[3]) + ")"
  return string_out

  
def handle_frame():
    
  sleep(20)
  color("white")
  box(0,0,screen_width,screen_height)
  color("black")
  circle(screen_width/2,screen_height/2,domain+radius)
  for i in range (0,n):
    #a[d*i+8]=-a[d*i]/1000
    #a[d*i+9]=-a[d*i+1]/1000
    a[d*i]=a[d*i]+a[d*i+2]
    a[d*i+1]=a[d*i+1]+a[d*i+3]
    
    a1=a[d*i]-screen_width/2
    a2=a[d*i+1]-screen_height/2
    aa=sqrt(a1*a1+a2*a2)
    a[d*i+8]=-mu*a[d*i+2]-g*a1/aa
    a[d*i+9]=-mu*a[d*i+3]-g*a2/aa
    
    a[d*i+2]=a[d*i+2]*1+a[d*i+8]
    a[d*i+3]=a[d*i+3]*1+a[d*i+9]
   
 
  for i in range (0,n):
    c=[a[d*i+4],a[d*i+5],a[d*i+6],1]
    colstring = ctorgba(c)
    color(colstring)
    spot(a[d*i],a[d*i+1],radius)
  for i in range (0,n):
    for j in range (i+1,n):
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
            a[d*i+2]=((n2*n2-e*n1*n1)*v1x-(1+e)*n1*n2*v1y)/nn
            a[d*i+3]=(-(1+e)*n1*n2*v1x+(n1*n1-e*n2*n2)*v1y)/nn
            a[d*j+2]=((n2*n2-n1*n1)*v2x-2*n1*n2*v2y)/nn
            a[d*j+3]=(-2*n1*n2*v2x+(n1*n1-n2*n2)*v2y)/nn
            a[d*i]=a[d*i]+(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
            a[d*i+1]=a[d*i+1]+(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
            a[d*j]=a[d*j]-(0+radius-sqrt(nn)/2)*n1/sqrt(nn)
            a[d*j+1]=a[d*j+1]-(0+radius-sqrt(nn)/2)*n2/sqrt(nn)
            a[d*i+7]=0
            a[d*j+7]=0
    if a[d*i+7]!=0:
      a[d*i+7]=a[d*i+7]-1
  #print(i,domain*domain,(a[d*i]-screen_width/2)*(a[d*i]-screen_width/2)+(a[d*i+1]-screen_height/2)*(a[d*i+1]-screen_height/2))
            
    if (a[d*i]-screen_width/2)*(a[d*i]-screen_width/2)+(a[d*i+1]-screen_height/2)*(a[d*i+1]-screen_height/2)>domain*domain and a[d*i]<screen_width:
      #print(i)
      n1=-(a[d*i]-screen_width/2)
      n2=-(a[d*i+1]-screen_height/2)
      v1x=a[d*i+2]
      v1y=a[d*i+3]
      nn=n1*n1+n2*n2
      a[d*i+2]=((n2*n2-e2*n1*n1)*v1x-(1+e2)*n1*n2*v1y)/nn
      a[d*i+3]=(-(1+e2)*n1*n2*v1x+(n1*n1-e2*n2*n2)*v1y)/nn
      a[d*i]=a[d*i]+(0-domain+sqrt(nn))*n1/sqrt(nn)
      a[d*i+1]=a[d*i+1]+(0-domain+sqrt(nn))*n2/sqrt(nn)
