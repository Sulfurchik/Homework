N = int(input())

for a in range(1, N - 1):
    for b in range(1, N - a):
        v = N - a - b
        if v >= 1:
            print(f"А={a} Б={b} В={v}")