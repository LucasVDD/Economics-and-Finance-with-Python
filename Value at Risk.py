import numpy as np
import scipy.stats as ss

# To do:
    # New goal: Insert ticker and scrape data from yahoo finance, then calculate mean, volatility and plot histogram.
    # Then we will estimate nonparametrically and parametrically

    # Nonparametric estimation will be done by finding the discrete data value below our desired threshhold. It can take any distribution

    # Parametric estimation will be done through the equation "VaR(a) = -Investment * (average + Z(a) * volatility)" while assuming normality.


    # For now, mean and volatility will be inputted manually.

# Program Comments:

# Variable Inputs

# Basel II standards dictate that Time(N) = 1 and Confidence_Level(X) = 99.9% (0.999)  
# Basel IV standards use Expected shortfall with a 97.5% Confidence_Level
 
# Rename confidence_level variable to mathematical notation (equivalent to gamma for Expected Shortfall)

while True:
    try:
        confidence_level = float(input("Input a VaR confidence level between 0.90 and 0.999...: "))
        if not (0.90 <= confidence_level < 1):
            print("Confidence level must between 0.90 and 0.99...")
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

while True:
    try:
        gamma = float(input("Input a Expected Shortfall confidence level between 0.90 and 0.99: "))
        if not (0.90 <= gamma < 1):
            print("Confidence level must between 0.90 and 0.9999...")
            continue
        break
    except ValueError:
        print("Invalid input(s), please enter only floats and/or integers.")


# To calculate expected shortfall using historical simulation we average the observations in the tail of the distribution of losses.


# Weighted average Expected Shortfall:

# Lets say you wanted to weight recent observations more than old ones.

# Then youd need to index (for loop) to assign weight to to ith scenario.

weighted_average_expected_shortfall = gamma**(n-i)(1 - gamma)/1-gamma**n

# where n is the number of scenarios(observations)