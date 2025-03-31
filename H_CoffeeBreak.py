from collections import deque


def CoffeeBreak(n):
    maximum = [0] * len(n)

    for i in range(len(n)):
        duplicated = n.copy()
        inqueue = set()
        queue = deque()
        for j in range(len(n)):
            if duplicated[j] >= 2 and j != i:
                queue.append(j)
                inqueue.add(j)

        while queue:
            j = queue.popleft()
            inqueue.remove(j)
            half = duplicated[j]//2
            if j - 1 >= 0:
                duplicated[j-1] += half
                if duplicated[j - 1] >= 2 and j-1 != i and (j - 1) not in inqueue:
                    queue.append(j - 1)
                    inqueue.add(j - 1)
            if j + 1 < len(n):
                duplicated[j + 1] += half
                if duplicated[j + 1] >= 2 and j+1 != i and (j + 1) not in inqueue:
                    queue.append(j + 1)
                    inqueue.add(j + 1)

            duplicated[j] %= 2

        maximum[i] = duplicated[i]

    return maximum


if __name__ == '__main__':
    cases = int(input())
    cases_table = []
    for _ in range(cases):
        machinescount = int(input())
        st = input()
        n = list(map(int, st.split()))
        cases_table.append(n)

    for case in cases_table:
        result = CoffeeBreak(case)
        print(" ".join(map(str, result)))
