# By CAMbassador James

from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import (sin, cos, pi, sqrt)

from tealight.art import screen_width, screen_height

from random import (random, randint)

from tealight.utils import sleep

balls=[]
n=5
s1=15
e=0.9
e2=1
e3=1
g=0
mu=0
nom=10

redcount=2*n
bluecount=2*n
domain=min(screen_width,screen_height)/2-10
radius=domain/12
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

class Vector:
  x = None
  y = None
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
  
  def __iadd__(self, other):
    self.x += other.x
    self.y += other.y
    return self
  
  def __sub__(self, other):
    return Vector(self.x - other.x, self.y - other.y)
  
  def __mul__(self,other):
    return self.x*other.x + self.y*other.y
  
  def scale(self,factor):
    return Vector(self.x*factor,self.y*factor)
  
  def mod(self):
    return sqrt(self.x**2 + self.y**2)
  def __str__(self):
    return "%s,%s" % (self.x, self.y)
  
  
class Ball:
  position = None
  velocity = None
  colour = None
  def __init__(self,position,velocity,colour):
    self.position = position
    self.velocity = velocity
    self.colour = colour
    
  def __str__(self):
    return "Ball at %s, velocity %s, color%s" % (self.position, self.velocity, self.colour)
    


for i in range (0,4*n+1):
  c=1
  r5=randint(domain/3,domain)
  r6=randint(0,100)*(360)/100
  r1=r5*cos(r6)+screen_width/2
  r2=r5*sin(r6)+screen_height/2
  r3=randint(0,s1*100)/100-s1/2
  r4=randint(0,s1*100)/100-s1/2
  balls.append(Ball(Vector(r1,r2),Vector(r3,r4),None))
  if i<n:
    balls[i].colour = (0,0,255,1)
  elif  i<2*n:
    balls[i].colour = (255,0,255,1)
  elif i < 3*n:
    balls[i].colour = (255,0,0,1)
  elif i<4*n:
    balls[i].colour = (255,100,0,1)
  else: # Danger Ball
    balls[i].colour = (0,0,0,1)
  

  print balls[-1]


def ctorgba(c):
  r,g,b,a = c
  string_out = "rgba("
  string_out = string_out + str(r) + "," + str(g) + "," + str(b) + "," + str(a) + ")"
  return string_out

def handle_keydown(key):
  global hippo1, hippo2, hippo3, hippo4
  if key == "left":
    hippo1=2
  elif key == "up":
    hippo2=2
  elif key == "down":
    hippo3=2
  elif key == "right":
    hippo4=2

    
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
  global balls, sr, sb, gameend, e3, redcount, bluecount, hippo1, hippo2, hippo3, hippo4
  if gameend==0:
    
    sleep(20)
    color("white")
    box(0,0,screen_width,screen_height)
    color("black")
    circle(screen_width/2,screen_height/2,domain+radius)
    color("rgba(255,0,0,1)")
    circle(screen_width/2-domain/2,screen_height/2,hipporadius)
    color("rgba(255,0,255,1)")
    circle(screen_width/2,screen_height/2-domain/2,hipporadius)
    color("rgba(255,100,0,1)")
    circle(screen_width/2,screen_height/2+domain/2,hipporadius)
    color("rgba(0,0,255,1)")
    circle(screen_width/2+domain/2,screen_height/2,hipporadius)
    
    for ball in balls:
      #a[d*i+8]=-a[d*i]/1000
      #a[d*i+9]=-a[d*i+1]/1000
      ball.position = ball.position + ball.velocity
    
      
      # TODO: Acceleration
      #a1=a[d*i]-screen_width/2
      #a2=a[d*i+1]-screen_height/2
      #aa=sqrt(a1*a1+a2*a2)
      #a[d*i+8]=-mu*a[d*i+2]-g*a1/aa
      #a[d*i+9]=-mu*a[d*i+3]-g*a2/aa
      #if a[d*i]<screen_width:
      #  a[d*i+2]=a[d*i+2]*1+a[d*i+8]
      #  a[d*i+3]=a[d*i+3]*1+a[d*i+9]
     
    
    
    for i in range (0,len(balls)):
      for j in range (i+1,len(balls)):
        
        normal = balls[i].position - balls[j].position
        
        nn=normal.mod()
        
        if nn<2*radius:
          if nn !=0:
            
            # rotate so colission along x
            tangent=Vector(-normal.y,normal.x)
            
            v3 = Vector(normal * balls[i].velocity,
                        tangent * balls[i].velocity)
            v4 = Vector(normal * balls[j].velocity,
                        tangent * balls[j].velocity)
            
            
            
            v5x=0.5*((1-e)*v3.x+(1+e)*v4.x)
            v6x=0.5*((1-e)*v4.x+(1+e)*v3.x)
            
            balls[i].velocity = \
                  Vector((normal.x*v5x-normal.y*v3.y)/nn**2,
                         (normal.y*v5x+normal.x*v3.y)/nn**2)
            balls[j].velocity = \
                  Vector((normal.x*v6x-normal.y*v4.y)/nn**2,
                         (normal.y*v6x+normal.x*v4.y)/nn**2)
           
            
             
            
            balls[i].position += normal.scale((2*radius-nn) / (2 * nn))
            balls[j].position += normal.scale(-(2*radius-nn) / (2 * nn))
            
            
      
              
      #if (a[d*i]-screen_width/2)*(a[d*i]-screen_width/2)+(a[d*i+1]-screen_height/2)*(a[d*i+1]-screen_height/2)>domain*domain and a[d*i]<screen_width:
        #print(i)
      #  n1=-(a[d*i]-screen_width/2)
      #  n2=-(a[d*i+1]-screen_height/2)
      #  v1x=a[d*i+2]
      #  v1y=a[d*i+3]
      #  nn=n1*n1+n2*n2
      #  a[d*i+2]=((n2*n2-e2*n1*n1)*v1x-(1+e2)*n1*n2*v1y)/nn
      #  a[d*i+3]=(-(1+e2)*n1*n2*v1x+(n1*n1-e2*n2*n2)*v1y)/nn
      #  a[d*i]=a[d*i]+(1-domain+sqrt(nn))*n1/sqrt(nn)
      #  a[d*i+1]=a[d*i+1]+(1-domain+sqrt(nn))*n2/sqrt(nn)
      
      
      
      #hcx=a[d*i]-screen_width/2+domain/2
      #hcy=a[d*i+1]-screen_height/2
      #if hcx*hcx+hcy*hcy>hipporadius*hipporadius and hcx*hcx+hcy*hcy<(hipporadius+radius)*(hipporadius+radius) and hippo1>1:
      #  print(i)
      #  a[d*i+2]=nom*a[d*i+2]
      #  a[d*i+3]=nom*a[d*i+3]
        
      #if hippo1>1:
      #  hippo1=hippo1-1
      #if hippo2==2:
      #  hippo2=1
      #if hippo3==2:
      #  hippo3=1
      #if hippo4==2:
      #  hippo4=1
      #if hcx*hcx+hcy*hcy>hipporadius*hipporadius and hcx*hcx+hcy*hcy<(hipporadius+radius)*(hipporadius+radius) and hippo1>0:
      #  n1=hcx
      #  n2=hcy
      #  nn=n1*n1+n2*n2
      #  v1x=a[d*i+2]
      #  v1y=a[d*i+3]
      #  a[d*i+2]=((n2*n2-e3*n1*n1)*v1x-(1+e3)*n1*n2*v1y)/nn
      #  a[d*i+3]=(-(1+e3)*n1*n2*v1x+(n1*n1-e3*n2*n2)*v1y)/nn
      #  a[d*i]=a[d*i]+(0+radius+hipporadius-sqrt(nn))*n1/sqrt(nn)
      #  a[d*i+1]=a[d*i+1]+(0+radius+hipporadius-sqrt(nn))*n2/sqrt(nn)
      #if (a[d*i]-screen_width/2+domain/2)*(a[d*i]-screen_width/2+domain/2)+(a[d*i+1]-screen_height/2)*(a[d*i+1]-screen_height/2)<hipporadius*hipporadius and hippo1==1:
      #  a[d*i]=screen_width+100
      #  a[d*i+1]=screen_height+100
      #  a[d*i+2]=0
      #  a[d*i+3]=0
      #  team=int(i/n)
      #  if team==0:
      #    sr=sr-1
      #    bluecount=bluecount-1
      #  elif team==1:
      #    sr=sr-1
      #    bluecount=bluecount-1
      #  elif team==2:
      #    sr=sr+3
      #    redcount=redcount-1
      #  elif team==3:
      #    sr=sr-1
      #    redcount=redcount-1
      #  elif team==4:
      #    sr=-100
      #    gameend=1
      #    print("Blue team wins!")
      #hcx=a[d*i]-screen_width/2
      #hcy=a[d*i+1]-screen_height/2+domain/2
      #if hcx*hcx+hcy*hcy>hipporadius*hipporadius and hcx*hcx+hcy*hcy<(hipporadius+radius)*(hipporadius+radius) and hippo2==1:
      #  n1=hcx
      #  n2=hcy
      #  nn=n1*n1+n2*n2
      #  v1x=a[d*i+2]
      #  v1y=a[d*i+3]
      #  a[d*i+2]=((n2*n2-e3*n1*n1)*v1x-(1+e3)*n1*n2*v1y)/nn
      #  a[d*i+3]=(-(1+e3)*n1*n2*v1x+(n1*n1-e3*n2*n2)*v1y)/nn
      #  a[d*i]=a[d*i]+(0+radius+hipporadius-sqrt(nn))*n1/sqrt(nn)
      #  a[d*i+1]=a[d*i+1]+(0+radius+hipporadius-sqrt(nn))*n2/sqrt(nn)
      #if (a[d*i]-screen_width/2)*(a[d*i]-screen_width/2)+(a[d*i+1]-screen_height/2+domain/2)*(a[d*i+1]-screen_height/2+domain/2)<hipporadius*hipporadius and hippo2==1:
      #  a[d*i]=1000000
      #  a[d*i+1]=1000000
      #  a[d*i+2]=0
      #  a[d*i+3]=0
      #  team=int(i/n)
      #  if team==0:
      #    sr=sr
      #    bluecount=bluecount-1
      #  elif team==1:
      #    sb=sb+1
      #    bluecount=bluecount-1
      #  elif team==2:
      #    sr=sr
      #    redcount=redcount-1
      #  elif team==3:
      #    sr=sr
      #    redcount=redcount-1
      #  elif team==4:
      #    sb=-100
      #    gameend=1
      #    print("Red team wins!")
      #    
      #hcx=a[d*i]-screen_width/2
      #hcy=a[d*i+1]-screen_height/2-domain/2
      #if hcx*hcx+hcy*hcy>hipporadius*hipporadius and hcx*hcx+hcy*hcy<(hipporadius+radius)*(hipporadius+radius) and hippo3==1:
      #  n1=hcx
      #  n2=hcy
      #  nn=n1*n1+n2*n2
      #  v1x=a[d*i+2]
      #  v1y=a[d*i+3]
      #  a[d*i+2]=((n2*n2-e3*n1*n1)*v1x-(1+e3)*n1*n2*v1y)/nn
      #  a[d*i+3]=(-(1+e3)*n1*n2*v1x+(n1*n1-e3*n2*n2)*v1y)/nn
      #  a[d*i]=a[d*i]+(0+radius+hipporadius-sqrt(nn))*n1/sqrt(nn)
      #  a[d*i+1]=a[d*i+1]+(0+radius+hipporadius-sqrt(nn))*n2/sqrt(nn)
      #if (a[d*i]-screen_width/2)*(a[d*i]-screen_width/2)+(a[d*i+1]-screen_height/2-domain/2)*(a[d*i+1]-screen_height/2-domain/2)<hipporadius*hipporadius and hippo3==1:
      #  a[d*i]=1000000
      #  a[d*i+1]=1000000
      #  a[d*i+2]=0
      #  a[d*i+3]=0
      #  team=int(i/n)
      #  if team==0:
      #    sr=sr
      #    bluecount=bluecount-1
      #  elif team==1:
      #    sr=sr
      #    bluecount=bluecount-1
      #  elif team==2:
      #    sr=sr
      #    redcount=redcount-1
      #  elif team==3:
      #    sr=sr+1
      #    redcount=redcount-1
      #  elif team==4:
      #    sr=-100
      #    gameend=1
      #    print("Blue team wins!")
      #hcx=a[d*i]-screen_width/2-domain/2
      #hcy=a[d*i+1]-screen_height/2
      #if hcx*hcx+hcy*hcy>hipporadius*hipporadius and hcx*hcx+hcy*hcy<(hipporadius+radius)*(hipporadius+radius) and hippo4==1:
      #  n1=hcx
      #  n2=hcy
      #  nn=n1*n1+n2*n2
      #  v1x=a[d*i+2]
      #  v1y=a[d*i+3]
      #  a[d*i+2]=((n2*n2-e3*n1*n1)*v1x-(1+e3)*n1*n2*v1y)/nn
      #  a[d*i+3]=(-(1+e3)*n1*n2*v1x+(n1*n1-e3*n2*n2)*v1y)/nn
      #  a[d*i]=a[d*i]+(0+radius+hipporadius-sqrt(nn))*n1/sqrt(nn)
      #  a[d*i+1]=a[d*i+1]+(0+radius+hipporadius-sqrt(nn))*n2/sqrt(nn)
      #  
      #if (a[d*i]-screen_width/2-domain/2)*(a[d*i]-screen_width/2-domain/2)+(a[d*i+1]-screen_height/2)*(a[d*i+1]-screen_height/2)<hipporadius*hipporadius and hippo4==1:
      #  a[d*i]=1000000
      #  a[d*i+1]=1000000
      #  a[d*i+2]=0
      #  a[d*i+3]=0
      #  team=int(i/n)
      #  if team==0:
      #    sb=sb+3
      #    bluecount=bluecount-1
      #  elif team==1:
      #    sb=sb-1
      #    bluecount=bluecount-1
      #  elif team==2:
      #    sb=sb-1
      #    redcount=redcount-1
      #  elif team==3:
      #    sb=sb-1
      #    redcount=redcount-1
      #  elif team==4:
      #    sb=-100
      #    gameend=1
      #    print("Red team wins!")
    for i, ball in enumerate(balls):
      color(ctorgba(ball.colour))
      spot(ball.position.x, ball.position.y, radius)
    if i==4*n:
      color("white")
      text(ball.position.x-3, ball.position.y-12,"!")
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