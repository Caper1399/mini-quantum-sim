import numpy as np
from gates import X, Y, Z, H

state0 = np.array([1, 0], dtype=complex)  # |0> state
state1 = np.array([0, 1], dtype=complex)  # |1> state

class Qubit:
    def __init__(self, state):
        if(state == 0):
            self.state = state0
        else:
            self.state = state1
        
    def measure(self):
        prob = np.abs(self.state)**2
        # print("% of 0:", prob[0])
        # print("% of 1:", prob[1])
        return np.random.choice([0,1], p=prob)
    
    def appyGate(self, gate):
        self.state = gate @ self.state

counts = {0: 0, 1: 0}
for _ in range(1000):
    q = Qubit(0)
    q.appyGate(H)
    result = q.measure()
    counts[result] += 1

print("H gate: ", counts)

counts = {0: 0, 1: 0}
for _ in range(1000):
    q = Qubit(0)
    q.appyGate(X)
    result = q.measure()
    counts[result] += 1

print("X gate on 0: ", counts)

counts = {0: 0, 1: 0}
for _ in range(1000):
    q = Qubit(1)
    q.appyGate(X)
    result = q.measure()
    counts[result] += 1

print("X gate on 1: ", counts)