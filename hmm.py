import csv
import numpy as np
import warnings
from hmmlearn import hmm
from matplotlib import pyplot as plt

# There are annoying sklearn DeprecationWarnings, we silence them here.
def warn(*args, **kwargs):
    pass
warnings.warn = warn

def get_emitted_data(filepath='Q1/chromosome1.tsv'):
	""" Returns a numpy array, where each entry is [chromosome position, DamID data] """
	X = []
	with open(filepath, 'r') as csvfile:
	    reader = csv.reader(csvfile, delimiter='\t')
	    for row in reader:
	        X.append(np.array([_ for _ in map(float, row)]))
	return np.array(X)

def get_ground_truth(filepath='Q1/chromosome1_lads.tsv'):
	""" Returns a numpy array, where each entry is [start_site, end_site] """
	Z = []
	with open(filepath, 'r') as csvfile:
	    reader = csv.reader(csvfile, delimiter='\t')
	    for row in reader:
	        Z.append(np.array([_ for _ in map(float, row)]))
	return np.array(Z)

def count_correct(predicted_states, ground_truth):
	""" Predicted states is a numpy array, where each entry is [chromosome position, predicted state]
		ground_truth is a numpy array, where each entry is [start_site, end_site] """

	return 0.0

GHMM = hmm.GaussianHMM(n_components=2)
emissions = get_emitted_data()
signals = emissions[:,1][np.newaxis].transpose()

GHMM.fit(signals)

states = GHMM.predict(signals)

state_data = (emissions[np.where(states==0)], emissions[np.where(states==1)])
colors = ((0.35, 0.15, 1.0), (1.0, 0.15, 0.35))

plt.title('2 State HMM Predicted States and DamID Values')
plt.xlabel('Chromosome Position')
plt.ylabel('DamID Value')
for i, state in enumerate(state_data):
	plt.plot(state[:,0], state[:,1], '.', linewidth=1, color=colors[i], label='State ' + str(i))
plt.legend()
plt.show()