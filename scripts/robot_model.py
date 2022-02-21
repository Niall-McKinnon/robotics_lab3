# Import necessary modules
import math
import numpy as np

# example = [5, 10, 15, 20] # random values for testing purposes

def dh_transformation(DH):
	# NOTE: assumes DH is in order [theta, Ai, Di, alpha] as in the lecture powerpoint
	
	# Get variables from input:
	Ai = DH[0]# link length
	alpha = DH[1] # link twist
	theta = DH[2] # joint angle
	Di = DH[3] # link offset
	
	# Generate combined homogenous transformation:
	DH = np.array([[math.cos(theta), (-math.sin(theta)*math.cos(alpha)), (math.sin(theta)*math.sin(alpha)), Ai*math.cos(theta)],
				   [math.sin(theta), (math.cos(theta)*math.cos(alpha)), (-math.cos(theta)*math.sin(alpha)), Ai*math.sin(theta)],
				   [0, 				  math.sin(alpha), 					 math.cos(alpha), 					Di],
				   [0, 				  0, 								 0, 								1]])
							   

	return DH

# testing:
example = [5, 10, 15, 20] # random values for testing purposes
# print(dh_transformation(example))

def kinematic_chain(DH):
	
	# Initialize total transformation:
	total_trans = np.identity(4)
	
	for row in DH: # Get data for each individual segment
		# NOTE: Assumes row is in order [theta, Ai, Di, alpha] as in the lecture powerpoint
		total_trans = np.matmul(total_trans, dh_transformation(row))
	
	return total_trans
	
# Testing:
# params = np.array([[0, 0, 0.1625, math.pi/2], [0, -0.425, 0, 0], [0, -0.3922, 0, 0], [0, 0, 0.1333, math.pi/2], [0, 0, 0.0977, -math.pi/2]])
# print(kinematic_chain(params))

def get_pos(trans):

	# Get positions:
	x = trans[0][3] # accessing values in array as trans[row][column]
	y = trans[1][3]
	z = trans[2][3]
	
	return x, y, z

# testing:
# print(get_pos(dh_transformation(example)))

def get_rot(trans):
	
	# Calculate roll:
	psi = math.atan(trans[2][1] / trans[2][2])
	# Calculate pitch:
	theta = math.atan(-trans[2][0] / math.sqrt( (trans[2][1] ** 2) + (trans[2][2] ** 2) ) )
	# Calculate yaw: 
	phi = math.atan(trans[1][0] / trans[0][0])
	
	# Formulas from lab sheet
	
	return psi, theta, phi

# testing:
# print(get_rot(dh_transformation(example)))
	
	
