import numpy as np
import matplotlib.pyplot as plt

def neutrosophic_set(membership, indeterminacy, nonmembership, universe):
    """
    Neutrosophic set.
    Parameters:
    membership (float): Truth-membership value.
    indeterminacy (float): Indeterminacy-membership value.
    nonmembership (float): Falsity-membership value.
    universe (numpy array): Universe of discourse.
    Returns:
    numpy array: Neutrosophic set membership values.
    """
#     print(membership)
#     print(indeterminacy)
#     print(nonmembership)
#     print(universe)
    # Calculate the exponent term of the neutrosophic set formula
    exponent_term = -0.5 * ((universe - membership) / indeterminacy) ** 2
#     print(exponent_term)
    # Calculate the neutrosophic set membership values
    result = np.exp(exponent_term)
#     print(result)
    # Clip values to ensure they are in the range [0, 1]
    result = np.clip(result, 0, 1)
    
    return result

# Define neutrosophic set parameters
membership_value = 5.0
indeterminacy_value = 1.0
nonmembership_value = 4.5

# Generate universe of discourse (x values)
universe = np.linspace(0, 10, 10000)

# Calculate neutrosophic set membership values
neutrosophic_membership = neutrosophic_set(
    membership_value, indeterminacy_value, nonmembership_value, universe
)

# Plot the neutrosophic set
plt.plot(universe, neutrosophic_membership, label=f'Neutrosophic Set: ({membership_value}, {indeterminacy_value}, {nonmembership_value})')
plt.title('Neutrosophic Set')
plt.xlabel('Universe of Discourse')
plt.ylabel('Membership Value')
plt.legend()
plt.grid(True)
plt.show()
