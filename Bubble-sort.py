def countSwaps(a):
    m = 0
    n = len(a)

    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                m += 1

    print("Array is sorted in", swaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
n = int(input())
a = list(map(int, input().split()))
countSwaps(a)
