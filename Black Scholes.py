import math
import numpy as np
import random as rand
import scipy.stats as ss

# Declaring/Inputing Variables

while True:
    try:
        stock_price = float(input("Enter the stock price at time t, S:"))
        strike_price = float(input("Enter the Strike Price, K:"))
        risk_free_rate = float(input("Enter the Risk-Free Rate, r:"))
        sigma = float(input("Enter the volatility, sigma:"))
        total_time = float(input("Enter the total time horizon, T:"))
        time_passed = float(input("Enter the time passed:"))
        break
    except ValueError:
        print("Invalid input(s), please enter only floats and/or integers")

# Calculating delta 1 and delta 2

d1 = (math.log(stock_price /strike_price) + ((risk_free_rate + (sigma**2)/2) * (total_time-time_passed)))/(sigma * np.sqrt(total_time-time_passed))

d2 = (math.log(stock_price/strike_price) + ((risk_free_rate - (sigma**2)/2) * (total_time-time_passed)))/(sigma * np.sqrt(total_time-time_passed))

call_price = (ss.norm.cdf(d1) * stock_price) - (ss.norm.cdf(d2) * strike_price * math.e**(-risk_free_rate * (total_time-time_passed)))
print("Call price = ", call_price)

put_price = -((ss.norm.cdf(-d1) * stock_price) - (ss.norm.cdf(-d2) * strike_price * math.e**(-risk_free_rate * (total_time-time_passed))))
print("Put price =", put_price)