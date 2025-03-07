# -*- coding: utf-8 -*-
"""Stack.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D6HdvCAapy1Zd3VcemX-wotxxNMajvgM
"""

#This creates a list which will follow the last in first out principle. It will be useful in many cases.
class stack:
    def __init__(self):
        self.stack = []

    def push(self, item, index):
        temp = [item , index]
        self.stack.append(temp)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1][0]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

#This function will check whether the given string contains brackets in an ordered/balanced manner or not.
opening = ['(', '[', '{']
closing = [')', ']', '}']
def balanced(str):
  mystack = stack()
  for i in str:
    if i in opening:
      mystack.push(i)
    else:
      index = closing.index(i)
      if mystack.is_empty() == False and opening[index] == mystack.peek():
        mystack.pop()
      else:
        return 'unbalanced'
  if mystack.is_empty() == False:
    return 'unbalanced'
  return 'balanced'

#This function helps us to find the next greater integer for every selected integer.
def next_greater(list):
    ans = [-1] * len(list)
    mystack = stack()
    for i in range(len(list)):
      if mystack.is_empty() == True or list[i] < mystack.peek():
        mystack.push(list[i], i)
      else:
        while mystack.is_empty() == False and list[i] > mystack.peek():
          removed = mystack.pop()
          ans[removed[1]] = list[i]
        mystack.push(list[i], i)
    return ans

def postfix_calculator(str):
  ops = ['+', '-', '*', '/']
  mystack = stack()
  for i in str:
    if i in ops:
      num2 = mystack.pop()
      num1 = mystack.pop()
      if i == '+':
        mystack.push(num1 + num2)
      if i == '-':
        mystack.push(num1 - num2)
      if i == '*':
        mystack.push(num1 * num2)
      if i == '/':
        mystack.push(num1 / num2)
    else:
      mystack.push(int(i))
  return mystack.pop()

def postfixtoinfix_convertor(str):
  ops = ['+', '-', '*', '/']
  mystack = stack()
  for i in str:
    if i in ops:
      num2 = mystack.pop()
      num1 = mystack.pop()
      mystack.push('('+num1+i+num2+')')
    else:
      mystack.push(i)
  return mystack.pop()

def priority_calculator(operator):
    if operator == '*' or operator == "/":
      return 1
    return 0

def infixtopostfix_convertor(str):
    ans = ''
    ops = ['+', '-', '*', '/']
    mystack = stack()
    for i in str:
      if i in ops:
        while mystack.is_empty() == False and priority_calculator(i) < priority_calculator(mystack.peek()):
          ans += mystack.pop()
        mystack.push(i)
      else:
        ans += i
    while mystack.is_empty() == False:
      ans += mystack.pop()
    return ans

def largest_rectangle(list):
  n = len(list)
  rightstack = stack()
  nextsmallright = [n] * n
  for i in range(n):
    if rightstack.is_empty() == True:
      rightstack.push(list[i], i)
    else:
      while rightstack.is_empty == False and list[i] < rightstack.peek():
        removed = rightstack.pop()
        nextsmallright[removed[1]] = i
      rightstack.push(list[i], i)

  leftstack = stack()
  nextsmallleft = [-1] * n
  for i in range(n-1, -1, -1):
    if leftstack.is_empty() == True:
      leftstack.push(list[i], i)
    else:
      while leftstack.is_empty == False and list[i] < leftstack.peek():
        removed = leftstack.pop()
        nextsmallleft[removed[1]] = i
      leftstack.push(list[i], i)

  ans = 0
  for i in range(n):
    tempAns = list[i]
    tempAns += list[i] * (nextsmallright[i] - i - 1)
    tempAns += list[i] * (i - nextsmallleft[i] - 1)
    ans = max(ans, tempAns)
  print(nextsmallleft)
  print(nextsmallright)
  return ans