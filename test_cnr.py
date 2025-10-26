import numpy as np
import json
import sys
from platform_info import get_platform_info


print(json.dumps(get_platform_info()))

with open('A.json','r') as f:
    a = json.load(f)

with open('B.json','r') as f:
    b = json.load(f)

A = np.asarray(a, dtype=np.float32)
B = np.asarray(b, dtype=np.float32)

result = np.dot(A,B)[0]

with open(sys.argv[1],'w') as f:
    f.write('\n'.join(map(str,result)))

with open(sys.argv[2],'w') as f:
    f.write(json.dumps(get_platform_info(), indent=4))

