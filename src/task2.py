import random
from problem import Problem
from data import Data
from utils import defineRandomSwapNeighbour, acceptRandomly

random.seed(Data.seed)

def s(x_criteria):
    c = [1,5,5]
    sum = 0
    for i in range(len(x_criteria)):
        sum += x_criteria[i]*c[i]
    return sum

def task2(n, maxIter, output = False):
    it_to_check = [i for i in range(maxIter//8,maxIter+1,maxIter//8)]
    scores = {}
    it = 0                        
    problem = Problem(n, Data.seed)

    x = list(range(n))                 
    random.shuffle(x)                                       

    x_criteria = problem.calculateCriteria(x, num_of_criteria=3)

    x_best = s(x_criteria)    
    scores[0] =  x_best
    while (it < maxIter):
        x_criteria = problem.calculateCriteria(x, num_of_criteria=3)                               
        x_prime = defineRandomSwapNeighbour(x)  
        x_prime_criteria = problem.calculateCriteria(x_prime, num_of_criteria=3)  
        if s(x_prime_criteria) < s(x_criteria):                           
            x = x_prime                                         
            x_best = s(x_prime_criteria) if s(x_prime_criteria) < x_best else x_best
        elif acceptRandomly(p=0.1):                     
            x = x_prime       

        if it+1 in it_to_check:
            scores[it+1] = x_best

        it += 1      
    
    if output:
        print(f"x:\t{x}\ns(x):\t{s(x)}")

    return scores
    