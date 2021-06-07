from vpython import *
#GlowScript 3.1 VPython
#create our sphere
ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.green, make_trail=True)
ball2 = sphere(pos=vector(5,0,0), radius=0.5, color=color.yellow, make_trail=True)
#create our wall, there are nine colors  red, green, blue, yellow, magenta,
#cyan, orange, black, and white.
wallR = box(pos=vector(6,0,0), size=vector(.5,12,12.5), color=color.blue)
wallL = box(pos=vector(-6,0,0), size=vector(.5,12,12.5), color=color.blue)
wallBK = box(pos=vector(0,0,-6), size=vector(12,12,.5), color=color.red)
wallT = box(pos=vector(0,6,0), size=vector(12.5,.5,12.5), color=color.green)
wallBT = box(pos=vector(0,-6,0), size=vector(12.5,.5,12.5), color=color.green)
#give our ball velocity
ball.velocity = vector(25,10,-12)
ball2.velocity = vector(15,15,7)
#our dt is showing how much we are changing
dt = 0.005
#time starts at 0
t = 0
#velocity arrow visual with scaler to make arrow correct size
vscale = 0.1
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow)
varr2 = arrow(pos=ball2.pos, axis=vscale*ball2.velocity, color=color.yellow)
#we update position based on velocity and change
scene.autoscale = True 
while t<1000000:
    rate(100)
    randnum = random()
#    controls right and left wall bounce
    if (ball.pos.x + .5) > (wallR.pos.x - .5):
        ball.velocity.x = -ball.velocity.x
        ball.color=color.cyan
    if (ball.pos.x - .5) < (wallL.pos.x + .5):
        ball.velocity.x = -ball.velocity.x
        ball.color=color.green
        

    if (ball2.pos.x + .5) > (wallR.pos.x - .5):
        ball2.velocity.x = -ball2.velocity.x
        ball2.color=color.red
    if (ball2.pos.x - .5) < (wallL.pos.x + .5):
        ball2.velocity.x = -ball2.velocity.x
        ball2.color=color.yellow
#    controls front and back wall bounce 
    if (ball.pos.z - .5) < (wallBK.pos.z + .5):
        ball.velocity.z = -ball.velocity.z
        ball.color=color.orange
    if (ball.pos.z + .5) > (-wallBK.pos.z - .5):
        ball.velocity.z = -ball.velocity.z
        ball.color=color.yellow
    
    if (ball2.pos.z - .5) < (wallBK.pos.z + .5):
        ball2.velocity.z = -ball2.velocity.z
        ball.color=color.purple
    if (ball2.pos.z + .5) > (-wallBK.pos.z - .5):
        ball2.velocity.z = -ball2.velocity.z
        ball.color=color.white
#    controls top and bottom wall bounce
    if (ball.pos.y + .5) > (wallT.pos.y - .5):
        ball.velocity.y = -ball.velocity.y
        ball.color=color.green
    if (ball.pos.y - .5) < (wallL.pos.x + .5):
        ball.velocity.y = -ball.velocity.y
        ball.color=color.green
        
    if (ball2.pos.y + .5) > (wallT.pos.y - .5):
        ball2.velocity.y = -ball2.velocity.y
        ball2.color=color.black
    if (ball2.pos.y - .5) < (wallL.pos.x + .5):
        ball2.velocity.y = -ball2.velocity.y
        ball2.color=color.cyan
#        updating balls position and arrrow position
    ball.pos = ball.pos + ball.velocity*dt
    varr.pos=ball.pos
    varr.axis=ball.velocity*vscale
    
    ball2.pos = ball2.pos + ball2.velocity*dt
    varr2.pos=ball2.pos
    varr2.axis=ball2.velocity*vscale
    t = t + dt
   
