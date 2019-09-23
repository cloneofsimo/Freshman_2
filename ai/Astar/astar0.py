from collections import defaultdict


def stateasint(vect):
    arr = []
    alp = ['a','b','c','d','e','f','g','h','i']
    for x in range(9):
        for y in range(9):
            if vect[x] == alp[y]:
                arr.append(y)
    return arr

def inttostate(vect):
    arr = []
    alp = ['a','b','c','d','e','f','g','h','i']
    for x in range(9):
        arr.append(alp[vect[x]])
    return arr

def issamelist(a,b):
    for x in range(9):
        if a[x] != b[x]:
            return False

    return True

def swap(vect, i, j):
    temp = vect[i]
    vect[i] = vect[j]
    vect[j] = temp
    return vect

def isarrinarr(item,array):
    for x in array:
        if issamelist(item,x):
            return True
    return False

def switch1(vector):
    list = []
    pos0 = 0
    for x in range(9):
        if vector[x] == 'a':
            pos0 = x
    x1 = pos0%3
    y1 = (pos0)//3
    r1 = (x1+1,y1)
    r2 = (x1-1,y1)
    r3 = (x1,y1+1)
    r4 = (x1,y1-1)
    chart = [r1,r2,r3,r4]
    while chart:
        pos = chart.pop(0)
        if (0 <= pos[0]) and (0 <= pos[1]) and (pos[0] <= 2) and (pos[1]<=2):

            ras = pos[0]+pos[1]*3
            rector = vector.copy()
            list.append(swap(rector, pos0, ras))
    return list

def h1(vector):
    ordered = "abcdefghi"
    value =0
    for x in range(9): #for a~ i
        posalp =0  #position of alphabet
        for pos in range(9): #find the position of ordered[x]
            if ordered[x] == vector[pos]:
                posalp = pos
        posalpy = posalp//3
        orialpy = x//3
        posalpx = posalp%3
        orialpx = x%3
        value = value + abs(posalpx-orialpx) + abs(posalpy-orialpy)
    return value





class Graph:
    def __init__(self,inistate):
        self.inistate = inistate
    def lds(self):
        self.visited = defaultdict(int)
        self.sedges = defaultdict(str)
        priory = defaultdict(int)
        depth = 1
        stack = []
        stack.append(self.inistate)
        inistr="".join(self.inistate)
        self.visited[inistr] = 1
        priory[inistr] = h1(inistr) + depth

        ordered = ['a','b','c','d','e','f','g','h','i']
        while stack:
            cs = min(priory.keys(), key=(lambda k: priory[k]))
            currentstate = list(cs)
            del priory[cs]
            for nextstate in switch1(currentstate):
                snxt = "".join(nextstate)
                scru = "".join(currentstate)
                if self.visited[snxt] == 0:

                    print(depth)
                    print(snxt)
                    stack.append(nextstate)
                    self.visited[snxt] = self.visited[scru]+1
                    self.sedges[snxt] = scru
                    depth = self.visited[snxt]
                    priory[snxt] = depth + h1(snxt)
                    if issamelist(ordered,nextstate):
                        self.showsteps(nextstate)
                        return True

        return False

    def showsteps(self, state):
        step = 0
        parentstate = state.copy()
        print('yo')
        while issamelist(parentstate,self.inistate)==False:
            succ = self.sedges["".join(parentstate)]
            parentstate = succ
            print(stateasint(succ))
            step = step + 1
        return print(step)

    def ids(self):
        found = False
        n = 1
        while found == False:
            found = self.lds(n)
            n = n+1



node1 = [1,2,0,4,5,3,6,7,8]
node2 = [7,2,4,5,0,6,8,3,1]
print(h1("badcefghi"))
g = Graph(inttostate(node2))
print(inttostate(node1))
g.lds()
