import pybullet as p
import time
import math
import numpy as np
from datetime import datetime
import pybullet_data


def MakeArena(x,y,z=0.5,scale_x=0.5,scale_y=1,scale_z=0.5,Inter_area_dist=1,pickAreaHeight=0.9):
	p.setAdditionalSearchPath(pybullet_data.getDataPath())

	#boundary_c=p.createCollisionShape(p.GEOM_BOX,halfExtents=[scale_x/50,scale_y,0.02])
	#boundary_v=p.createVisualShape(p.GEOM_BOX,halfExtents=[scale_x/50,scale_y,0.02],rgbaColor=[0,0,1,1])

	pick_c=p.createCollisionShape(p.GEOM_BOX,halfExtents=[scale_x,scale_y,pickAreaHeight/2.0])
	pick_v=p.createVisualShape(p.GEOM_BOX,halfExtents=[scale_x,scale_y,pickAreaHeight/2.0],rgbaColor=[1,0,1,1])
	y_pick = y - scale_y - Inter_area_dist/2.0
	

