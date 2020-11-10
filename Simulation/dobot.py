import pybullet as p
import pybullet_data
import numpy as np
import math
import time

class DobotEnv():

	def __init__(self):
		p.connect(p.GUI)
		p.setGravity(0,0,-10)
		self.plane = p.loadURDF("%s/plane.urdf" % pybullet_data.getDataPath())
		self.dobot = p.loadURDF("rsc/dobot/dobot.urdf",useFixedBase=True,globalScaling=1)
		c = p.createConstraint(self.dobot,6,self.dobot,8,jointType=p.JOINT_POINT2POINT,jointAxis =[1,0,0],parentFramePosition=[-0.05,0,0.08],childFramePosition=[-0.05,0.026,-0.006])#0.014-0.02 (inertial com)
		c = p.createConstraint(self.dobot,3,self.dobot,5,jointType=p.JOINT_POINT2POINT,jointAxis =[1,0,0],parentFramePosition=[-0.05,0,0.075],childFramePosition=[-0.05,-0.026,0.014])
		# to create a pick table
		scale_x =0.1
		scale_y =0.1
		pickAreaHeight = 0.15
		table_pos = [0,0.2,pickAreaHeight/2]

		

		pick_c=p.createCollisionShape(p.GEOM_BOX,halfExtents=[scale_x,scale_y,pickAreaHeight/2.0])
		pick_v=p.createVisualShape(p.GEOM_BOX,halfExtents=[scale_x,scale_y,pickAreaHeight/2.0],rgbaColor=[1,0,1,1])
		multi=p.createMultiBody(baseCollisionShapeIndex=pick_c,baseVisualShapeIndex=pick_v,basePosition=table_pos)

	def print_joint_info(self):
		for i in range (p.getNumJoints(self.dobot)):
			print(p.getJointInfo(self.dobot,i))


	def step(self):
		self.set_motor_commands()
		p.stepSimulation()

	def set_motor_commands(self):
		p.setJointMotorControl2(self.dobot,0,p.VELOCITY_CONTROL,targetVelocity=0,force=1000)
		p.setJointMotorControl2(self.dobot,3,p.VELOCITY_CONTROL,targetVelocity=0,force=0)
		p.setJointMotorControl2(self.dobot,5,p.VELOCITY_CONTROL,targetVelocity=0,force=0)
		p.setJointMotorControl2(self.dobot,6,p.VELOCITY_CONTROL,targetVelocity=0,force=0)
		p.setJointMotorControl2(self.dobot,8,p.VELOCITY_CONTROL,targetVelocity=0,force=0)

	def reset(self):
		# function to reset the robot and environment to initial state
		pass

	def get_camera_image(self):
		# function to get a over head camera image
		# p.getCameraImage(320,200)#160,100)
		pass

	def load_and_objects(self):
		# to load random object urdf's
		pass

if __name__ == "__main__":
	env = DobotEnv()
	while(1):
		env.step()