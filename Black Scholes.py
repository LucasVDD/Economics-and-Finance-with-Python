import math
import numpy as np
import random as rand
import scipy.stats as sp

# Declaring/Inputing Variables

while True:
    try:
        s = float(input("Enter the stock price at time t, S:"))
        k = float(input("Enter the Strike Price, k:"))
        r = float(input("Enter the Risk-Free Rate, r:"))
        sigma = float(input("Enter the volatility, sigma:"))
        T = float(input("Enter the total time horizon, T:"))
        t = float(input("Enter the time to expiry t:"))
        break
    except ValueError:
        print("Invalid input, please enter a float or string")

# Calculating delta 1 and delta 2
d1 = (math.log(s/k) + ((r + (sigma**2)/2) * (T-t)))/(sigma * np.sqrt(T-t))

d2 = (math.log(s/k) + ((r - (sigma**2)/2) * (T-t)))/(sigma * np.sqrt(T-t))

c = (sp.norm.cdf(d1) * s) - (sp.norm.cdf(d2) * k * math.e**(-r * (T-t)))
print("Call price = ", c)

p = -((sp.norm.cdf(-d1) * s) - (sp.norm.cdf(-d2) * k * math.e**(-r * (T-t))))
print("Put price =", p)