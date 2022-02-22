# Import necessary modules
import math
import numpy as np


# Define function to calculate a single homogeneous transformation:
def dh_transformation(DH):
	# NOTE: assumes DH is a list in order [theta, Ai, Di, alpha] as in the lecture powerpoint
	
	# Get variables from input:
	theta = DH[0]# link length
	Ai = DH[1] # link twist
	Di = DH[2] # joint angle
	alpha = DH[3] # link offset
	
	# Calculate combined homogenous transformation:
	DH = np.array([[math.cos(theta), (-math.sin(theta)*math.cos(alpha)), (math.sin(theta)*math.sin(alpha)), Ai*math.cos(theta)],
				   [math.sin(theta), (math.cos(theta)*math.cos(alpha)), (-math.cos(theta)*math.sin(alpha)), Ai*math.sin(theta)],
				   [0, 				  math.sin(alpha), 					 math.cos(alpha), 					Di],
				   [0, 				  0, 								 0, 								1]])
							   

	return DH

# Define function to calculate total homogenenous transformation for a kinematic chain:
def kinematic_chain(DH):
	
	# Initialize total transformation:
	total_trans = np.identity(4)
	
	for row in DH: # Get data for each individual segment
		# NOTE: Assumes row is in order [theta, Ai, Di, alpha] as in the lecture powerpoint
		
		# Calculate homogeneous transformation for each row and multiply all transformations together:
		total_trans = np.matmul(total_trans, dh_transformation(row))
	
	# Return the total homogeneous transformation:
	return total_trans
	

# Define a function to get positions from a homogeneous transformation:
def get_pos(trans):

	# Get positions:
	x = trans[0][3] # accessing values in array as trans[row][column]
	y = trans[1][3]
	z = trans[2][3]
	
	# Return a tuple of the three coordinates:
	return x, y, z


# Define a function to get orientation information from a homogeneous transformation:
def get_rot(trans):
	
	# Calculate roll:
	psi = math.atan2(trans[2][1] , trans[2][2])
	# Calculate pitch:
	theta = math.atan2(-trans[2][0] , math.sqrt( (trans[2][1] ** 2) + (trans[2][2] ** 2) ) )
	# Calculate yaw: 
	phi = math.atan2(trans[1][0] , trans[0][0])
	
	# Formulas from lab sheet
	
	# Return a tuple of the three orientations:
	return psi, theta, phi
	
	
