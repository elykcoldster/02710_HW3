import numpy as np
import matplotlib.pyplot as plt
from scipy.io import savemat
from scipy.sparse import coo_matrix

def load_hic(filename='combined_50Kb.txt', res=50000):
	hic_file = open(filename, 'r')
	hic_data = np.loadtxt(hic_file)

	row = hic_data[:,0]/res
	col = hic_data[:,1]/res
	data = hic_data[:,2]

	nrow = row[-1] + 1
	ncol = col[-1] + 1

	hic_matrix = coo_matrix((data, (row, col)), shape=(nrow, ncol)).toarray()

	return hic_matrix

hic_matrix = load_hic()
savemat('hic_matrix.mat', {'hic': hic_matrix})