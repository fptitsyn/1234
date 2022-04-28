def n_max_elements(lst, n):
    final_list = []

    for i in range(0, n):
        max1 = 0

        for j in range(len(lst)):
            if lst[j] > max1:
                max1 = lst[j]

        lst.remove(max1)
        final_list.append(max1)

    return final_list


if __name__ == "__main__":
    n = int(input())
    m = n
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        a.append(row)

    lst = []

    for i in a:
        for j in i:
            lst.append(j)

    n_largest = n_max_elements(lst, n)

    for i in range(len(a)):
        count = 0
        for j in a[i]:
            if j > 0:
                count += 1
        if count == 0:
            print(i + 1)
            break

    for i in range(n):
        a[i][i] = n_largest[i]
