# queue
from collections import deque

def solution(s):
  queue = deque(s)
  ans = 0
  for _ in range(len(s)):
    x = queue.popleft()
    queue.append(x)
    
    if check_bracket(queue):
      ans += 1

  return ans

def check_bracket(x):
  stack = []
  for i in x:
    if i in "([{":
      stack.append(i)
    else:
      if len(stack) == 0:
        return False
      
      if i == "]":
        if stack[-1] == "[":
          stack.pop()
        else:
          return False
      elif i == ")":
        if stack[-1] == "(":
            stack.pop()
        else:
            return False
      elif i == "}":
        if stack[-1] == "{":
            stack.pop()
        else:
            return False
  
  return len(stack) == 0



print(solution("[)(]"))