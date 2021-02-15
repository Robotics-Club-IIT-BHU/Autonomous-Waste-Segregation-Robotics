import pybullet as p
import time
import math
import numpy as np
from datetime import datetime
import pybullet_data
import os

#p.connect(p.GUI)
def MakeArena(x,y,z=0.5,scale_x=0.5,scale_y=1,scale_z=0.5,Inter_area_dist=1,pickAreaHeight=0.9):
	p.setAdditionalSearchPath(pybullet_data.getDataPath())
	planeOrn = [0,0,0,1]
	planeId = p.loadURDF("plane.urdf", [0,0,0],planeOrn)

	
	#boxId = p.loadSDF(os.path.join("kuka_iiwa/kuka_with_gripper2.sdf"))
	d=1
	stool1=p.loadURDF("cube_small1.urdf",[0,d,0],globalScaling=8)
	stool2=p.loadURDF("cube_small1.urdf",[0,-d,0],globalScaling=8)
	stool3=p.loadURDF("cube_small1.urdf",[d,0,0],globalScaling=8)
	stool4=p.loadURDF("cube_small1.urdf",[-d,0,0],globalScaling=8)
	#ballId = p.loadSoftBody("ball.obj", simFileName = "ball.vtk", basePosition = [0.5,0.5,0.05], scale = 0.07, mass = 0.1, useNeoHookean = 1, NeoHookeanMu = 400, NeoHookeanLambda = 600, NeoHookeanDamping = 0.001, useSelfCollision = 1, frictionCoeff = .5, collisionMargin = 0.001)
	text=p.addUserDebugText("LDPE,HDPE",[-0.2,0.9,0.5],[1,0,0])
	text=p.addUserDebugText("HDPE,LDPE,PET",[1,0,0.5],[1,0,0])
	text=p.addUserDebugText("PVC,HDPE",[-1.3,-0.4,0.5],[1,0,0])
	text=p.addUserDebugText("POLYSTYRENE",[-0.2,-1.4,0.5],[1,0,0])
	car=p.loadURDF("bottle.urdf",[0.5,-0.5,0],globalScaling=0.02)

if __name__=='__main__':
	p.connect(p.GUI)
	MakeArena(x=0,y=0,z=-0.15,scale_x=0.3,scale_y=0.3,scale_z=0,Inter_area_dist=0.5,pickAreaHeight=0.5)
	p.resetDebugVisualizerCamera(1.3 , 0, -41, [0, 0, 0.5])
	time.sleep(10)