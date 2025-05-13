import math
import numpy as np
import random as rand
import scipy.stats as sp

# Declaring/Inputing Variables


    ## **NEEDS TO BE REWORKED TO PREVENT STRINGS FROM PASSING**

while True:

    s = float(input("Enter the stock price at time t, S:"))
    T = float(input("Enter the total time horizon, T:"))
    t = float(input("Enter the time to expiry t:"))
    k = float(input("Enter the Strike Price, k:"))
    r = float(input("Enter the Risk-Free Rate, r:"))
    sigma = float(input("Enter the volatility, sigma:"))
    
    if not all(isinstance(i, (int , float)) for i in (s , t , k , r , sigma)):
        print("You entered a value incorrectly, try again (must be int or float)")
        print(type(s),type(t),type(k),type(r),type(sigma))
        continue
    else:
        #All variables must be integers or floats.
        break


# Calculating delta 1 and delta 2

d1 = (math.log(s/k) + ((r + (sigma**2)/2) * (T-t)))/(sigma * np.sqrt(T-t))
print("d1 = ", d1)

d2 = (math.log(s/k) + ((r - (sigma**2)/2) * (T-t)))/(sigma * np.sqrt(T-t))
print("d2 = ", d2)

C = (sp.norm.cdf(d1) * s) - (sp.norm.cdf(d2) * k * math.e**(-r * (T-t)))
print("Call price = ", C)