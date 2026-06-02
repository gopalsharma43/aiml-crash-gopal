import numpy as np

scores = np.array([78, 85, 92, 67, 88, 95, 73, 81])

print("Scores:")
print(scores)

print("\nAverage Score:", np.mean(scores))
print("Highest Score:", np.max(scores))
print("Lowest Score:", np.min(scores))

above_80 = scores[scores > 80]

print("\nScores Above 80:")
print(above_80)