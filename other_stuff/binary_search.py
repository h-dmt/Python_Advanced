def bin_search(value, left_side, right_side, iteration=1):
    iteration += 1
    n = (left_side + right_side)//2
    if value == n:
        return f"found on interation {iteration}"
    elif value < n:
        return bin_search(value, left_side, n, iteration)
    elif value > n:
        return bin_search(value, n, right_side, iteration)
    else:
        return "Not found"


bin_search(13, 1, 48)
