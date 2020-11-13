import random
import pybullet as p
import pybullet_data
import time 
import math
p.connect(p.GUI)
p.loadURDF("%s/plane.urdf" % pybullet_data.getDataPath())
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

def archimed_spiral_param(t,a):
    x = a*t*math.cos(t)
    y = a*t*math.sin(t)
    z = 0.5*a*t
    return [x,y,z]

for i in range(1000):
    random_id = random.randint(0,1000)   
    try:
        p.loadURDF('random_urdfs/'+ str(random_id)+'/'+ str(random_id)+'.urdf',archimed_spiral_param(i*0.1,0.1))
    except:
        pass
    p.stepSimulation()
    time.sleep(0.01)
  