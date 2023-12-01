def choose_best_smartphone(criteria, weights, smartphones):
    # Normalize the criteria values if necessary
    normalized_smartphones = normalize(smartphones, criteria)

    # Calculate the weighted scores for each smartphone
    weighted_scores = np.dot(normalized_smartphones, weights)

    # Find the smartphone with the highest weighted score
    best_smartphone = smartphones[np.argmax(weighted_scores)]

    return best_smartphone

# Function to normalize criteria values
def normalize(smartphones, criteria):
    normalized_smartphones = []
    for smartphone in smartphones:
        normalized_smartphone = []
        for criterion, value in smartphone.items():
            if criterion in ['Price', 'Battery Life']:
                normalized_value = (max(criteria[criterion]) - value) / (max(criteria[criterion]) - min(criteria[criterion]))
            else:
                normalized_value = (value - min(criteria[criterion])) / (max(criteria[criterion]) - min(criteria[criterion]))
            normalized_smartphone.append(normalized_value)
        normalized_smartphones.append(normalized_smartphone)

    return np.array(normalized_smartphones)

# Define the criteria and random weights for smartphone features
criteria_smartphones = {'Price': [500, 1500], 'Camera Quality': [5, 12], 'Battery Life': [10, 40],
                        'Brand Reputation': [1, 10], 'Processor': [2, 8], 'Display': [5, 10]}

# Assign random weights to the criteria
# print(len(criteria_smartphones))
weights_smartphones = np.array([1.0, 0.7, 1.0, 0.4, 0.8, 0.9])
# weights_smartphones = np.random.rand(len(criteria_smartphones))
# print(np.random.rand(len(criteria_smartphones)))

# Normalize weights to ensure they sum to 1
weights_smartphones /= np.sum(weights_smartphones)

# Define the smartphone options
smartphones_options = [
    {'Price': 500, 'Camera Quality': 15, 'Battery Life': 35, 'Brand Reputation': 5, 'Processor': 6, 'Display': 8},
    {'Price': 600, 'Camera Quality': 8, 'Battery Life': 30, 'Brand Reputation': 8, 'Processor': 7, 'Display': 9},
    {'Price': 1200, 'Camera Quality': 11, 'Battery Life': 25, 'Brand Reputation': 4, 'Processor': 5, 'Display': 7},
    {'Price': 900, 'Camera Quality': 9, 'Battery Life': 32, 'Brand Reputation': 7, 'Processor': 6, 'Display': 9},
    {'Price': 1000, 'Camera Quality': 10, 'Battery Life': 28, 'Brand Reputation': 6, 'Processor': 8, 'Display': 10},
    {'Price': 700, 'Camera Quality': 7, 'Battery Life': 20, 'Brand Reputation': 9, 'Processor': 7, 'Display': 8},
    {'Price': 950, 'Camera Quality': 8, 'Battery Life': 32, 'Brand Reputation': 6, 'Processor': 9, 'Display': 9},
    {'Price': 1100, 'Camera Quality': 10, 'Battery Life': 38, 'Brand Reputation': 8, 'Processor': 7, 'Display': 8},
    {'Price': 750, 'Camera Quality': 6, 'Battery Life': 22, 'Brand Reputation': 7, 'Processor': 8, 'Display': 9},
    {'Price': 850, 'Camera Quality': 9, 'Battery Life': 27, 'Brand Reputation': 5, 'Processor': 7, 'Display': 10},
]



best_smartphone_option = choose_best_smartphone(criteria_smartphones, weights_smartphones, smartphones_options)

print(best_smartphone_option)
