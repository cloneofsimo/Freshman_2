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
        if vector[x] == 0:
            pos0 = x
    x1 = pos0%3
    y1 = (pos0)//3
    r1 = (x1+1,y1)
    r2 = (x1-1,y1)
    r3 = (x1,y1+1)
    r4 = (x1,y1-1)
    chart = [r1,r2,r3,r4]
    print(chart)
    t =(4,4)
    while chart:
        pos = chart.pop(0)
        if (0 <= pos[0]) and (0 <= pos[1]) and (pos[0] <= 2) and (pos[1]<=2):
            print(t)
            ras = pos[0]+pos[1]*3
            rector = vector.copy()
            list.append(swap(rector, pos0, ras))
    return list

init = [6,1,4,3,2,0,5,7,8]
#
l = switch1(init)
#
print(l)
item = [1,2,3]
if not 5 in item:
    print("hi")


0 1 2
3 4 5
6 7 8
