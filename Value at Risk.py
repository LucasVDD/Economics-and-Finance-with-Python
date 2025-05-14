import math
import numpy as np
import random as rand
import scipy.stats as ss

# For now, value and volatility will correspond the expected location and scale parameters of our distribution.

# I'd like to have the option to either: Manually input the mean and volatility OR Estimate it from a data set

# I.e A choice in the terminal between "Manual" or "Import" as inputs to the Var and ES/CVAR calculations.
    # If manual input, allow distribution type to be picked
    # If imported, estimate distribution and run comparison tests for normality.

value = float(input("Input the Total Value: "))
volatility = float(input("Input the Volatility ()"))
confidence_level = float(input("Input a confidence level between 0 and 0.99:"))
time = float(input("Enter the time horizon: "))



