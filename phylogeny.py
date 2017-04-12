import numpy as np

tree = ((((1, 1), 0), 1),(0, 0))

def getScore(t, present):
	score = 0
	for i in range(0,2):
		if isinstance(t[i], tuple):
			branch_scores = [getScore(t[i], 0), getScore(t[i], 1)]
			score += min(branch_scores)

			if np.min(branch_scores) != np.max(branch_scores) and np.argmin(branch_scores) != present:
				score += 1
		else:
			if present != t[i]:
				score += 1
	return score

min_insert_deletion = min(getScore(tree, 0), getScore(tree, 1))
print(min_insert_deletion)