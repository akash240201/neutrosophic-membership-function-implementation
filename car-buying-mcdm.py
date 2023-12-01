import numpy as np

def saw(criteria, weights, alternatives):
    # Normalize the criteria values if necessary
    normalized_alternatives = normalize(alternatives, criteria)

    # Calculate the weighted scores for each alternative
    weighted_scores = np.dot(normalized_alternatives, weights)

    # Find the alternative with the highest weighted score
    best_alternative = alternatives[np.argmax(weighted_scores)]

    return best_alternative

# Function to normalize criteria values
def normalize(alternatives, criteria):
    normalized_alternatives = []
    for alternative in alternatives:
        normalized_alternative = []
        for criterion, value in alternative.items():
            if criterion in ['price', 'cost']:
                normalized_value = (max(criteria[criterion]) - value) / (max(criteria[criterion]) - min(criteria[criterion]))
            else:
                normalized_value = (value - min(criteria[criterion])) / (max(criteria[criterion]) - min(criteria[criterion]))
            normalized_alternative.append(normalized_value)
        normalized_alternatives.append(normalized_alternative)

    return np.array(normalized_alternatives)

# Define the criteria
criteria = {'price': [20000, 30000], 'fuel efficiency': [30, 50], 'safety rating': [3, 5]}

# Assign weights to the criteria
weights = np.array([0.3, 0.4, 0.3])

# Define the alternatives
alternatives = [
    {'price': 10000, 'fuel efficiency': 50, 'safety rating': 4},
    {'price': 1000, 'fuel efficiency': 30, 'safety rating': 3},
    {'price': 30000, 'fuel efficiency': 50, 'safety rating': 5},
]

best_alternative = saw(criteria, weights, alternatives)

print(best_alternative)
