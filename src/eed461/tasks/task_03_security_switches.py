def turnOffSwitches(n):
    def solve(m):
        if(m==0):
            return []
        elif(m==1):
            return [1]
        a = []
        b = []
        result = []
        for x in solve(m-2):
            a.append(x+2)
        for x in solve(m-1):
            b.append(x+1)


        for x in a:
            result.append(x)
        result.append(1)
        for i in range(len(a)-1,-1,-1):
            result.append(a[i])
        for x in b:
            result.append(x)
        return result

    toggles = solve(n)
    min_moves= len(toggles)
    return min_moves,toggles