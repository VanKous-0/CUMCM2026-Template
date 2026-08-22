"""Problem 2: solve a small integer resource-allocation example."""


def best_allocation(scores, capacities, budget):
    if len(scores) != len(capacities):
        raise ValueError("scores and capacities must have equal length")
    best_value, best_plan = float("-inf"), None

    def search(index, remaining, plan):
        nonlocal best_value, best_plan
        if index == len(scores):
            value = sum(score * amount for score, amount in zip(scores, plan))
            if value > best_value:
                best_value, best_plan = value, plan.copy()
            return
        for amount in range(min(capacities[index], remaining) + 1):
            search(index + 1, remaining - amount, plan + [amount])

    search(0, budget, [])
    return best_plan, best_value


if __name__ == "__main__":
    allocation, value = best_allocation([0.842, 0.766, 0.693], [3, 4, 5], 7)
    print({"allocation": allocation, "objective": round(value, 4)})
