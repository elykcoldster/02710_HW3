import numpy as np

tree = ((((1, 1), 0), 1),(0, 0))

def getScore(t, present):
	score = 0
	for i in range(0,2): # i = 0 for left branch, 1 for right branch
		if isinstance(t[i], tuple):
			# get branch scores for different presence states
			branch_scores = [getScore(t[i], 0), getScore(t[i], 1)]
			score += min(branch_scores)

			# this step checks if a branch's optimal assignment requires it to insert/delete region x
			# if the branches can be assigned either 0 or 1, assume it prefers to be the same
			# assignment as this node
			if np.min(branch_scores) != np.max(branch_scores) and np.argmin(branch_scores) != present:
				score += 1
		else:
			if present != t[i]:
				score += 1
	return score

min_insert_deletion = min(getScore(tree, 0), getScore(tree, 1))
print(min_insert_deletion)