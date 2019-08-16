def make_function(parity):
    """Return a function that filters out `odd` and `even`
       numbers depending on the provided `parity`
    """
    if parity == 'even':
        matches_parity = lambda x: x % 2 == 0
    elif parity == 'odd':
        matches_parity = lambda x: x % 2 != 0
    else:
        raise AttributeError("Unknown Parity: " + parity)

    def get_by_parity(numbers):
        filtered = [num for num in numbers if matches_parity(num)]
        return filtered
    return get_by_parity
