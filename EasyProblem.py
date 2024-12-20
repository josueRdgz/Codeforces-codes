
def EasyProblem(t,n):
    for i in range(t):
        print(n[i]-1)

if __name__ == '__main__':
    t = int(input())
    n = []
    for i in range(t):
        n.append(int(input()))
    EasyProblem(t,n)
