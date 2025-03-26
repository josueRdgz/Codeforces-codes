def AdrenalileRush(start, final):
    '''2025A Codeforces Problem'''
    overtakes = []
    maximum = 0
    log = {}
    for i in range(len(start)):
        log.setdefault(start[i], [])
    there_was_a_change = True
    while there_was_a_change:
        there_was_a_change = False

        for car in range(len(start)-1):
            if start[car+1] == final[car+1] and (start[car] in log[start[car+1]] or start[car+1] in log[start[car]]):
                continue
            if (final.index(start[car]) < final.index(start[car+1])) and (start[car+1] in log[start[car]]):
                continue
            if start[car] not in log[start[car+1]]:
                maximum += 1
                there_was_a_change = True
                overtakes.append(
                    [start[car+1], start[car]])
                log[start[car+1]].append(start[car])
                start[car], start[car +
                                  1] = start[car+1], start[car]
    return maximum, overtakes


if __name__ == '__main__':
    m = int(input())
    st = input()
    final = []
    start = []
    for i in range(m):
        start.append(i+1)
        final.append(int(st.split()[i]))
    maximum, overtakes = AdrenalileRush(start, final)
    print(maximum)
    for i in range(len(overtakes)):
        print(overtakes[i][0], overtakes[i][1])
