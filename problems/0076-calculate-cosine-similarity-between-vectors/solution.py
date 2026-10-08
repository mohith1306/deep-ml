import numpy as np
import math
def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	suma=0
	sumb=0
	tsum=0
	for i in range(len(v1)):
		tsum+=v1[i]*v2[i]
	for i in v1:
		suma+=i*i
	for i in v2:
		sumb+=i*i
	return tsum/(math.sqrt(suma)*math.sqrt(sumb))
	pass