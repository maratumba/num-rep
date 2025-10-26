import json
import numpy as np

np.random.seed(42)

MATRIX_SIZE = 1000 
A = np.random.rand(MATRIX_SIZE, MATRIX_SIZE).astype(np.float64)
B = np.random.rand(MATRIX_SIZE, MATRIX_SIZE).astype(np.float64)
with open('A.json', 'w') as f:
    json.dump(A.tolist(), f)

with open('B.json', 'w') as f:
    json.dump(B.tolist(), f)