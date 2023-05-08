
while True:
  string = input()

  if string == ".":
    break

  stack = []

  for s in string:
    if s == "(" or s == "[":
      stack.append(s)
    elif s == ")":
      if len(stack) != 0 and stack[-1] == "(":
        stack.pop()
      else:
        stack.append(")")
        break
    elif s == "]":
      if len(stack) != 0 and stack[-1] == "[":
        stack.pop()
      else:
        stack.append("]")
        break
  
  if len(stack) == 0:
    print("yes")
  else:
    print("no")