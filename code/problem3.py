"""Problem 3: summarize score ranges under weight perturbations."""


def normalize_weights(weights):
    total = sum(weights)
    if total <= 0:
        raise ValueError("The weight sum must be positive")
    return [weight / total for weight in weights]


def score_ranges(normalized_data, base_weights, relative_change=0.1):
    scenarios = []
    for index in range(len(base_weights)):
        for direction in (-1.0, 1.0):
            changed = base_weights.copy()
            changed[index] *= 1.0 + direction * relative_change
            weights = normalize_weights(changed)
            scenarios.append([
                sum(value * weight for value, weight in zip(row, weights))
                for row in normalized_data
            ])
    return [(min(values), max(values)) for values in zip(*scenarios)]


if __name__ == "__main__":
    data = [[1.0, 0.2, 0.5], [0.5, 1.0, 0.0], [0.0, 0.4, 1.0]]
    ranges = score_ranges(data, [0.4, 0.35, 0.25])
    print([(round(low, 4), round(high, 4)) for low, high in ranges])
