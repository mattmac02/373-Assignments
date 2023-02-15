import matplotlib.pyplot as plt
import numpy as np

arrivalRate = np.array([0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745])
serviceRate = 0.75
timeSlots = 1000000
expecQueue = []

for a in arrivalRate:
    p = (a * (1 - serviceRate)) / (serviceRate * (1 - a))
    L = sum(b*(p**b)*(1-p) for b in range(timeSlots))
    W = L/a
    print(f"Expected Cumulative Queue Delay {W}")
    expecQueue.append(W)

plt.plot(arrivalRate, expecQueue)
plt.xlabel("Arrival Rate")
plt.ylabel("Expected Queue Delay")
plt.show()

