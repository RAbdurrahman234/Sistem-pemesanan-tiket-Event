def bubble_sort(data, key, terbalik=False):
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            a = arr[j][key]
            b = arr[j+1][key]
            try:
                a, b = float(a), float(b)
            except:
                a, b = str(a), str(b)
            if (a > b) != terbalik:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def binary_search(data_terurut, key, target):
    lo, hi = 0, len(data_terurut) - 1
    target = target.lower()
    while lo <= hi:
        mid = (lo + hi) // 2
        val = str(data_terurut[mid][key]).lower()
        if val == target:
            return mid
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
