if __name__ == "__main__":
    n = int(input())
    m = int(input())
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        a.append(row)

    count = 0
    s = []

    for i in a:
        if 0 not in i:
            count += 1

    for i in a:
        s_count = 0
        for j in i:
            if j not in s:
                s_count += 1
            if s_count > 1:
                s.append(j)
                s_count = 0

    print(count, max(s))
