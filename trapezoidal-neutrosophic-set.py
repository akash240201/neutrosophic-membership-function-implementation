import matplotlib.pyplot as plt
import numpy as np

def neutrosophic_trapizoidal_membership_function(x, a, b, c, d):
    """
    Calculates the neutrosophic trapezoidal membership function.
    
    Args:
    x: The input value.
    a: The lower bound of the support interval.
    b: The lower bound of the core interval.
    c: The upper bound of the core interval.
    d: The upper bound of the support interval.
    
    Returns:
    A tuple of three values: the truth membership degree, the indeterminacy
    membership degree, and the falsity membership degree.
    """
    if x < a:
        return (0, 1, 1)  # Falsity is 1, Indeterminacy is 1, Truth is 0
    elif x < b:
        truth_degree = (x - a) / (b - a)
        indeterminacy_degree = 1 - truth_degree
        falsity_degree = 1
        return (truth_degree, indeterminacy_degree, falsity_degree)
    elif x <= c:
        return (1, 0, 0)  # Truth is 1, Indeterminacy is 0, Falsity is 0
    elif x < d:
        truth_degree = 1 - (x - c) / (d - c)
        indeterminacy_degree = (x - c) / (d - c)
        falsity_degree = 1 - indeterminacy_degree
        return (truth_degree, indeterminacy_degree, falsity_degree)
    else:
        return (0, 0, 1)  # Truth is 0, Indeterminacy is 0, Falsity is 1

# Define the parameters of the membership function
a = 0
b = 2
c = 5
d = 7

# Generate the input values
x = np.linspace(a, d, 100)

# Calculate the membership degrees
truth_degrees = []
indeterminacy_degrees = []
falsity_degrees = []

for value in x:
    # Call the neutrosophic_trapezoidal_membership_function for each x
    truth_degree, indeterminacy_degree, falsity_degree = neutrosophic_trapizoidal_membership_function(value, a, b, c, d)
    
    # Append the calculated degrees to the corresponding lists
    truth_degrees.append(truth_degree)
    indeterminacy_degrees.append(indeterminacy_degree)
    falsity_degrees.append(falsity_degree)

# Plot the membership functions
plt.plot(x, truth_degrees, label='Truth')
plt.plot(x, indeterminacy_degrees, label='Indeterminacy')
plt.plot(x, falsity_degrees, label='Falsity')
plt.xlabel('x')
plt.ylabel('Membership degree')
plt.title('Neutrosophic trapezoidal membership function')
plt.legend()
plt.show()
