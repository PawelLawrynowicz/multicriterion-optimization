from dataclasses import dataclass
import random

@dataclass
class Data:
    seed = 1410
    maxIter = 400
    n = 100
    random.seed(seed)