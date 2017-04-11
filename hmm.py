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
	corr_states = [0, 1]
	num_corr = [0, 0]
    
	locations = predicted_states[:,0]

	for i, corr_state in enumerate(corr_states):
		for n in range(0, len(ground_truth)):
			lower = np.where(locations >= ground_truth[n,0])
			upper = np.where(locations <= ground_truth[n,1])
			lad_locs = np.intersect1d(upper, lower)
			
			for lad_loc in lad_locs:
				if predicted_states[lad_loc, 1] == corr_state:
					num_corr[i] += 1
	return max(num_corr)

GHMM = hmm.GaussianHMM(n_components=2)
emissions = get_emitted_data()
ground_truth = get_ground_truth()
signals = emissions[:,1][np.newaxis].transpose()

GHMM.fit(signals)

states = GHMM.predict(signals)

state_data = (emissions[np.where(states==0)], emissions[np.where(states==1)])

# Get maximum score
num_correct = count_correct(np.stack([emissions[:,0], states]).transpose(), ground_truth)

print("Maximum score:")
print(num_correct)

# Get BIC
BIC_array = []
for k in range(2,16):
	GHMM = hmm.GaussianHMM(n_components=k)
	GHMM.fit(signals)
	
	l = GHMM.score(signals)
	p = k*(k+1)

	BIC = -2*l + p*np.log(len(signals))
	BIC_array.append(BIC)
	print('k = {0}: {1}'.format(k, BIC))
print('Optimal BIC: {0}: {1}'.format(np.argmin(BIC_array) + 2, min(BIC_array)))

# Plot States 0 and 1
colors = ((0.35, 0.15, 1.0), (1.0, 0.15, 0.35))

plt.title('2 State HMM Predicted States and DamID Values')
plt.xlabel('Chromosome Position')
plt.ylabel('DamID Value')
for i, state in enumerate(state_data):
	plt.plot(state[:,0], state[:,1], '.', linewidth=1, color=colors[i], label='State ' + str(i))
plt.legend()
plt.show()