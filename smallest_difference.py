def smallestDifference(arrayOne, arrayTwo):
    min = float('inf')
    pair = None
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            if diff(arrayOne[i], arrayTwo[j]) < min:
                min = diff(arrayOne[i], arrayTwo[j])
                pair = [arrayOne[i], arrayTwo[j]]

    return pair

def diff(x, y):
    return abs(x - y)
