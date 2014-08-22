from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import (sin, cos, pi, sqrt)

from tealight.art import screen_width, screen_height

from random import (random, randint)

from tealight.utils import sleep

a=[]
n=10
s1=15
e=0.99
e2=1
e3=1.5
radius=30
hipporadius=100
redcount=2*n
bluecount=2*n
domain=min(screen_width,screen_height)/2-radius-10
#(x,y,u,v,colr,colg,colb,inert)
d=8
hippo1=0
hippo2=0
hippo3=0
hippo4=0

sr=0
sb=0
gameend=0


for i in range (0,4*n+1):
  c=1
  r5=randint(0,domain)
  r6=randint(0,100)*(360)/100
  r1=r5*cos(r6)+screen_width/2
  r2=r5*sin(r6)+screen_height/2
  r3=randint(0,s1*100)/100-s1/2
  r4=randint(0,s1*100)/100-s1/2
  a=a+[r1,r2,r3,r4,0,0,0,0]
  if i<n:
    a[d*i+4]=0
    a[d*i+5]=0
    a[d*i+6]=255
  if n-1<i and i<2*n:
    a[d*i+4]=255
    a[d*i+5]=0
    a[d*i+6]=255
  if 2*n-1 < i and i < 3*n:
    a[d*i+4]=255
    a[d*i+5]=0
    a[d*i+6]=0
  if 3*n-1<i and i<4*n:
    a[d*i+4]=255
    a[d*i+5]=100
    a[d*i+6]=0
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

def handle_keydown(key):
  global hippo1, hippo2, hippo3, hippo4
  if key == "left":
    hippo1=1
  elif key == "up":
    hippo2=1
  elif key == "down":
    hippo3=1
  elif key == "right":
    hippo4=1

    
def handle_keyup(key):
  global hippo1, hippo2, hippo3, hippo4
  if key == "left":
    hippo1=0
  elif key == "up":
    hippo2=0
  elif key == "down":
    hippo3=0
  elif key == "right":
    hippo4=0



  
def handle_frame():
  global sr, sb, gameend, e3, redcount, bluecount
  if gameend==0:
    
    sleep(20)
    color("white")
    box(0,0,screen_width,screen_height)
    color("black")
    circle(screen_width/2,screen_height/2,domain+radius)
    
    for i in range (0,4*n+1):
      a[d*i]=a[d*i]+a[d*i+2]
      a[d*i+1]=a[d*i+1]+a[d*i+3]
      a[d*i+2]=a[d*i+2]*1
      a[d*i+3]=a[d*i+3]*1
    
    for i in range (0,4*n+1):
      c=[a[d*i+4],a[d*i+5],a[d*i+6],1]
      colstring = ctorgba(c)
      color(colstring)
      spot(a[d*i],a[d*i+1],radius)
    if i==4*n+1:
      color("white")
      text("!")
    for i in range (0,4*n+1):
      for j in range (i+1,4*n+1):
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
              
      if (a[d*i]-screen_width/2)*(a[d*i]-screen_width/2)+(a[d*i+1]-screen_height/2)*(a[d*i+1]-screen_height/2)>domain*domain:
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
      hcx=a[d*i]-screen_width/2+domain/2
      hcy=a[d*i+1]-screen_height/2
      if hcx*hcx+hcy*hcy>hipporadius*hipporadius and hcx*hcx+hcy*hcy<(hipporadius+radius)*(hipporadius+radius) and hippo1==1:
        n1=hcx
        n2=hcy
        nn=n1*n1+n2*n2
        v1x=a[d*i+2]
        v1y=a[d*i+3]
        a[d*i+2]=((n2*n2-e3*n1*n1)*v1x-(1+e3)*n1*n2*v1y)/nn
        a[d*i+3]=(-(1+e3)*n1*n2*v1x+(n1*n1-e3*n2*n2)*v1y)/nn
        a[d*i]=a[d*i]+(0+radius+hipporadius-sqrt(nn))*n1/sqrt(nn)
        a[d*i+1]=a[d*i+1]+(0+radius+hipporadius-sqrt(nn))*n2/sqrt(nn)
      if (a[d*i]-screen_width/2+domain/2)*(a[d*i]-screen_width/2+domain/2)+(a[d*i+1]-screen_height/2)*(a[d*i+1]-screen_height/2)<hipporadius*hipporadius and hippo1==1:
        a[d*i]=1000000
        a[d*i+1]=1000000
        a[d*i+2]=0
        a[d*i+3]=0
        team=int(i/n)
        if team==0:
          sr=sr-1
          bluecount=bluecount-1
        elif team==1:
          sr=sr-1
          bluecount=bluecount-1
        elif team==2:
          sr=sr+3
          redcount=redcount-1
        elif team==3:
          sr=sr-1
          redcount=redcount-1
        elif team==4:
          sr=-100
          gameend=1
          print("Blue team wins!")
      hcx=a[d*i]-screen_width/2
      hcy=a[d*i+1]-screen_height/2+domain/2
      if hcx*hcx+hcy*hcy>hipporadius*hipporadius and hcx*hcx+hcy*hcy<(hipporadius+radius)*(hipporadius+radius) and hippo2==1:
        n1=hcx
        n2=hcy
        nn=n1*n1+n2*n2
        v1x=a[d*i+2]
        v1y=a[d*i+3]
        a[d*i+2]=((n2*n2-e3*n1*n1)*v1x-(1+e3)*n1*n2*v1y)/nn
        a[d*i+3]=(-(1+e3)*n1*n2*v1x+(n1*n1-e3*n2*n2)*v1y)/nn
        a[d*i]=a[d*i]+(0+radius+hipporadius-sqrt(nn))*n1/sqrt(nn)
        a[d*i+1]=a[d*i+1]+(0+radius+hipporadius-sqrt(nn))*n2/sqrt(nn)
      if (a[d*i]-screen_width/2)*(a[d*i]-screen_width/2)+(a[d*i+1]-screen_height/2+domain/2)*(a[d*i+1]-screen_height/2+domain/2)<hipporadius*hipporadius and hippo2==1:
        a[d*i]=1000000
        a[d*i+1]=1000000
        a[d*i+2]=0
        a[d*i+3]=0
        team=int(i/n)
        if team==0:
          sr=sr
          bluecount=bluecount-1
        elif team==1:
          sb=sb+1
          bluecount=bluecount-1
        elif team==2:
          sr=sr
          redcount=redcount-1
        elif team==3:
          sr=sr
          redcount=redcount-1
        elif team==4:
          sb=-100
          gameend=1
          print("Red team wins!")
          
      hcx=a[d*i]-screen_width/2
      hcy=a[d*i+1]-screen_height/2-domain/2
      if hcx*hcx+hcy*hcy>hipporadius*hipporadius and hcx*hcx+hcy*hcy<(hipporadius+radius)*(hipporadius+radius) and hippo3==1:
        n1=hcx
        n2=hcy
        nn=n1*n1+n2*n2
        v1x=a[d*i+2]
        v1y=a[d*i+3]
        a[d*i+2]=((n2*n2-e3*n1*n1)*v1x-(1+e3)*n1*n2*v1y)/nn
        a[d*i+3]=(-(1+e3)*n1*n2*v1x+(n1*n1-e3*n2*n2)*v1y)/nn
        a[d*i]=a[d*i]+(0+radius+hipporadius-sqrt(nn))*n1/sqrt(nn)
        a[d*i+1]=a[d*i+1]+(0+radius+hipporadius-sqrt(nn))*n2/sqrt(nn)
      if (a[d*i]-screen_width/2)*(a[d*i]-screen_width/2)+(a[d*i+1]-screen_height/2-domain/2)*(a[d*i+1]-screen_height/2-domain/2)<hipporadius*hipporadius and hippo3==1:
        a[d*i]=1000000
        a[d*i+1]=1000000
        a[d*i+2]=0
        a[d*i+3]=0
        team=int(i/n)
        if team==0:
          sr=sr
          bluecount=bluecount-1
        elif team==1:
          sr=sr
          bluecount=bluecount-1
        elif team==2:
          sr=sr
          redcount=redcount-1
        elif team==3:
          sr=sr+1
          redcount=redcount-1
        elif team==4:
          sr=-100
          gameend=1
          print("Blue team wins!")
      hcx=a[d*i]-screen_width/2-domain/2
      hcy=a[d*i+1]-screen_height/2
      if hcx*hcx+hcy*hcy>hipporadius*hipporadius and hcx*hcx+hcy*hcy<(hipporadius+radius)*(hipporadius+radius) and hippo4==1:
        n1=hcx
        n2=hcy
        nn=n1*n1+n2*n2
        v1x=a[d*i+2]
        v1y=a[d*i+3]
        a[d*i+2]=((n2*n2-e3*n1*n1)*v1x-(1+e3)*n1*n2*v1y)/nn
        a[d*i+3]=(-(1+e3)*n1*n2*v1x+(n1*n1-e3*n2*n2)*v1y)/nn
        a[d*i]=a[d*i]+(0+radius+hipporadius-sqrt(nn))*n1/sqrt(nn)
        a[d*i+1]=a[d*i+1]+(0+radius+hipporadius-sqrt(nn))*n2/sqrt(nn)
        
      if (a[d*i]-screen_width/2-domain/2)*(a[d*i]-screen_width/2-domain/2)+(a[d*i+1]-screen_height/2)*(a[d*i+1]-screen_height/2)<hipporadius*hipporadius and hippo4==1:
        a[d*i]=1000000
        a[d*i+1]=1000000
        a[d*i+2]=0
        a[d*i+3]=0
        team=int(i/n)
        if team==0:
          sb=sb+3
          bluecount=bluecount-1
        elif team==1:
          sb=sb-1
          bluecount=bluecount-1
        elif team==2:
          sb=sb-1
          redcount=redcount-1
        elif team==3:
          sb=sb-1
          redcount=redcount-1
        elif team==4:
          sb=-100
          gameend=1
          print("Red team wins!")
    color("rgba(255,0,0,1)")
    circle(screen_width/2-domain/2,screen_height/2,hipporadius)
    color("rgba(255,0,255,1)")
    circle(screen_width/2,screen_height/2-domain/2,hipporadius)
    color("rgba(255,100,0,1)")
    circle(screen_width/2,screen_height/2+domain/2,hipporadius)
    color("rgba(0,0,255,1)")
    circle(screen_width/2+domain/2,screen_height/2,hipporadius)
    
    if hippo1==1:
      color("rgba(255,0,0,1)")
      spot(screen_width/2-domain/2,screen_height/2,hipporadius)
      color("white")
      spot(screen_width/2-domain/2+hipporadius/3,screen_height/2+hipporadius/3,hipporadius/5)
      spot(screen_width/2-domain/2+hipporadius/3,screen_height/2-hipporadius/3,hipporadius/5)
      color("black")
      spot(screen_width/2-domain/2+1.2*hipporadius/3,screen_height/2+hipporadius/3,hipporadius/10)
      spot(screen_width/2-domain/2+1.2*hipporadius/3,screen_height/2-hipporadius/3,hipporadius/10)
    if hippo2==1:
      color("rgba(255,0,255,1)")
      spot(screen_width/2,screen_height/2-domain/2,hipporadius)
      color("white")
      spot(screen_width/2+hipporadius/3,screen_height/2-domain/2+hipporadius/3,hipporadius/5)
      spot(screen_width/2-hipporadius/3,screen_height/2-domain/2+hipporadius/3,hipporadius/5)
      color("black")
      spot(screen_width/2+hipporadius/3,screen_height/2-domain/2+1.2*hipporadius/3,hipporadius/10)
      spot(screen_width/2-hipporadius/3,screen_height/2-domain/2+1.2*hipporadius/3,hipporadius/10)
    if hippo3==1:
      color("rgba(255,100,0,1)")
      spot(screen_width/2,screen_height/2+domain/2,hipporadius)
      color("white")
      spot(screen_width/2-hipporadius/3,screen_height/2+domain/2-hipporadius/3,hipporadius/5)
      spot(screen_width/2+hipporadius/3,screen_height/2+domain/2-hipporadius/3,hipporadius/5)
      color("black")
      spot(screen_width/2-hipporadius/3,screen_height/2+domain/2-1.2*hipporadius/3,hipporadius/10)
      spot(screen_width/2+hipporadius/3,screen_height/2+domain/2-1.2*hipporadius/3,hipporadius/10)
    if hippo4==1:
      color("rgba(0,0,255,1)")
      spot(screen_width/2+domain/2,screen_height/2,hipporadius)
      color("white")
      spot(screen_width/2+domain/2-hipporadius/3,screen_height/2+hipporadius/3,hipporadius/5)
      spot(screen_width/2+domain/2-hipporadius/3,screen_height/2-hipporadius/3,hipporadius/5)
      color("black")
      spot(screen_width/2+domain/2-1.2*hipporadius/3,screen_height/2+hipporadius/3,hipporadius/10)
      spot(screen_width/2+domain/2-1.2*hipporadius/3,screen_height/2-hipporadius/3,hipporadius/10)
 
    color("red")  
    text(10,10,sr)
    color("blue")
    text(screen_width-100,10,sb)
    
    if redcount==0 or bluecount==0:
      gameend=1
      if sr>sb:
        print("Red team wins!")
      elif sb>sr:
        print("Blue team wins!")
      else:
        print("Draw!")