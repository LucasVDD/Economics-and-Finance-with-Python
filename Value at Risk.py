import numpy as np
import scipy.stats as ss

# To do:
    # New goal: Insert ticker and scrape data from yahoo finance, then calculate mean, volatility and plot histogram.
    # Then we will estimate nonparametrically and parametrically

    # Nonparametric estimation will be done by finding the discrete data value below our desired threshhold. It can take any distribution

    # Parametric estimation will be done through the equation "VaR(a) = -Investment * (average + Z(a) * volatility)

    # For now, mean and volatility will be inputted manually.

# Program Comments:

# Variable Inputs

while True:
    try:
        confidence_level = float(input("Input a confidence level between 0.90 and 0.999...: "))
        if not (0.90 <= confidence_level < 1):
            print("Confidence level must be greater than 0 and less than 1")
            continue
        value = float(input("Input the total value: "))
        average_return = float(input("Input the average return: "))
        volatility = float(input("Input the volatility as a decimal: "))
        time = float(input("Enter the time horizon: "))
        break
    except ValueError:
        print("Invalid input(s), please enter only floats and/or integers")

# Calculations

alpha = 1 - confidence_level

value_at_risk = (-value * (average_return + (ss.norm.ppf(alpha)*(volatility)))) * np.sqrt(time)
print("The ",time," day Value at Risk is: ", value_at_risk)
