
rows = int(input())
M = [[int(m) for m in input().split(' ')] for _ in range(rows)]
diag_M = [row[i] for i, row in enumerate(M)]

print(sum(diag_M))
