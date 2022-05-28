from dataclasses import dataclass
import random

@dataclass
class Data:
    seed = 1410
    maxIter = 100
    n = 10
    random.seed(seed)