# Import neccessary modules
import math
import numpy as np
import robot_model as rm

if __name__ == '__main__':
	
	# Problem 2a:
	
	# define parameters using order [theta, Ai, Di, alpha]:
	links = [[math.pi/2, 1, 0, 0], [math.pi/2, 1, 0, 0]] 
	# reference lecture slide 32
	
	# generate homogeneous transformation:
	transformation = rm.kinematic_chain(links)
	
	# get position and rotation:
	pos = rm.get_pos(transformation)
	rot = rm.get_rot(transformation)
	
	print(pos)
	print(rot)
	
	
	
