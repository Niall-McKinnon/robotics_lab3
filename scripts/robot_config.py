# Import neccessary modules
import math
import numpy as np
import robot_model as rm

# define a function to solve a case and print results:
def solve_problem(data):
	
	# Generate total homogeneous transformation:
	trans = rm.kinematic_chain(data)
	
	# get position and rotation:
	pos = rm.get_pos(trans)
	rot = rm.get_rot(trans)
	
	# print results:
	print('x, y, z positions are: {}'.format(pos))
	print('roll, pitch, yaw orientations are: {}'.format(rot))


if __name__ == '__main__':

	# Problem 2a:
	
	# define parameters using order [theta, Ai, Di, alpha]:
	data_2a = np.array([[math.pi/2, 1, 0, 0], [math.pi/2, 1, 0, 0]])
	# reference lecture slide 32
	
	print('\n===== Problem 2a: =====\n')
	solve_problem(data_2a) # The rotational output for this problem seems to be incorrect. I am not sure why, because the rotational outputs for Problem 2b all appear to be correct.
	
	# Problem 2b:
	
	# values from lecture slide 36
	case_1 = np.array([[0, 0, 0.1625, math.pi/2], [0, -0.425, 0, 0], [0, -0.3922, 0, 0], [0, 0, 0.1333, math.pi/2], [0, 0, 0.0977, -math.pi/2], [0, 0, 0.0996, 0]])
	case_2 = np.array([[0, 0, 0.1625, math.pi/2], [-math.pi/2, -0.425, 0, 0], [0, -0.3922, 0, 0], [0, 0, 0.1333, math.pi/2], [0, 0, 0.0977, -math.pi/2], [0, 0, 0.0996, 0]])
	
	print('\n===== Problem 2b, Case 1: =====\n')
	solve_problem(case_1)
	
	print('\n===== Problem 2b, Case 2: =====\n')
	solve_problem(case_2)
	
	
