def for_wizards(n):  # wrong answer user's subarray shift is not optimal (test case 107)

    if n == sorted(n):
        return (1, 1)

    inversion = [0] * len(n)
    maximum = [float('-inf')]*len(n)
    end = list(range(len(n)))
    for i in range(len(n)-1):
        for j in range(i, len(n)):
            if n[j] < n[i]:
                inversion[i] += 1
            if n[j] > n[i]:
                inversion[i] -= 1
            if inversion[i] > maximum[i]:
                maximum[i] = inversion[i]
                end[i] = j
    i = inversion.index(max(inversion[:-1]))
    j = end[i]

    return (i+1, j+1)


if __name__ == '__main__':
    cases = int(input())
    cases_table = []
    for i in range(cases):
        wizardscount = int(input())
        st = input()

        m = [st.split(" ", wizardscount)]
        n = [int(x) for x in m[0]]
        cases_table.append(n)
    for i in range(cases):
        n = for_wizards(cases_table[i])
        print(n[0], n[1])
