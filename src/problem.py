
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

    def calculateMakespan(self, solution):
        makespan = 0
        timestable = self.p
        queue1 = solution
        queue2 = []
        queue3 = []
        while not(len(queue1)==0 and len(queue2)==0 and len(queue3)==0):
            if len(queue3)!=0:
                timestable[2][queue3[0]]-=1
                if timestable[2][queue3[0]]==0:
                    queue3.pop(0)
            if len(queue2)!=0:
                timestable[1][queue2[0]]-=1
                if timestable[1][queue2[0]]==0:
                    queue3.append(queue2.pop(0))
            if len(queue1)!=0:
                timestable[0][queue1[0]]-=1
                if timestable[0][queue1[0]]==0:
                    queue2.append(queue1.pop(0))
            makespan+=1
        return makespan
