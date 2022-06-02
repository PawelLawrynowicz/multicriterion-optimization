import numpy as  np
l=np.array([[781,   126,   126, -2966+4000],
            [826,   116,   116, -3877+4000],
            [827,    72,    72, -3544+4000],
            [903,   155,   155, -3195+4000]])
l[:,-1] = abs(l[:,-1])
max_vals = []
min_vals = []
for i in  range(4):
    max_vals.append(max(l[:,i]))
    min_vals.append(min(l[:,i]))
print(max_vals, min_vals)

print(l/1034)

for i in range(4):
    for j in  range(4):
        normalized_l = (l[i][j] - min_vals[j])/(max_vals[j]-min_vals[j])
        if j % 4 == 3:
            normalized_l = 1-normalized_l
        print(f'{normalized_l:.3f}', end=' ')
    print()