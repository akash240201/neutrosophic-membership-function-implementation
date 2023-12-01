import numpy as np
import matplotlib.pyplot as plt

def neutrosophic_interval_valued_set(left, middle, right, x):
    """
    Neutrosophic interval-valued set.
    
    Parameters:
    left (float): Left boundary of the interval.
    middle (float): Middle value of the interval.
    right (float): Right boundary of the interval.
    x (numpy array): Input values for the function.
    
    Returns:
    numpy array: Neutrosophic interval-valued set membership values.
    """
    result = np.zeros_like(x, dtype=float)
    
    # Define masks for different regions of x
    mask_left = x <= left
    mask_middle = np.logical_and(x > left, x <= right)
    mask_right = x > right
    
    # Assign membership values based on the masks
    result[mask_left] = 1.0
    result[mask_middle] = (right - x[mask_middle]) / (right - left)
    result[mask_right] = 0.0
    
    return result

# Define interval values
left = 2
middle = 5
right = 8

# Generate x values
x = np.linspace(0, 10, 1000)

# Calculate y values using the neutrosophic interval-valued set function
y = neutrosophic_interval_valued_set(left, middle, right, x)

# Plot the neutrosophic interval-valued set
plt.plot(x, y, label=f'Neutrosophic Interval: [{left}, {middle}, {right}]')
plt.title('Neutrosophic Interval-Valued Set')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.legend()
plt.grid(True)
plt.show()

# In this example, we define three criteria (Cost, Quality, Time) and their associated
# neutrosophic set parameters. The neutrosophic_set function calculates the
# membership values for each criterion, and the aggregate_neutrosophic_sets function
# aggregates these sets using the max-min strategy.
# We can adjust the criteria and their parameters to fit your specific decision-making
# scenario. The resulting plot shows individual neutrosophic sets for each criterion and
# the aggregated neutrosophic set.
