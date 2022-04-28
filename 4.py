if __name__ == "__main__":
    n = int(input())
    m = n
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        a.append(row)

s = []

max_col = len(a[0])
max_row = len(a)
cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
d1 = [[] for _ in range(max_row + max_col - 1)]
d2 = [[] for _ in range(len(d1))]
min_d2 = -max_row + 1

for i in a:
    count = 0
    for j in i:
        if j < 0:
            count = 0
            break
        count += j
    if count != 0:
        s.append(count)
print(s)

for i in range(max_col):
    for j in range(max_row):
        cols[i].append(a[j][i])
        rows[j].append(a[j][i])
        d1[i + j].append(a[j][i])
        d2[i - j - min_d2].append(a[j][i])

print(d1, '\n', d2)

for i in d1:
    if i == d1[0]:
        smallest_sum = sum(i)
    else:
        if sum(i) < smallest_sum:
            smallest_sum = sum(i)

for i in d2:
    if sum(i) < smallest_sum:
        smallest_sum = sum(i)

print(smallest_sum)
