def fractional_knapsack(values, weights, capacity):
    items = list(zip(values, weights))
    items.sort(key=lambda x: x[0]/x[1], reverse=True)

    total = 0
    for v, w in items:
        if capacity >= w:
            total += v
            capacity -= w
        else:
            total += v * (capacity/w)
            break
    return total

def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    result = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= result[-1][1]:
            result.append(activities[i])

    return result