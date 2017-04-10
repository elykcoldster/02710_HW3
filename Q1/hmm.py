import csv
import numpy as np
import warnings
from hmmlearn import hmm
from matplotlib import pyplot as plt

# There are annoying sklearn DeprecationWarnings, we silence them here.
def warn(*args, **kwargs):
    pass
warnings.warn = warn

def get_emitted_data():
	""" Returns a numpy array, where each entry is [chromosome position, DamID data] """
	X = []
	with open("chromosome1.tsv", 'r') as csvfile:
	    reader = csv.reader(csvfile, delimiter='\t')
	    for row in reader:
	        X.append(np.array([_ for _ in map(float, row)]))
	return np.array(X)


def get_ground_truth():
	""" Returns a numpy array, where each entry is [start_site, end_site] """
	Z = []
	with open("chromosome1_lads.tsv", 'r') as csvfile:
	    reader = csv.reader(csvfile, delimiter='\t')
	    for row in reader:
	        Z.append(np.array([_ for _ in map(float, row)]))
	return np.array(Z)

def count_correct(predicted_states, ground_truth):
	""" Predicted states is a numpy array, where each entry is [chromosome position, predicted state]
		ground_truth is a numpy array, where each entry is [start_site, end_site] """

	return 0.0
