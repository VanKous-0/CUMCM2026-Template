"""Problem 1: compute min-max normalized weighted scores."""


def normalize_columns(rows):
    columns = list(zip(*rows))
    normalized = []
    for row in rows:
        current = []
        for value, column in zip(row, columns):
            low, high = min(column), max(column)
            current.append(0.0 if high == low else (value - low) / (high - low))
        normalized.append(current)
    return normalized


def weighted_scores(rows, weights):
    if any(len(row) != len(weights) for row in rows):
        raise ValueError("Each row must have the same length as weights")
    return [sum(value * weight for value, weight in zip(row, weights)) for row in rows]


if __name__ == "__main__":
    data = [[8.0, 6.0, 7.0], [7.0, 9.0, 6.0], [6.0, 7.0, 9.0]]
    result = weighted_scores(normalize_columns(data), [0.4, 0.35, 0.25])
    print([round(value, 4) for value in result])
