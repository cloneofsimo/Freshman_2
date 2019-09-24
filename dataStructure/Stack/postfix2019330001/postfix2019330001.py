f1 = open('postfix.in','r')
comds = f1.read().split('\n')
f2 = open('postfix.out','w')
print(comds)
string = ''
while comds:
    r = comds.pop(0)
    #print(r)
    if not r in ['',' ']:
        pfexp = list(r)
        #print(pfexp)

        stack = []
        while pfexp:

            expr = pfexp.pop(0)
            if expr != ' ':
                #print(expr)
                #print(stack)
                if not expr in ['-','+','/','*']:
                    stack.append(expr)
                else:
                    r1 = stack.pop()
                    r2 = stack.pop()
                    command = ''.join([str(r2),expr,str(r1)])
                    stack.append(eval(command))
        string = string + str(stack.pop()) + '\n'
f2.write(string)
print(string)
