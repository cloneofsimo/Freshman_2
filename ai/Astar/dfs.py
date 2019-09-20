
from collections import defaultdict

# def convert(list):
#
#     # Converting integer list to string list
#     s = [str(i) for i in list]
#
#     # Join list items using join()
#     res = int("".join(s))
#
#     return(res)

# Driver code
def printasinf(vect):
    arr = []
    alp = ['a','b','c','d','e','f','g','h','i']
    for x in range(9):
        for y in range(9):
            if vect[x] == alp[y]:
                arr.append(y)
    return arr

def inttostring(vect):
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



class Graph:
    def __init__(self,inistate):
        self.edges = []
        self.inistate = inistate
        self.visited = defaultdict(int)
        self.sedges = defaultdict(str)
    def bfs(self):

        queue = []

        queue.append(self.inistate)
        self.visited["".join(self.inistate)] = 1

        ordered = ['a','b','c','d','e','f','g','h','i']
        while queue:
            currentstate = queue.pop() #Only difference with bfs
            # swith is wrong...
            for nextstate in switch1(currentstate):
                snxt = "".join(nextstate)
                if self.visited[snxt] == 0:

                    print("hi")
                    print(snxt)
                    queue.append(nextstate)
                    self.visited[snxt] = 1
                    self.edges.append((nextstate,currentstate))
                    self.sedges[snxt] = "".join(currentstate)
                    if issamelist(ordered,nextstate):
                        return self.showsteps(nextstate)

        return print(ordered)

    def showsteps(self, state):
        step = 0
        parentstate = state.copy()
        print('yo')
        while issamelist(parentstate,self.inistate)==False:
            succ = self.sedges["".join(parentstate)]
            parentstate = succ
            step = step + 1
        return print(step)
            # print(self.edges)
            # pasttake = self.edges[pasttake]




node2 = [7,2,4,5,0,6,8,3,1]
g = Graph(inttostring(node2))
print(inttostring(node2))
g.bfs()
