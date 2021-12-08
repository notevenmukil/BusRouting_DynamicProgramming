file1 = open("memoization.txt", "w")

def busRoute(i, s, graph):
    h = i

    #adjustment for i
    if i == 0:
        f = 0
    elif i > 0:
        f = (i * 2) - 1
    else:
        f = i * -2
    i = f
    
    if s == []:
        a = graph[i][len(graph)-1]
        return a
    
    elif len(s) == 2:
        a = graph[i][(s[0]*2)-1]
        b = graph[(s[0]*2)-1][len(graph)-1]
        c = graph[i][(s[1]*-2)]
        d = graph[(s[1]*-2)][len(graph)-1]
        a = a + b
        c = c + d

        v = str(s.copy())
        v = v.replace(" ", "")

        n = min(a,c)
        if n == a:
            line = str(h) + " " + str(s[0]) + " " + str(v) + " " + str(a) + "\n"
        else:
            line = str(h) + " " + str(s[1]) + " " + str(v) + " " + str(b) + "\n"
        file1.write(line)
        
        s.clear()
        return n
    else:
        l = []
        for j in s:
            if j > 0:
                m = (j * 2) - 1
            else:
                m = j * -2
                
            a = graph[i][m]
            x = s.copy()
            x.remove(j)
            x.remove(j*-1)
            b = a + busRoute(j, x, graph)
            v = str(s.copy())
            v = v.replace(" ", "")
            line = str(h) + " " + str(j) + " " + str(v) + " " + str(b) + "\n"
            file1.write(line)
            l.append(b)
        l.sort()
        return l[0]

def backtrack(s, mini):
    file2 = open("memoization.txt", "r")
    lines = file2.readlines()
    file2.close()

    memo = []
    for line in lines:
        y = line.strip()
        x = y.split(" ")
        a = [z for z in x]
        memo.append(a)

    q = 0
    l = len(s) - 2
    r = []
    c = []
    path = []
    miniset = []
    for i in memo:
        i[2] = i[2].replace(",", ", ")
        c.append(i)
        if i[2] == str(s):  #identifying full sets
            q = 1
        if q == 1 and mini == int(i[3]):    #if the cost of this route is equal to minimum
            r.clear()
            r.append(int(i[0]))
            r.append(int(i[1]))
            end = int(i[1])
            
            while l > 0:
                miniset.clear()
                for j in c:
                    k = j[2].strip("[")
                    k = k.strip("]")
                    k = k.split(", ")
                    if end == int(j[0]) and l == len(k):
                        miniset.append([int(j[1]), int(j[3])])
                l = l - 2
                x = [z[1] for z in miniset]
                if x != []:
                    p = min(x)
                    index = x.index(p)
                    r.append(miniset[index][0])
                    end = miniset[index][0]
            r.append((len(s)//2)+1)
            w = r.copy()
            path.append(w)
        if q == 1:
            q = 0
            l = len(s) - 2
            c.clear()

    print("PATHS ARE : ", path)

# driver function
def main():
    file = open("graph.txt", "r")
    lines = file.readlines()
    file.close()

    graph = []
    for line in lines:
        y = line.strip()
        x = y.split(" ")
        a = [int(z) for z in x]
        graph.append(a)

    #global s
    s = []
    for i in range(1, len(graph)//2):
        s.append(i)
        s.append(i*-1)

    #global mini
    mini = busRoute(0, s, graph)
    file1.close()
    print("MINIMUM COST : ", mini)
    backtrack(s, mini)

main()

'''
file1.close()

backtrack(s, mini)
'''
