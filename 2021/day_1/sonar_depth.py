import json

with open("input.txt", "r") as f:
    depths = json.load(f)


count = 0
for i in range(1, len(depths)):
    if depths[i-1] < depths[i]:
        count += 1
    


