import numpy as np
import sys

def read_nums_file(path):
  with open(path, 'r') as f:
    return np.asarray([float(line.strip()) for line in f.readlines()], dtype=np.float32)

def calc_score(A, B):
  # total absolute difference normalized by number of elements
  mean = np.mean(np.abs(A - B))
  std = np.std(np.abs(A - B))
  return mean, std

size = len(sys.argv)-1

results_mean = np.zeros((size, size), dtype=np.float32)
results_std = np.zeros((size, size), dtype=np.float32)

for i in range(size):
  for j in range(size):
    A = read_nums_file(sys.argv[i+1])
    B = read_nums_file(sys.argv[j+1])
    results_mean[i][j], results_std[i][j] = calc_score(A, B)

print("Mean Results:")
print(str(results_mean))
print("Standard Deviation Results:")
print(str(results_std))
