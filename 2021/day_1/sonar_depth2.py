import json

with open('input.txt') as f:
    depths = json.load(f)

count = 0
for i in range(0, len(depths)-3):
    if sum(depths[(i+1):(i+4)]) > sum(depths[i:(i+3)]):
        count += 1

print(count)

