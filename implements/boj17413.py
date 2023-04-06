# 단어 뒤집기 2
# 구현

s = input()
stack = []
in_tag = False

for c in s:
    if c == '<':
        # 스택에 저장된 문자열 출력
        while stack:
            print(stack.pop(), end='')
        in_tag = True
        print(c, end='')
    elif c == '>':
        in_tag = False
        print(c, end='')
    elif in_tag:
        # 태그 안의 문자열 그대로 출력
        print(c, end='')
    else:
        if c == ' ':
            # 스택에 저장된 문자열 출력
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')
        else:
            stack.append(c)

# 스택에 저장된 문자열 출력
while stack:
    print(stack.pop(), end='')