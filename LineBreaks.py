
def LineBreaks(cases,m,words):
    solver=[]
    for case in range(cases):
        count = 0
        possiblewords = 0
        for i in range(len(words[case])):
            for j in range(len(words[case][i])):
                count+=1
            if count > m[case]:
                break    
            possiblewords+=1
        solver.append(possiblewords)
    return solver
            

if __name__ == '__main__':
    cases = int(input())
    n = []
    m = []
    words = []
    for i in range(cases):
        ni,mi = map(int,input().split())
        n.append(ni)
        m.append(mi)
        casewords = []
        for j in range(ni):
            casewords.append(input())
        words.append(casewords)
    sol= LineBreaks(cases,m,words)
    for i in range(len(sol)):
        print(sol[i])
