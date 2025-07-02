# Personal solution I wrote up as practice:

import numpy as np

# Length of Inscribed Square, you can use this to approximate the area of any circle where r = l
l = 1
inside = []
# Number of sample points: as N approaches infinity. P approaches Pi
N = 1000000
for n in range(N):
    x, y = np.random.uniform(0,l), np.random.uniform(0,1)
    R = np.sqrt(x**2 + y**2)
    if R < l:
        inside.append(R)
        s = len(inside)
    else:
        pass
π = (4 * s)/n
print(π)
list.clear(inside)

accuracy = π/np.pi
print(str(accuracy) + "%")


# Following Solution from QuantEcon.org/Lectures/IntroToPython/:

n = 1000000 # sample size for Monte Carlo simulation

count = 0
for i in range(n):

    # drawing random positions on the square
    u, v = np.random.uniform(), np.random.uniform()

    # check whether the point falls within the boundary
    # of the unit circle centred at (0.5,0.5)
    d = np.sqrt((u - 0.5)**2 + (v - 0.5)**2)

    # if it falls within the inscribed circle, 
    # add it to the count
    if d < 0.5:
        count += 1

area_estimate = count / n

print(area_estimate * 4)  # dividing by radius**2

accuracy = (area_estimate * 4)/np.pi
print(str(accuracy) + "%")