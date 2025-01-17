def CoffeeBreak(n):
    maximum = []
    
    for i in range(len(n)):
        duplicated = n.copy()
        
        first_move=False
        j=0
        while j <len(n):
            if j==i:
                j+=1
                continue
            if duplicated[j]<2:
                j+=1
                continue
            if j-1>=0:
                duplicated[j-1]+=int(duplicated[j]/2)
            if j+1<len(n):
                duplicated[j+1]+=int(duplicated[j]/2)
            if not duplicated[j]%2:
                duplicated[j]=0
            else:
                duplicated[j]=1
            
            first_move=True
            j+=1
            for k in range(0,len(n)):
                if duplicated[k]>=2 and k!=i:
                    j=k
                    break
            if not first_move:
                break
                
        maximum.append(duplicated[i])
    return maximum
    


if __name__ == '__main__':
    cases = int(input())
    cases_table = []
    for i in range (cases):
        machinescount= int(input())
        st = input()
        
        m=[st.split(" ",machinescount)]
        n=[int(x) for x in m[0]]
        cases_table.append(n)
    for i in range(cases):
        n=CoffeeBreak(cases_table[i])
        for i in range(len(n)):
           print(n[i], end=" ")
        print()
