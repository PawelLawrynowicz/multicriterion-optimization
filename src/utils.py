from data import Data
import random
from RandomNumberGenerator import RandomNumberGenerator

random.seed(Data.seed)
rng = RandomNumberGenerator(Data.seed)

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