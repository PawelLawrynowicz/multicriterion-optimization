from problem import Problem

n = 2
seed = 1410
maxIter = 1000

P = list(list())
i = 0
problem = Problem(n, seed)

P += range(0, n)  # rozwiązanie początkowe

print(problem.p)
print(problem.calculateMakespan(P))
