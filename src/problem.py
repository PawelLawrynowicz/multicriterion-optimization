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

    def calculateMakespan(self, solution: list):
        makespan = 0
        timestable = self.p.copy()
        queue1 = solution.copy()
        queue2 = []
        queue3 = []
        while not(len(queue1)==0 and len(queue2)==0 and len(queue3)==0):
            makespan+=1
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
        return makespan

    def calculateMaxTardiness(self, solution: list):
        time = 0
        maxTardiness = 0
        timestable = self.p.copy()
        queue1 = solution.copy()
        queue2 = []
        queue3 = []
        while not(len(queue1)==0 and len(queue2)==0 and len(queue3)==0):
            time+=1
            if len(queue3)!=0:
                timestable[2][queue3[0]]-=1
                if timestable[2][queue3[0]]==0:
                    tardiness = time - self.d[queue3[0]]
                    if tardiness > 0 and tardiness > maxTardiness:
                        maxTardiness = tardiness
                    queue3.pop(0)
            if len(queue2)!=0:
                timestable[1][queue2[0]]-=1
                if timestable[1][queue2[0]]==0:
                    queue3.append(queue2.pop(0))
            if len(queue1)!=0:
                timestable[0][queue1[0]]-=1
                if timestable[0][queue1[0]]==0:
                    queue2.append(queue1.pop(0))
        return maxTardiness

    def calculateMaxLateness(self, solution: list):
        time = 0
        maxLateness = 0
        timestable = self.p.copy()
        queue1 = solution.copy()
        queue2 = []
        queue3 = []
        while not(len(queue1)==0 and len(queue2)==0 and len(queue3)==0):
            time+=1
            if len(queue3)!=0:
                timestable[2][queue3[0]]-=1
                if timestable[2][queue3[0]]==0:
                    lateness = time - self.d[queue3[0]]
                    if lateness > maxLateness:
                        maxLateness = lateness
                    queue3.pop(0)
            if len(queue2)!=0:
                timestable[1][queue2[0]]-=1
                if timestable[1][queue2[0]]==0:
                    queue3.append(queue2.pop(0))
            if len(queue1)!=0:
                timestable[0][queue1[0]]-=1
                if timestable[0][queue1[0]]==0:
                    queue2.append(queue1.pop(0))
        return maxLateness

    def calculateTotalLateness(self, solution: list):
        time = 0
        totalLateness = 0
        timestable = self.p.copy()
        queue1 = solution.copy()
        queue2 = []
        queue3 = []
        while not(len(queue1)==0 and len(queue2)==0 and len(queue3)==0):
            time+=1
            if len(queue3)!=0:
                timestable[2][queue3[0]]-=1
                if timestable[2][queue3[0]]==0:
                    totalLateness += time - self.d[queue3[0]]
                    queue3.pop(0)
            if len(queue2)!=0:
                timestable[1][queue2[0]]-=1
                if timestable[1][queue2[0]]==0:
                    queue3.append(queue2.pop(0))
            if len(queue1)!=0:
                timestable[0][queue1[0]]-=1
                if timestable[0][queue1[0]]==0:
                    queue2.append(queue1.pop(0))
        return totalLateness

    def calculateCriteria(self, solution: list, num_of_criteria=2):
        criteria_methods = {
            0: self.calculateMakespan(solution),
            1: self.calculateMaxTardiness(solution),
            2: self.calculateMaxLateness(solution),
            3: self.calculateTotalLateness(solution),
        }
        criteria = np.zeros(num_of_criteria)
        for i in range(num_of_criteria):
            criteria[i] = criteria_methods[i]
        return criteria