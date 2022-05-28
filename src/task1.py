from problem import Problem
import random
from RandomNumberGenerator import RandomNumberGenerator

seed = 1410
random.seed(seed)
rng = RandomNumberGenerator(seed)

maxIter = 100
n = 10

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def defineRandomSwapNeighbour(x):
    idx1 = rng.nextInt(0, len(x)-1)
    idx2 = rng.nextInt(0, len(x)-1)
    while (idx1 == idx2):
        idx2 = rng.nextInt(0, len(x)-1)
    order = x
    swap(order, idx1, idx2)
    return order

def isDominating(left, right):
    options = {"better": 1, "same": 0, "worse": -1}
    evaluation = list()
    for i in range(len(left)):
        if left[i] > right[i]:
            evaluation.append(options["worse"])
        elif left[i] == right[i]:
            evaluation.append(options["same"])
        elif left[i] < right[i]:
            evaluation.append(options["better"])
    # some are worse
    if any([i == options["worse"] for i in evaluation]):
        return False
    # none are worse, some are better
    elif any([i == options["better"] for i in evaluation]):
        return True
    else:  # none are worse, none are better; all are the same
        return False

def acceptRandomly(p=0.1):
    random_sample = random.randint(0, 100) / 100
    if p < random_sample:
        return False
    else:
        return True

def task1():

    P = list(list())
    it = 0

    problem = Problem(n, seed)
    
    x = list(range(n))
    random.shuffle(x)                                       # losowe rozwiązanie początkowe
    P += [(x.copy(), problem.calculateCriteria(x))]         # dodaj x do P

    while(it < maxIter): 
        x_prime = defineRandomSwapNeighbour(x)              # wyznacz x' jako losowego sąsiada x
        if isDominating(                                    # jeśli x' dominuje nad x
            problem.calculateCriteria(x_prime), 
            problem.calculateCriteria(x)
            ):  
            x = x_prime                                     # wykonaj x <- x'
            P+=[(x.copy(), problem.calculateCriteria(x))]   # dodaj x' do P
        elif acceptRandomly(p=0.1):                         # w przeciwnym razie wykonaj powyższy etap z prawadopodobieństwem p(it) = 0.1
            x = x_prime                                     # wykonaj x <- x'
            P+=[(x.copy(), problem.calculateCriteria(x))]   # dodaj x' do P
        it += 1                                             # it <- it + 1
    print(P)
task1()