# SWEA 1222 계산기1
# SWEA 1222

# Created by sw0817 on 2020. 09. 22..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14mbSaAEwCFAYD&categoryId=AV14mbSaAEwCFAYD&categoryType=CODE


for tc in range(1, 11):
    L = int(input())
    text = input()
    infix = list(text)
    stack = []
    operator = ['*', '/', '+', '-']
    bracket = ['(', ')']
    result = []

    def prior(a):
        if a is '*' or a is '/':
            return 2
        elif a is '+' or a is '-':
            return 1
        elif a is '(' or a is ')':
            return 0

    def number(a):
        if a not in operator and a not in bracket:
            return True
        else:
            return False

    for a in infix:
        if number(a):
            result.append(int(a))
        elif a in operator:
            while len(stack) > 0:
                if prior(stack[-1]) <= prior(a):
                    break
                result.append(stack.pop())
            stack.append(a)
        elif a == '(':
            stack.append(a)
        elif a == ')':
            while True:
                b = stack.pop()
                if b == '(':
                    break
                result.append(b)
    while len(stack) > 0:
        result.append(stack.pop())

    while len(result) != 1:
        for i in range(len(result)):
            if result[i] in operator:
                if result[i] == '+':
                    result[i] = result[i-2] + result[i-1]
                elif result[i] == '-':
                    result[i] = result[i-2] - result[i-1]
                elif result[i] == '*':
                    result[i] = result[i-2] * result[i-1]
                elif result[i] == '/':
                    result[i] = result[i-2] / result[i-1]
                result.pop(i-2)
                result.pop(i-2)
                break

    print('#{} {}'.format(tc, result[0]))
