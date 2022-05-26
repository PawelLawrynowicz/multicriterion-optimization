
from RandomNumberGenerator import RandomNumberGenerator
import math
import numpy as np


class Problem:
    def __init__(self, n, seed):
        rng = RandomNumberGenerator(seed)
        A = 0
        self.p = np.zeros((3, n))
        self.d = np.zeros(n)
        for i in range(3):
            for j in range(n):
                self.p[i][j] = rng.nextInt(1, 99)
                A = A+self.p[i][j]
        B = math.floor(A/2)
        A = math.floor(A/6)
        for j in range(n):
            self.d[j] = rng.nextInt(A, B)
