import json
import random

lst = []

for i in range(50):
    lst.append(random.randint(1, 1000))

data = { 'data': lst}

with open('datalist.txt', 'w') as f:
    f.write(json.dumps(data))
f.close