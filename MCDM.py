import numpy as np
import matplotlib.pyplot as plt

def neutrosophic_set(membership, indeterminacy, nonmembership, x):
    """
    Neutrosophic set.
    
    Parameters:
    membership (float): Truth-membership value.
    indeterminacy (float): Indeterminacy-membership value.
    nonmembership (float): Falsity-membership value.
    x (numpy array): Input values for the function.
    
    Returns:
    numpy array: Neutrosophic set membership values.
    """
    result = np.exp(-0.5 * ((x - membership) / indeterminacy) ** 2)
    result = np.clip(result, 0, 1)  # Ensure values are in the range [0, 1]
    return result

def aggregate_neutrosophic_sets(sets):
    """
    Aggregate multiple neutrosophic sets using the max-min strategy.
    
    Parameters:
    sets (list of numpy arrays): List of neutrosophic sets.
    
    Returns:
    numpy array: Aggregated neutrosophic set.
    """
    aggregated_set = np.min(sets, axis=0)
    return aggregated_set

# Define criteria and their neutrosophic set parameters
criteria = ['Cost', 'Quality', 'Time']
params = {
    'Cost': {'membership': 3.0, 'indeterminacy': 2.0, 'nonmembership': 4.0},
    'Quality': {'membership': 7.0, 'indeterminacy': 1.5, 'nonmembership': 2.0},
    'Time': {'membership': 5.0, 'indeterminacy': 2.5, 'nonmembership': 3.0}
}

# Generate x values
x = np.linspace(0, 10, 1000)

# Calculate neutrosophic sets for each criterion
neutrosophic_sets = {}
for criterion in criteria:
    params_criterion = params[criterion]
    neutrosophic_sets[criterion] = neutrosophic_set(
        params_criterion['membership'],
        params_criterion['indeterminacy'],
        params_criterion['nonmembership'],
        x
    )

# Aggregate neutrosophic sets using the max-min strategy
aggregated_set = aggregate_neutrosophic_sets(list(neutrosophic_sets.values()))

# Plot the individual and aggregated neutrosophic sets
plt.figure(figsize=(10, 6))
for criterion in criteria:
    plt.plot(x, neutrosophic_sets[criterion], label=f'{criterion} Set')
plt.plot(x, aggregated_set, label='Aggregated Set', linestyle='--', linewidth=2)
plt.title('Multicriteria Decision Making with Neutrosophic Sets')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.legend()
plt.grid(True)
plt.show()
