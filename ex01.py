def flatten_list(lists):
    result = []
    for element in lists:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result
