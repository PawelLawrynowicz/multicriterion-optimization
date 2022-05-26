from problem import Problem

n = 5
seed = 1410
maxIter = 1000

P = list(list())
i = 0
problem = Problem(n, seed)

P += [range(0, n)]  # rozwiązanie początkowe

it = 0
while(it < maxIter):

    it += 1
