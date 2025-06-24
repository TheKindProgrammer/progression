def canMakeArithmeticProgression(arr):
    if len(arr) == 2:
        return True

    arr.sort()
    lowest = min(arr)
    highest = max(arr)

    step = (highest - lowest) / len(arr)

    for i in range(1, len(arr)):
        prev = arr[i - 1]
        curr = arr[i]
        if prev + step != curr:
            return False

    return True

arr = [-68,-96,-12,-40,16]
canMakeArithmeticProgression(arr)