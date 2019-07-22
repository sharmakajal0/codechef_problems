T = int(input())
for _ in range(0, T):
    expr = list(input())
    stack = []
    answer = ''

    for i in expr:
        if (i == '('):
            stack.append('(')
        elif (i >= 'a' and i <= 'z'):
            answer = answer + i
        elif (i == ')'):
            while (stack[-1] != '('):
                answer = answer + stack.pop()
            
            stack.pop()
            print(stack)
        else:
            stack.append(i)
    print(answer)