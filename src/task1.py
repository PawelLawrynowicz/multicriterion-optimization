from problem import Problem
import random
from RandomNumberGenerator import RandomNumberGenerator
from utils import defineRandomSwapNeighbour, isDominating, acceptRandomly

from data import Data

random.seed(Data.seed)

def task1(n, maxIter, numCriteria = 2, output=False):

    P = list(list())
    it = 0

    problem = Problem(n, Data.seed)
    
    x = list(range(n))
    random.shuffle(x)                                           # losowe rozwiązanie początkowe
    P += [(x.copy(), problem.calculateCriteria(x, num_of_criteria=numCriteria))]             # dodaj x do P

    while(it < maxIter): 
        x_prime = defineRandomSwapNeighbour(x)                  # wyznacz x' jako losowego sąsiada x
        if isDominating(                                        # jeśli x' dominuje nad x
            problem.calculateCriteria(x_prime, num_of_criteria=numCriteria), 
            problem.calculateCriteria(x, num_of_criteria=numCriteria)
            ):  
            x = x_prime                                         # wykonaj x <- x'
            P += [(x.copy(), problem.calculateCriteria(x))]     # dodaj x' do P
        elif acceptRandomly(p=0.1):                             # w przeciwnym razie wykonaj powyższy etap z prawadopodobieństwem p(it) = 0.1
            x = x_prime                                         # wykonaj x <- x'
            P += [(x.copy(), problem.calculateCriteria(x))]     # dodaj x' do P
        it += 1                                                 # it <- it + 1
    if output:
        print(P)

task1(Data.n, Data.maxIter, numCriteria=4, output=True)