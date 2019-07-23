#!/usr/bin/env python

'''module for transformation of infix to postfix'''

def infix_topostfix(infix_exp):

    '''Function definition to transform an infix expression into postfix expression'''
    stack = []
    answer = ''

    for i in infix_exp:
        if i == '(':
            stack.append('(')
        elif i >= 'a' and i <= 'z':
            answer = answer + i
        elif i == ')':
            while stack[-1] != '(':
                answer = answer + stack.pop()

            stack.pop()
        else:
            stack.append(i)
    return answer

T = int(input())
for _ in range(0, T):
    expr = list(input())
    print(infix_topostfix(expr))
