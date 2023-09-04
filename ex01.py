def flatten(x):
    result = []
    for element in x:
        if hasattr(element, "__iter__") and not isinstance(element, str):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result


lists = [1, 2, [3, 4, [5], [6]], 7, 8, 9]


n2 = flatten(lists)

print(n2)