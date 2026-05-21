N = int(input())
M = int(input())
width = len(str(N * M))

for i in range(N):
    if i % 2 == 0:
        start = i * M + 1
        end = start + M
        for j in range(start, end):
            print(f"{j:{width}}", end=" ")
    else:
        start = (i + 1) * M
        end = i * M
        for j in range(start, end, -1):
            print(f"{j:{width}}", end=" ")
    print()
