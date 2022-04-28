if __name__ == "__main__":
    n = int(input())
    m = n
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        a.append(row)

    print(a)

    b = []

    for _ in range(m):
        b.append([0] * n)
    for i in range(n):
        for j in range(m):
            b[j][i] = a[n-1-i][j]
    for row in b:
        print(" ".join([str(x) for x in row]))
